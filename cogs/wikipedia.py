# imports
import discord
import wikipediaapi
from discord.ext import commands


class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=["wikipedia"])
    async def wiki(self, ctx):
        await ctx.message.delete(delay=10)
        await ctx.send(f"{ctx.author.mention} please specify some task :)", delete_after=10)

    @wiki.command(aliases=["s"])
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
            await ctx.message.delete(delay=10)
            await ctx.send(f"{ctx.author.mention} please specify a valid Wikipedia Page :)", delete_after=10)

    @wiki.command(aliases=["f"])
    async def full(self, ctx, *, query: str):
        ww = wikipediaapi.Wikipedia(language="en", extract_format=wikipediaapi.ExtractFormat.WIKI)
        page = ww.page(query)

        if page.exists():
            title = page.title
            content = page.text

            pager = commands.Paginator()
            pager.add_line(line=f"Title : {title}")
            pager.add_line(line=f"Full Text - ")

            for line in content.splitlines(keepends=True):
                if len(line) < 1992:
                    pager.add_line(line)
                else:
                    lines = line.split(".")
                    for sl in lines:
                        pager.add_line(sl)

            for page in pager.pages:
                try:
                    await ctx.author.send(page)
                except discord.Forbidden:
                    await ctx.message.delete(delay=10)
                    await ctx.send(f"{ctx.author.mention} Could not DM you :)", delete_after=10)
                    break

        else:
            await ctx.send(f"{ctx.author.mention} please specify a valid Wikipedia Page :)")


def setup(client):
    client.add_cog(Wikipedia(client))
