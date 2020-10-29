# discord imports
import discord
from discord.ext import commands

# other imports
import datetime
import img

# functions
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour=discord.Colour.light_gray()
    )
    Embed.set_author(name=author, icon_url=img.ImgTodo)
    return Embed


class ToDo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=["td"])
    async def todo(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed = SimpleEmbed("Please provide a 'todo' command"), delete_after=10)

    @todo.command()
    async def insert(self, ctx, *, text: str):
        """ Inserts task into your todo list """
        async with ctx.channel.typing():
            await ctx.message.delete()
            work = await commands.clean_content().convert(ctx=ctx, argument=text)
            open_dms = False

            try:
                await ctx.author.send(embed = SimpleEmbed(f"Todo - {work}"))
                open_dms = True

            except discord.Forbidden:
                await ctx.send(embed = SimpleEmbed("The bot is not able to DM you, please check your privacy settings"), delete_after=10)
                open_dms = False

            if open_dms:
                user_id = ctx.author.id
                check = await self.client.db.check_from_todo(user_id, work)
                if not check:
                    time = str(datetime.datetime.utcnow())
                    await self.client.db.insert_into_todo(user_id, work, time)
                    return
                await ctx.send(f"{ctx.author.mention} a work already exists of that name", delete_after=10)

    @todo.command()
    async def delete(self, ctx, *, text: str):
        """ Deletes a task from your todo list """
        async with ctx.channel.typing():
            await ctx.message.delete()
            user_id = ctx.author.id
            work = await commands.clean_content().convert(ctx=ctx, argument=text)
            check = await self.client.db.check_from_todo(user_id, work)

            if not check:
                await ctx.send(f"{ctx.author.mention} no work found")
                return

            await self.client.db.delete_from_todo(user_id, work)
            await ctx.send(embed = SimpleEmbed("Task deleted successfully!"))

    @todo.command()
    async def all(self, ctx):
        """ Gets all the task in your todo list """
        async with ctx.channel.typing():
            user_id = ctx.author.id
            query = await self.client.db.select_all_from_todo(user_id)
            if not query:
                await ctx.message.delete()
                await ctx.send(f"{ctx.author.mention} you dont have any tasks yet")
                return

            records = []

            for record in query:
                time = str(record["time"]).split(".")
                schedule = f"{time[0]} - {record['work']}"
                records.append(schedule)

            pager = commands.Paginator()

            for line in records:
                pager.add_line(line)

            for page in pager.pages:
                try:
                    await ctx.author.send(page)
                except discord.Forbidden:
                    await ctx.send(f"{ctx.author.mention} cant DM you!")


def setup(client):
    client.add_cog(ToDo(client))
