# discord imports
import discord
from discord.ext import commands

# dictionary imports
from PyDictionary import PyDictionary
dictionary = PyDictionary()


class dictionary(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def define(self, ctx, arg):
        Definition = dictionary.meaning(arg)
        
        DefinitionEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        DefinitionEmbed.set_author(name = 'Definition of "{}"'.format(arg))
        
        for i in range(len(Definition)):
            CurrentDef = str(Definition[list(Definition)[i]]).replace("[", "").replace("]", "")
            DefinitionEmbed.add_field(name = list(Definition)[i], value=CurrentDef, inline=False)
        
        await ctx.send(embed = DefinitionEmbed)

    
    @commands.command()
    async def synonym(self, ctx, arg):
        Synonyms = str(dictionary.synonym(arg)).replace("[", "").replace("]", "").replace("'", "").split(",")
        
        string = ""
        for i in range(len(Synonyms)):
            string = "{0}\n{1}".format(string, Synonyms[i])
        
        SynonymEmbed = discord.Embed(
            colour = discord.Colour.light_gray(),
            description = string
        )
        SynonymEmbed.set_author(name='Synonyms for "{}"'.format(arg))

        await ctx.send(embed = SynonymEmbed)


def setup(client):
    client.add_cog(dictionary(client))