# imports
import discord
from discord.ext import commands

# other imports
import img


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def purge(self, ctx, amount=100):
        """ Bulk deletes the messages in the channel """
        channel = ctx.channel
        await channel.purge(limit=amount)

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason: str = None):
        """ Kicks the member """
        KickedEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        KickedEmbed.set_author(name = f"{user.display_name} has been kicked for : {reason}", icon_url=img.ImgMain)
        await ctx.send(embed = KickedEmbed)
        await user.kick(reason=reason)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason: str = None):
        """ Bans the member """
        BannedEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        BannedEmbed.set_author(name = f"{user.display_name} has been banned for : {reason}", icon_url=img.ImgMain)
        await ctx.send(embed = BannedEmbed) 
        await user.ban(reason=reason)


def setup(client):
    client.add_cog(Moderation(client))
