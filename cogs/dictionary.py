# discord imports
import aiohttp
import discord

# dictionary imports
from PyDictionary import PyDictionary
from discord.ext import commands

# other imports
import img


class dictionary(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def dict(self, ctx):
        async with ctx.channel.typing():
            TaskErrorEmbed = discord.Embed(
                colour=discord.Colour.light_gray()
            )
            await ctx.message.delete()
            TaskErrorEmbed.set_author(name="Please specify a dict task!", icon_url=img.ImgDictionary)
            await ctx.send(embed=TaskErrorEmbed, delete_after = 10)


    # define command
    @dict.command(aliases = ["def"])
    async def define(self, ctx, arg):
        dictionary = PyDictionary()
        
        Definition = dictionary.meaning(arg)
        
        DefinitionEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        DefinitionEmbed.set_author(name = 'Definition of "{}"'.format(arg))
        
        for i in range(len(Definition)):
            CurrentDef = str(Definition[list(Definition)[i]]).replace("[", "").replace("]", "")
            DefinitionEmbed.add_field(name = list(Definition)[i], value=CurrentDef, inline=False)
        
        await ctx.send(embed = DefinitionEmbed)


    # urban defs
    @dict.command()
    async def urban(self, ctx, *, arg: str):
        """ Finds the meaning of a word """
        async with ctx.channel.typing():
            word = await commands.clean_content().convert(ctx=ctx, argument=arg)

            url = f"https://api.urbandictionary.com/v0/define?term={word}"

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    json = await response.json()

            if not json:
                await ctx.send("Oh no! Our sources are down ATM, Please try again :)")
                return

            if not len(json["list"]):
                await ctx.send(f"{ctx.author.mention} cant find that word in the dictionary")
                return

            data = json["list"][0]

            meaning = discord.Embed(colour=discord.Colour.light_gray())

            meaning.set_author(name=f"Definition of {data['word']}", icon_url=img.ImgDictionary)
            meaning.description = f"\n {data['definition']} \n"
            meaning.description += f"\n **Example** \n {data['example']} \n"
            meaning.description += f"\n You can read more here at - {data['permalink']} \n"
            meaning.description += f"\n 👍 - {data['thumbs_up']} \n"
            meaning.description += f"\n 👎 - {data['thumbs_down']} \n"
            meaning.set_footer(text=f"Requested by - {ctx.author}")
            await ctx.send(embed=meaning)

    # synonyms
    @dict.command(aliases=["syn"])
    async def synonym(self, ctx, arg):
        """ Finds the synonym of a word """
        async with ctx.channel.typing():
            Synonyms = str(PyDictionary().synonym(arg)).replace("[", "").replace("]", "").replace("'", "").split(
                ",")  # getting the synonyms and putting them in a list (while removing any characters that are not needed)

            # getting all the characters and putting them into one string, each word on a new line
            string = ""
            for i in range(len(Synonyms)):
                string = "{0}\n{1}".format(string, Synonyms[i])

            # creating the embed that the synonyms will be delivered in
            SynonymEmbed = discord.Embed(
                colour=discord.Colour.light_gray(),
                description=string
            )
            SynonymEmbed.set_author(name='Synonyms for "{}"'.format(arg), icon_url=img.ImgDictionary)

            # sending the embed
            await ctx.send(embed=SynonymEmbed)


def setup(client):
    client.add_cog(dictionary(client))
