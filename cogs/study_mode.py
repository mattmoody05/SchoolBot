import discord
from discord.ext import commands
from .DataBase.client import DataBase


class StudyMode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            record = await self.client.db.fetch_all_study_modes()
            if record:
                for id in record[0]:
                    if message.author.id == id:
                        await message.delete()
                        await message.channel.send(f"{message.author.mention} please go to study :)")
                        break

    @commands.command()
    async def study_mode(self, ctx):
        check = await self.client.db.check_study_mode(ctx.author.id)
        if not check:
            await self.client.db.insert_study_mode(ctx.author.id)
            await ctx.send(f"Study Mode On!")
        else:
            if check[0][0]:
                await self.client.db.change_study_mode(ctx.author.id, False)
                await ctx.send(f"{ctx.author.mention} Study Mode Off!")
            else:
                await self.client.db.change_study_mode(ctx.author.id, True)
                await ctx.send(f"{ctx.author.mention} Study Mode On!")


def setup(client):
    client.add_cog(StudyMode(client))