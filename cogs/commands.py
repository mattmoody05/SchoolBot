# imports
import asyncio

import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency - {round(self.client.latency * 1000)}")

    @commands.command()
    async def timer(self, ctx, hour: int, minute: int, second: int):
        hour_seconds = hour * 60 * 60
        minute_seconds = minute * 60
        seconds = hour_seconds + minute_seconds + second

        time = {}
        if hour != 0:
            time["hour"] = hour
        if minute != 0:
            time["minute"] = minute
        if second != 0:
            time["second"] = second

        record = "Timer added for - "
        for key, value in time.items():
            if value == 1:
                record += f"{value} {key} "
            else:
                record += f"{value} {key + 's'} "

        TimerEmbed = discord.Embed(
            colour=discord.Colour.light_gray()
        )
        TimerEmbed.set_author(name=record)
        await ctx.send(embed=TimerEmbed)

        await ctx.send(f"{ctx.author.mention} timer started!")
        await asyncio.sleep(seconds)
        await ctx.send(f"{ctx.author.mention} time over!")


def setup(client):
    client.add_cog(Commands(client))
