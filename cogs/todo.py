import discord
from discord.ext import commands
import datetime


class ToDo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=["td"])
    async def todo(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"{ctx.author.mention} please provide a task", delete_after=10)

    @todo.command()
    async def insert(self, ctx, *, text: str):
        await ctx.message.delete()
        work = await commands.clean_content().convert(ctx=ctx, argument=text)
        open_dms = False

        try:
            await ctx.author.send(f"Todo - {work}")
            open_dms = True

        except discord.Forbidden:
            await ctx.send("You cant use this because I need to DM you :), please change your Privacy settings to use this Command!", delete_after=10)
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
        await ctx.message.delete()
        user_id = ctx.author.id
        work = await commands.clean_content().convert(ctx=ctx, argument=text)
        check = await self.client.db.check_from_todo(user_id, work)

        if not check:
            await ctx.send(f"{ctx.author.mention} no work found")
            return

        await self.client.db.delete_from_todo(user_id, work)
        await ctx.send(f"Task deleted successfully!")

    @todo.command()
    async def all(self, ctx):
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
            await ctx.author.send(page)


def setup(client):
    client.add_cog(ToDo(client))
