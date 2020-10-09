import discord
from discord.ext import commands

from PyDictionary import PyDictionary
dictionary = PyDictionary()

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


def setup(client):
    client.add_cog(define(client))