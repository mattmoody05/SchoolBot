# imports
import discord
import wikipediaapi
from discord.ext import commands


class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def wiki(self, ctx):
        await ctx.send(f"{ctx.author.mention} please specify some task :)")

    @wiki.command()
    async def summary(self, ctx, *, query: str):
        ww = wikipediaapi.Wikipedia(language="en")
        page = ww.page(query)

        if page.exists():
            title = page.title
            summary = page.summary.split(".")

            read_more = f"\n\nYou can read more about this here : {page.fullurl}"

            embed = discord.Embed()
            embed.title = title
            embed.description = ". ".join(summary[:10])
            embed.description += read_more
            embed.set_footer(text=f"Requested by - {ctx.author}")

            await ctx.send(embed=embed)

        else:
            await ctx.send(f"{ctx.author.mention} please specify a valid Wikipedia Page :)")

    @wiki.command()
    async def full(self, ctx, *, query: str):
        ww = wikipediaapi.Wikipedia(language="en", extract_format=wikipediaapi.ExtractFormat.WIKI)
        page = ww.page(query)

        if page.exists():
            title = page.title
            content = page.text

            pager = commands.Paginator()
            pager.add_line(line=f"Title : {title}")
            pager.add_line(line=f"Full Text - ")

        else:
            await ctx.send(f"{ctx.author.mention} please specify a valid Wikipedia Page :)")


def setup(client):
    client.add_cog(Wikipedia(client))
