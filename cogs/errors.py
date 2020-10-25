# discord imports
import discord
from discord.ext import commands

# other imports
import img

# embeds
NoCommandFoundEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
NoCommandFoundEmbed.set_author(name="That command could not be found, please try again.", icon_url=img.ImgError)

UserPermissionsEmbed = discord.Embed(
    colour=discord.Colour.light_gray(),
    description="Please contact a admin if you think this is an issue."
)
UserPermissionsEmbed.set_author(name="You do not have the required permissions to run that command", icon_url=img.ImgError)

ArgsErrorEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
ArgsErrorEmbed.set_author(name="You have not provided required arguments. Please try again", icon_url=img.ImgError)

BotPermissionsEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
BotPermissionsEmbed.set_author(name="The bot does not have the relevant permissions to perform this command.", icon_url=img.ImgError)

MemberNotFoundEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
MemberNotFoundEmbed.set_author(name="Member not found!", icon_url=img.ImgError)

Valueerror = discord.Embed(colour=discord.Colour.light_gray())
Valueerror.set_author(name="Please Provide the correct data type", icon_url=img.ImgError)

ForbiddenError = discord.Embed(colour=discord.Colour.light_gray())
ForbiddenError.set_author(name="404 Forbidden Error!", icon_url=img.ImgError)


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(content=f"{ctx.author.mention}", embed=NoCommandFoundEmbed)

        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(content=f"{ctx.author.mention}", embed=UserPermissionsEmbed)

        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(content=f"{ctx.author.mention}", embed=ArgsErrorEmbed)

        elif isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send(content=f"{ctx.author.mention}", embed=BotPermissionsEmbed)

        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.send(content=f"{ctx.author.mention}", embed=MemberNotFoundEmbed)

        elif isinstance(error, discord.errors.Forbidden):
            await ctx.send(content=f"{ctx.author.mention}", embed=ForbiddenError)

        else:
            raise error


def setup(client):
    client.add_cog(Errors(client))
