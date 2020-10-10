# imports
import discord
from discord.ext import commands
import wikipediaapi


class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def wiki(self, ctx):
        await ctx.send(f"{ctx.author.mention} please specify some task :)")

    @wiki.command()
    async def summary(self, ctx, *, query: str):
        ww = wikipediaapi.Wikipedia('en')

        page = ww.page(query)

        title = page.title
        summary = page.summary
        print(title)
        total = summary.split(".")
        await ctx.send(". ".join(total[:5]))

def setup(client):
    client.add_cog(Wikipedia(client))
