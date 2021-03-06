# discord imports
import discord
from discord.ext import commands

# other imports
import img

# functions
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour=discord.Colour.light_gray()
    )
    Embed.set_author(name=author, icon_url=img.ImgTag)
    return Embed


class Tag(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def tag(self, ctx, *, command: str):
        """ Checks that if there is a tag or else throw a error """
        async with ctx.channel.typing():
            name = await commands.clean_content().convert(ctx=ctx, argument=command)
            records = await self.client.db.select_from_tag(name)
            if not records:
                await ctx.send(embed = SimpleEmbed("No tag found!"))
                return
            await ctx.send(records[0]["text"])
            await self.client.db.update_uses_in_tag(name)

    @tag.command()
    async def create(self, ctx, command: str, *, text: str):
        """
        Creates a tag (allowed for everyone because its only for students)
        <name> <text>
        eg. Hello Hello Mortals!
        """
        async with ctx.channel.typing():
            name = await commands.clean_content().convert(ctx=ctx, argument=command)
            content = await commands.clean_content().convert(ctx=ctx, argument=text)

            records = await self.client.db.select_from_tag(name)

            if records:
                await ctx.send(f"{ctx.author.mention} there is a tag of that name!")
                return

            user_id = ctx.author.id

            await self.client.db.insert_into_tag(user_id, name, content)
            await ctx.send(f"{ctx.author.mention} tag created Successfully!")

    @tag.command()
    async def delete(self, ctx, *, command: str):
        """ Deletes you tag if that exists """
        async with ctx.channel.typing():
            name = await commands.clean_content().convert(ctx=ctx, argument=command)
            user_id = ctx.author.id
            records = await self.client.db.select_user_tag(user_id, name)
            if not records:
                await ctx.send(embed = SimpleEmbed("No tag found!"))
                return
            await self.client.db.delete_from_tag(user_id, name)
            await ctx.send(f"{ctx.author.mention} tag deleted Successfully!")

    @tag.command()
    async def rename(self, ctx, command: str, name: str):
        """ Renames your tag """
        async with ctx.channel.typing():
            old_name = await commands.clean_content().convert(ctx=ctx, argument=command)
            new_name = await commands.clean_content().convert(ctx=ctx, argument=name)
            user_id = ctx.author.id
            records = await self.client.db.select_user_tag(user_id, old_name)
            if not records:
                await ctx.send(embed = SimpleEmbed("No tag found!"))
                return
            await self.client.db.rename_from_tag(user_id, old_name, new_name)
            await ctx.send(embed = SimpleEmbed("Tag renamed Successfully!"))

    @tag.command()
    async def edit(self, ctx, command: str, *, text: str):
        """ Edits your tag if it exists """
        async with ctx.channel.typing():
            name = await commands.clean_content().convert(ctx=ctx, argument=command)
            user_id = ctx.author.id
            records = await self.client.db.select_user_tag(user_id, name)
            if not records:
                await ctx.send(embed = SimpleEmbed("No tag found!"))
                return
            content = await commands.clean_content().convert(ctx=ctx, argument=text)
            await self.client.db.edit_from_tag(user_id, name, content)
            await ctx.send(embed = SimpleEmbed("Tag edited Successfully!"))

    @tag.command()
    async def all(self, ctx):
        """ Gives all the tags """
        async with ctx.channel.typing():
            records = await self.client.db.select_all_from_tag()

            if not records:
                await ctx.send(embed = SimpleEmbed("There are no tags yet!"))
                return

            pager = commands.Paginator()

            for record in records:
                pager.add_line(record["name"])

            for page in pager.pages:
                try:
                    await ctx.author.send(page)
                except discord.Forbidden:
                    await ctx.send(embed = SimpleEmbed("The bot is not able to DM you, please check your privacy settings"))

    @tag.command()
    async def list(self, ctx, mem: commands.MemberConverter = None):
        """ Gives a list of tag either of you or a person """
        async with ctx.channel.typing():
            member = mem or ctx.author
            records = await self.client.db.select_tag_of_member(member.id)
            if not records:
                await ctx.send(embed = SimpleEmbed("No tags found"))
                return

            pager = commands.Paginator()

            for record in records:
                pager.add_line(record["name"])

            for pages in pager.pages:
                await ctx.send(pages)

    @tag.command()
    async def info(self, ctx, *, command: str):
        """ Gives the info of the tag creator """
        async with ctx.channel.typing():
            name = await commands.clean_content().convert(ctx=ctx, argument=command)
            record = await self.client.db.info_of_tag(name)
            if not record:
                await ctx.send(embed = SimpleEmbed("No Tag Found!"))
                return
            user_id = int(record[0]["user_id"])
            user = await self.client.fetch_user(user_id)
            uses = int(record[0]["uses"])
            content = f"```css" \
                      f"\nName - {user}\nUses - {uses}```"
            await ctx.send(content)


def setup(client):
    client.add_cog(Tag(client))
