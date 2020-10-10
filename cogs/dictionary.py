import discord
from discord.ext import commands

from PyDictionary import PyDictionary
dictionary = PyDictionary()
import requests

class define(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def define(self, ctx, arg):
        Definition = dictionary.meaning(arg)
        NumberOfDefinitions = len(Definition)
        DefinitionEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        DefinitionEmbed.set_author(name = 'Definition of "{}"'.format(arg))
        for i in range(NumberOfDefinitions):
            DefinitionEmbed.add_field(name = list(Definition)[i], value=(Definition[list(Definition)[i]]), inline=False)
        
        await ctx.send(embed = DefinitionEmbed)

    
    @commands.command()
    async def synonym(self, ctx, arg):
        Synonyms = str(dictionary.synonym(arg)).replace("[", "").replace("]", "").split(",")
        await ctx.send(Synonyms)

        SynonymEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        SynonymEmbed.set_author(name='Synonyms for "{}"'.format(arg))
        for i in range(len(Synonyms)):
            SynonymEmbed.add_field(name=Synonyms[i], value=dictionary.meaning(Synonyms[i]))
            print(dictionary.meaning(Synonyms[i]))
        

        await ctx.send(embed = SynonymEmbed)

    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send("pong")



def setup(client):
    client.add_cog(define(client))