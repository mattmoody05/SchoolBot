import json

import discord
from discord.ext import commands
from youtube_search import YoutubeSearch


class Youtube(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["yt"])
    async def youtube(self, ctx, *args):
        """ Gets the details and url for a yt video as per the query """
        async with ctx.channel.typing():
            query = ""
            for i in range(len(args)):
                query = "{0}{1} ".format(query, args[i])

            resultsjson = json.loads(YoutubeSearch(query, max_results=1).to_json())

            SearchEmbed = discord.Embed(
                colour=discord.Colour.light_gray()
            )
            SearchEmbed.set_author(name="Youtube results for '{}'".format(query[:-1]))
            SearchEmbed.add_field(name="Video Title:", value=resultsjson['videos'][0]['title'], inline=False)
            SearchEmbed.add_field(name="Channel name:", value=resultsjson['videos'][0]['channel'], inline=False)
            SearchEmbed.add_field(name="Video URL:",
                                  value="https://youtube.com{}".format(resultsjson['videos'][0]['url_suffix']),
                                  inline=False)
            SearchEmbed.add_field(name="Views:", value=resultsjson['videos'][0]['views'])
            SearchEmbed.add_field(name="Duration:", value=resultsjson['videos'][0]['duration'])
            SearchEmbed.set_image(url=resultsjson['videos'][0]['thumbnails'][0])

            await ctx.send(embed=SearchEmbed)
            return


def setup(client):
    client.add_cog(Youtube(client))
