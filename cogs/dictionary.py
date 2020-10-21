# discord imports
import aiohttp
import discord
# dictionary imports
from PyDictionary import PyDictionary
from discord.ext import commands


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
    async def define(self, ctx, *, arg: str):
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

        meaning.set_author(name=f"Definition of {data['word']}")
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
