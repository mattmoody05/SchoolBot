# discord imports
import discord
from discord.ext import commands

# dictionary imports
from PyDictionary import PyDictionary


class dictionary(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def dict(self, ctx):
        TaskErrorEmbed = discord.Embed(
            colour=discord.Colour.light_gray()
        )
        await ctx.message.delete()
        TaskErrorEmbed.set_author(name="Please specify a dict task!", delete_after=10)
        await ctx.send(embed=TaskErrorEmbed)

    # definitions
    @dict.command(aliases=["def"])
    async def define(self, ctx, arg):
        Definition = PyDictionary().meaning(arg)  # getting the defintion using PyDictionary

        # creating the embed that the defintions will be delivered in
        DefinitionEmbed = discord.Embed(
            colour=discord.Colour.light_gray()
        )
        DefinitionEmbed.set_author(name='Definition of "{}"'.format(arg))

        try:
            # adding the definitions to the embed
            for i in range(len(Definition)):
                CurrentDef = str(Definition[list(Definition)[i]]).replace("[", "").replace("]", "")
                DefinitionEmbed.add_field(name=list(Definition)[i], value=CurrentDef, inline=False)

            # sending the embed
            await ctx.send(embed=DefinitionEmbed)
        except TypeError:
            await ctx.message.delete()
            await ctx.send(f"There is no meaning for this word :(", delete_after=10)
        except:
            raise

    # synonyms
    @dict.command(aliases=["syn"])
    async def synonym(self, ctx, arg):
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
        SynonymEmbed.set_author(name='Synonyms for "{}"'.format(arg))

        # sending the embed
        await ctx.send(embed=SynonymEmbed)


def setup(client):
    client.add_cog(dictionary(client))
