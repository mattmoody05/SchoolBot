# other imports
import inspect
import img

# discord imports
import discord
from discord.ext import commands


# functions
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour=discord.Colour.light_gray()
    )
    Embed.set_author(name=author, icon_url=img.ImgSource)
    return Embed


class Source(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def source(self, ctx, *, query: str):
        """ Gets the command and sends it to make it in the pages and send that """
        async with ctx.channel.typing():
            cmd = self.client.get_command(query)
            if cmd is None:
                await ctx.send(content=ctx.author.mention, embed=SimpleEmbed("This command is not found"))
                return
            try:
                source = inspect.getsource(cmd.callback)
                pager = await self.pager(source)

                for page in pager.pages:
                    page = page.replace("```", "")
                    await ctx.send(f"```py{page}```")
            except:
                await ctx.send(embed=SimpleEmbed(f"{ctx.author.name} This command is not found"))
                return

    async def pager(self, content):
        """ Converts the source into pages """
        pager = commands.Paginator()

        for line in content.splitlines():
            pager.add_line(line)

        return pager


def setup(client):
    client.add_cog(Source(client))
