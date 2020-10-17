import discord
from discord.ext import commands
import inspect


class Source(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def source(self, ctx, *, query: str):
        cmd = self.client.get_command(query)
        if cmd is None:
            await ctx.send(f"{ctx.author.mention} this command is not found")
            return
        try:
            source = inspect.getsource(cmd.callback)
            pager = await self.pager(source)

            for page in pager.pages:
                page = page.replace("```", "")
                await ctx.send(f"```py{page}```")
        except:
            await ctx.send(f"{ctx.author.mention} this command is not found")
            return

    async def pager(self, content):
        pager = commands.Paginator()

        for line in content.splitlines():
            pager.add_line(line)

        return pager


def setup(client):
    client.add_cog(Source(client))
