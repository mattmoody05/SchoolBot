# discord imports
import discord
from discord.ext import commands

# dictionary imports
from PyDictionary import PyDictionary
dictionary = PyDictionary()


class dictionary(commands.Cog):
    def __init__(self, client):
        self.client = client

    # definitions
    @commands.command()
    async def define(self, ctx, arg):
        Definition = dictionary.meaning(arg)  # getting the defintion using PyDictionary

        # creating the embed that the defintions will be delivered in
        DefinitionEmbed = discord.Embed(
            colour=discord.Colour.light_gray()
        )
        DefinitionEmbed.set_author(name='Definition of "{}"'.format(arg))

        # adding the definitions to the embed
        for i in range(len(Definition)):
            CurrentDef = str(Definition[list(Definition)[i]]).replace("[", "").replace("]", "")
            DefinitionEmbed.add_field(name=list(Definition)[i], value=CurrentDef, inline=False)

        # sending the embed
        await ctx.send(embed=DefinitionEmbed)

    # synonyms
    @commands.command()
    async def synonym(self, ctx, arg):
        Synonyms = str(dictionary.synonym(arg)).replace("[", "").replace("]", "").replace("'", "").split(
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
        SynonymEmbed.set_author(name='Synonyms for "{}"'.format(arg))

        # sending the embed
        await ctx.send(embed=SynonymEmbed)


def setup(client):
    client.add_cog(dictionary(client))
