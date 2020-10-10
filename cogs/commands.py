# imports
import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency - {round(self.client.latency * 1000)}")

    @commands.command()
    async def purge(self, ctx, amount=100):
        channel = ctx.channel
        await channel.purge(limit=amount)


def setup(client):
    client.add_cog(Commands(client))
