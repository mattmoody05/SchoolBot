import discord
from discord.ext import commands
from youtube-search import YoutubeSearch

class youtube(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command = True, aliases = ["yt"])
    async def youtube(self, ctx):
        TaskErrorEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        TaskErrorEmbed.set_author(name = "Please specify a math task!")
        await ctx.send(embed = TaskErrorEmbed)

    @youtube.command(aliases = ["s"])
    async def search(self, ctx, *args):
        query = ""
        for i in range(len(args)):
            query = "{0}{1} ".format(query, args[i])
        
        


def setup(client):
    client.add_cog(youtube(client))