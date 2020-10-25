import discord
from discord.ext import commands
import googletrans


class Translation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def translate(self, ctx, lang: str = None, *, text: str = None):
        """ Translates the text into specified language """
        async with ctx.channel.typing():
            if lang is not None and text is not None:
                language = await commands.clean_content().convert(ctx=ctx, argument=lang)
                content = await commands.clean_content().convert(ctx=ctx, argument=text)

                translator = googletrans.Translator()
                translated = translator.translate(content, dest=language)

                all_languages = googletrans.LANGUAGES

                translate_embed = discord.Embed(color=discord.Color.light_grey())
                translate_embed.set_author(name=translated.text)
                translate_embed.description = f"""Source - {str(all_languages[translated.src]).title()} \nTo - {str(all_languages[translated.dest]).title()} \nOriginal - {translated.origin} """

                await ctx.send(embed=translate_embed)
            else:
                await ctx.send(f"{ctx.author.mention} please specify a task")

    @translate.command()
    async def all(self, ctx):
        """ Gives the list of all the languages supported by the translator """
        async with ctx.channel.typing():
            all_languages = googletrans.LANGUAGES

            pager = commands.Paginator()

            for key, value in all_languages.items():
                pager.add_line(f"{key} - {value.title()}")

            for pages in pager.pages:
                await ctx.send(pages)

    @translate.command()
    async def detect(self, ctx, *, text: str):
        """ Detects the name of the language of the text """
        async with ctx.channel.typing():
            content = await commands.clean_content().convert(ctx=ctx, argument=text)

            translator = googletrans.Translator()
            detected = translator.detect(content)

            all_languages = googletrans.LANGUAGES
            language = str(all_languages[detected.lang]).title()

            await ctx.send(language)


def setup(client):
    client.add_cog(Translation(client))
