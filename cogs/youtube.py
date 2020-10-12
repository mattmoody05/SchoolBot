import discord
from discord.ext import commands
from youtube_search import YoutubeSearch
import json

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
        
        resultsjson = json.loads(YoutubeSearch(query, max_results=1).to_json())

        SearchEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        SearchEmbed.set_author(name = "Youtube results for '{}'".format(query[:-1]))
        SearchEmbed.add_field(name = "Video Title:", value = resultsjson['videos'][0]['title'], inline=False)
        SearchEmbed.add_field(name = "Channel name:", value = resultsjson['videos'][0]['channel'], inline=False)
        SearchEmbed.add_field(name = "Video URL:", value = "https://youtube.com{}".format(resultsjson['videos'][0]['url_suffix']), inline=False)
        SearchEmbed.add_field(name = "Views:", value = resultsjson['videos'][0]['views'])
        SearchEmbed.add_field(name = "Duration:", value = resultsjson['videos'][0]['duration'])
        SearchEmbed.set_image(url = resultsjson['videos'][0]['thumbnails'][0])

        await ctx.send(embed = SearchEmbed)


def setup(client):
    client.add_cog(youtube(client))