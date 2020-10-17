import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(f"{ctx.author.mention} No command found!")

        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f"{ctx.author.mention} You dont have required Permissions!")

        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} Please provide required arguments!")

        elif isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send(f"{ctx.author.mention} i'm missing permissions to do this!")

        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.send(f"{ctx.author.mention} Member Not Found!")

        else:
            print(error)


def setup(client):
    client.add_cog(Errors(client))
