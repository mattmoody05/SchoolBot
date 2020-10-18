# discord imports
import discord
from discord.ext import commands


# embeds
NoCommandFoundEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
NoCommandFoundEmbed.set_author(name = "That command could not be found, please try again.")

UserPermissionsEmbed = discord.Embed(
    colour = discord.Colour.light_gray(),
    description = "Please contact a admin if you think this is an issue."
)
UserPermissionsEmbed.set_author(name = "You do not have the required permissions to run that command")

ArgsErrorEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
ArgsErrorEmbed.set_author(name = "You have not provided required arguments. Please try again")

BotPermissionsEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
BotPermissionsEmbed.set_author(name = "The bot does not have the relevant permissions to perform this command.")

MemberNotFoundEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
MemberNotFoundEmbed.set_author(name = "Member not found!")



class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed = NoCommandFoundEmbed)

        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed = UserPermissionsEmbed)

        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed = ArgsErrorEmbed)

        elif isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed = BotPermissionsEmbed)

        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed = MemberNotFoundEmbed)

        else:
            raise error


def setup(client):
    client.add_cog(Errors(client))