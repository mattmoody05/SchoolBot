import discord
from discord.ext import commands


class StudyMode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["sm"])
    async def study_mode(self, ctx):
        if ctx.author.bot:
            return
        check = await self.client.db.check_study_mode(ctx.author.id)
        if not check:
            await self.client.db.insert_study_mode(ctx.author.id)
            await ctx.send(f"{ctx.author.mention} Study Mode On!")
        else:
            if check[0][0]:
                await self.client.db.change_study_mode(ctx.author.id, False)
                await ctx.send(f"{ctx.author.mention} Study Mode Off!")
            else:
                await self.client.db.change_study_mode(ctx.author.id, True)
                await ctx.send(f"{ctx.author.mention} Study Mode On!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and message.content.count("$study_mode") < 1:
            record = await self.client.db.fetch_all_study_modes()
            if record:
                mentions = [x.id for x in message.mentions if not x.bot]
                for author_id in record:
                    if message.author.id == author_id["user_id"]:
                        await message.delete()
                        await message.channel.send(f"{message.author.mention} please go to Study!")
                    if author_id["user_id"] in mentions:
                        await message.delete()
                        await message.channel.send(f"{message.author.mention} {self.client.get_user(author_id[0])} is studying please dont disturb him :)")


def setup(client):
    client.add_cog(StudyMode(client))