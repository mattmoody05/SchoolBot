# discord imports
import discord
from discord.ext import commands


# functions
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour=discord.Colour.light_gray()
    )
    Embed.set_author(name=author)
    return Embed


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
            await ctx.send(ctx.author.mention)
            await ctx.send(embed=SimpleEmbed("Study mode is now on"))
        else:
            if check[0][0]:
                await self.client.db.change_study_mode(ctx.author.id, False)
                await ctx.send(ctx.author.mention)
                await ctx.send(embed=SimpleEmbed("Study mode is now off"))
            else:
                await self.client.db.change_study_mode(ctx.author.id, True)
                await ctx.send(ctx.author.mention)
                await ctx.send(embed=SimpleEmbed("Study mode is now on"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and message.content.count("$study_mode") < 1:
            record = await self.client.db.fetch_all_study_modes()
            if record:
                mentions = [x.id for x in message.mentions if not x.bot]
                for author_id in record:
                    if message.author.id == author_id["user_id"]:
                        await message.delete()
                        await message.channel.send(message.author.mention)
                        await message.channel.send(embed=SimpleEmbed("Please go and study!"))
                    if author_id["user_id"] in mentions:
                        await message.delete()
                        await message.channel.send(message.author.metion)
                        await message.channel.send(
                            SimpleEmbed(f"{self.client.get_user(author_id[0])} is studying please dont disturb him :)"))


def setup(client):
    client.add_cog(StudyMode(client))
