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
        KickedEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        KickedEmbed.set_author(name = f"{user.display_name} has been kicked for : {reason}")
        await ctx.send(embed = KickedEmbed)
        await user.kick(reason=reason)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason: str = None):
        BannedEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        BannedEmbed.set_author(name = f"{user.display_name} has been banned for : {reason}")
        await user.ban(reason=reason)


def setup(client):
    client.add_cog(Moderation(client))
