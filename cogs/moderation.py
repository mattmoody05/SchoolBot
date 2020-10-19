# imports
import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def purge(self, ctx, amount=100):
        channel = ctx.channel
        await channel.purge(limit=amount)

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason: str = None):
        await ctx.send(f"{user.mention} has been kicked for : {reason}")
        await user.kick(reason=reason)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason: str = None):
        await ctx.send(f"{user.mention} has been banned for : {reason}")
        await user.ban(reason=reason)


def setup(client):
    client.add_cog(Moderation(client))
