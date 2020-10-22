# discord imports
import discord
from discord.ext import commands

# other imports
import asyncio
import random
from datetime import datetime


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # ping command
    @commands.command()
    async def ping(self, ctx):
        async with ctx.channel.typing():
            LatencyEmbed = discord.Embed(
                colour=discord.Colour.light_gray()
            )
            LatencyEmbed.set_author(name=f"Latency - {round(self.client.latency * 1000)}")
            await ctx.send(embed=LatencyEmbed)

    # timer command
    @commands.command()
    async def timer(self, ctx, hour: int, minute: int, second: int):
        async with ctx.channel.typing():
            hour_seconds = hour * 60 * 60
            minute_seconds = minute * 60
            seconds = hour_seconds + minute_seconds + second

            time = {}
            if hour != 0:
                time["hour"] = hour
            if minute != 0:
                time["minute"] = minute
            if second != 0:
                time["second"] = second

            record = "Timer added for - "
            for key, value in time.items():
                if value == 1:
                    record += f"{value} {key} "
                else:
                    record += f"{value} {key + 's'} "

            TimerEmbed = discord.Embed(
                colour=discord.Colour.light_gray()
            )
            TimerEmbed.set_author(name=record)
            await ctx.send(embed=TimerEmbed)

            await ctx.send(f"{ctx.author.mention} timer started!")
            await asyncio.sleep(seconds)
            await ctx.send(f"{ctx.author.mention} time over!")

    # dice roller
    @commands.command(aliases=["rd"])
    async def roll_dice(self, ctx):
        async with ctx.channel.typing():
            number = random.randint(1, 6)
            NumberEmbed = discord.Embed(
                colour=discord.Colour.light_gray()
            )
            NumberEmbed.set_author(name="Your number: {}".format(number))
            await ctx.send(embed=NumberEmbed)

    # rock paper scissors command
    @commands.command(aliases=["sps"])
    async def stone_paper_scissor(self, ctx, opt: str):
        async with ctx.channel.typing():
            options = ("stone", "paper", "scissor")
            num = random.randint(0, 2)
            if opt.lower() not in options:
                ErrorEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                ErrorEmbed.set_author(
                    name="{}, please provide a valid option - (stone, paper, scissor)".format(ctx.author.name))
                await ctx.send(embed=ErrorEmbed)
                return

            option = opt.lower()
            opponent = options[num]

            if option == "stone" and opponent == "stone":
                WonEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                WonEmbed.set_author(name="{0}, You won! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=WonEmbed)
                return
            if option == "stone" and opponent == "paper":
                LostEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                LostEmbed.set_author(name="{0}, You lost! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=LostEmbed)
                return
            if option == "stone" and opponent == "scissor":
                WonEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                WonEmbed.set_author(name="{0}, It was a tie! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=WonEmbed)
                return
            if option == "paper" and opponent == "stone":
                WonEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                WonEmbed.set_author(name="{0}, You won! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=WonEmbed)
                return
            if option == "paper" and opponent == "paper":
                TieEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                TieEmbed.set_author(name="{0}, It was a tie! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=TieEmbed)
                return
            if option == "paper" and opponent == "scissor":
                LostEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                LostEmbed.set_author(name="{0}, You lost! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=LostEmbed)
                return
            if option == "scissor" and opponent == "stone":
                LostEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                LostEmbed.set_author(name="{0}, You lost! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=LostEmbed)
                return
            if option == "scissor" and opponent == "paper":
                WonEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                WonEmbed.set_author(name="{0}, You won! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=WonEmbed)
                return
            if option == "scissor" and opponent == "scissor":
                TieEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                TieEmbed.set_author(name="{0}, It was a tie! The option was {1}".format(ctx.author.name, opponent))
                await ctx.send(embed=TieEmbed)
                return

    # number guessing game
    @commands.command(aliases=["ng"])
    async def number_guess(self, ctx):
        async with ctx.channel.typing():
            hidden_number = random.randint(1, 100)
            given_number = random.randint(1, 100)

            GivenNumberEmbed = discord.Embed(
                colour=discord.Colour.light_gray()
            )
            GivenNumberEmbed.set_author(name=f"The number is {given_number}. Enter higher or lower")
            await ctx.send(embed=GivenNumberEmbed)

            def check(message):
                content = str(message.content).lower()
                return content == "h" or content == "higher" or content == "l" or content == "lower"

            try:
                option = await self.client.wait_for("message", timeout=30, check=check)

                if option:
                    content = str(option.content).lower()

                    if (content == "higher" or content == "h") and hidden_number > given_number:
                        WonEmbed = discord.Embed(
                            colour=discord.Colour.light_gray()
                        )
                        WonEmbed.set_author(name=f"{ctx.author.name} You Won!")
                        await ctx.send(embed=WonEmbed)
                        return

                    if (content == "lower" or content == "l") and hidden_number < given_number:
                        WonEmbed = discord.Embed(
                            colour=discord.Colour.light_gray()
                        )
                        WonEmbed.set_author(name=f"{ctx.author.name} You Won!")
                        await ctx.send(embed=WonEmbed)
                        return

                    if hidden_number == given_number:
                        TieEmbed = discord.Embed(
                            colour=discord.Colour.light_gray()
                        )
                        TieEmbed.set_author(name=f"{ctx.author.name}, it was a tie")
                        await ctx.send(embed=TieEmbed)

                        return

                    LostEmbed = discord.Embed(
                        colour=discord.Colour.light_gray()
                    )
                    LostEmbed.set_author(name=f"{ctx.author.name} You lost :(")
                    await ctx.send(embed=LostEmbed)

                    return

                ErrorEmbed = discord.Embed(
                    colour=discord.Colour.light_gray()
                )
                ErrorEmbed.set_author(name=f"{ctx.author.name} please provide a valid option - (higher or lower)")
                await ctx.send(embed=ErrorEmbed)

            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} Time out error!")

    @commands.command(aliases=["mc"])
    async def member_count(self, ctx):
        async with ctx.channel.typing():
            on_mobile = 0
            online = 0
            idle = 0
            dnd = 0
            offline = 0
            total = len(ctx.guild.members)
            for member in ctx.guild.members:
                if member.is_on_mobile():
                    on_mobile += 1
                if member.status == discord.Status.online:
                    online += 1
                elif member.status == discord.Status.idle:
                    idle += 1
                elif member.status == discord.Status.dnd:
                    dnd += 1
                elif member.status == discord.Status.offline:
                    offline += 1

            OnlineMembersEmbed = discord.Embed(
                colour = discord.Colour.light_gray()
            )
            OnlineMembersEmbed.set_author(name = "Member counts")
            OnlineMembersEmbed.add_field(name = "Online", value = online)
            OnlineMembersEmbed.add_field(name = "Idle", value = idle)
            OnlineMembersEmbed.add_field(name = "Offline", value = offline)
            OnlineMembersEmbed.add_field(name = "Do not disturb", value = dnd)
            OnlineMembersEmbed.add_field(name = "Total", value = total)
            OnlineMembersEmbed.set_footer(text = f"Member count correct at: {str(datetime.now().time())[:8]}")
            await ctx.send(embed = OnlineMembersEmbed)


    @commands.has_permissions(administrator=True)
    @commands.command()
    async def announcement(self, ctx, topic: str, *, text):
        try:
            for channel in ctx.guild.channels:
                if channel.name.lower().count("announcement") > 0:
                    await ctx.message.delete()
                    announcement = discord.Embed(colour=discord.Colour.light_grey())
                    announcement.set_author(name=topic, icon_url=ctx.author.avatar_url)
                    announcement.description = text
                    announcement.set_footer(text=f"Announcement By - {ctx.author}")
                    await channel.send(content=ctx.guild.default_role, embed=announcement)
                    return
            else:
                await ctx.message.delete()
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False),
                }
                channel = await ctx.guild.create_text_channel(name="Announcement",
                                                              topic="This Channel is for servers Announcements",
                                                              overwrites=overwrites)
                announcement = discord.Embed(colour=discord.Colour.light_grey())
                announcement.set_author(name=topic, icon_url=ctx.author.avatar_url)
                announcement.description = text
                announcement.set_footer(text=f"Announcement By - {ctx.author}")
                await channel.send(content=ctx.guild.default_role, embed=announcement)
                return
        except discord.Forbidden:
            await ctx.send(f"{ctx.author.mention} I dont have permissions to do this!")


def setup(client):
    client.add_cog(Commands(client))
