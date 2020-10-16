import discord
from discord.ext import commands
from youtube_search import YoutubeSearch
import json
from pytube import YouTube
import os
import time

def YTDownloadVideo(url):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_lowest_resolution().download(filename = "temp")


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


    @youtube.command(aliases = ["v"])
    async def video(self, ctx, arg):
        VideoTitle = (YouTube(arg).title)
        GettingDownloadEmbed = discord.Embed(
            colour = discord.Colour.light_gray(),
            description = "Please note that videos are in low quality due to the discord upload cap"
        )
        GettingDownloadEmbed.set_author(name = "Getting video '{0}' from youtube".format(VideoTitle))
        if YouTube(arg).length > 120:
            TooLongEmbed = discord.Embed(
                colour = discord.Colour.light_gray(),
                description = "Due to the discord upload cap, you can only download videos that a shorter than 120 seconds in length"
            )
            TooLongEmbed.set_author(name = "The video you have requested is too long.")
            await ctx.send(embed = TooLongEmbed)
        else:
            await ctx.send(embed = GettingDownloadEmbed)
            YTDownloadVideo(arg)
            await ctx.send(file = discord.File("temp.mp4".format(VideoTitle)))
            time.sleep(1)
            os.remove("temp.mp4")


def setup(client):
    client.add_cog(youtube(client))