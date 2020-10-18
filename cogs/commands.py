# imports
import asyncio
import random
import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency - {round(self.client.latency * 1000)}")

    @commands.command()
    async def timer(self, ctx, hour: int, minute: int, second: int):
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

    @commands.command(aliases=["rd"])
    async def roll_dice(self, ctx):
        number = random.randint(1, 6)
        await ctx.send(number)

    @commands.command(aliases=["sps"])
    async def stone_paper_scissor(self, ctx, opt: str):
        options = ("stone", "paper", "scissor")
        num = random.randint(0, 2)
        if opt.lower() not in options:
            await ctx.send(f"{ctx.author.mention} please provide a valid option - (stone, paper, scissor)")
            return

        option = opt.lower()
        opponent = options[num]

        if option == "stone" and opponent == "stone":
            await ctx.send(f"{ctx.author.mention} It was a tie! The option was {opponent}")
            return
        if option == "stone" and opponent == "paper":
            await ctx.send(f"{ctx.author.mention} You lost! The option was {opponent}")
            return
        if option == "stone" and opponent == "scissor":
            await ctx.send(f"{ctx.author.mention} You won! The option was {opponent}")
            return
        if option == "paper" and opponent == "stone":
            await ctx.send(f"{ctx.author.mention} You won! The option was {opponent}")
            return
        if option == "paper" and opponent == "paper":
            await ctx.send(f"{ctx.author.mention} It was a tie! The option was {opponent}")
            return
        if option == "paper" and opponent == "scissor":
            await ctx.send(f"{ctx.author.mention} You lost! The option was {opponent}")
            return
        if option == "scissor" and opponent == "stone":
            await ctx.send(f"{ctx.author.mention} You lost! The option was {opponent}")
            return
        if option == "scissor" and opponent == "paper":
            await ctx.send(f"{ctx.author.mention} You won! The option was {opponent}")
            return
        if option == "scissor" and opponent == "scissor":
            await ctx.send(f"{ctx.author.mention} It was a tie! The option was {opponent}")
            return

    @commands.command(aliases=["ng"])
    async def number_guess(self, ctx):
        hidden_number = random.randint(1, 100)
        given_number = random.randint(1, 100)

        await ctx.send(f"The number is {given_number}. Enter higher or lower")

        def check(message):
            content = str(message.content).lower()
            return content == "h" or content == "higher" or content == "l" or content == "lower"

        try:
            option = await self.client.wait_for("message", timeout=30, check=check)

            if option:
                content = str(option.content).lower()

                if (content == "higher" or content == "h") and hidden_number > given_number:
                    await ctx.send(f":partying_face: {ctx.author.mention} You Won! ")
                    return

                if (content == "lower" or content == "l") and hidden_number < given_number:
                    await ctx.send(f":partying_face: {ctx.author.mention} You Won! ")
                    return

                if hidden_number == given_number:
                    await ctx.send("It was a tie")
                    return

                await ctx.send(f"{ctx.author.mention} You lost! :cry: ")
                return

            await ctx.send(f"{ctx.author.mention} please provide a valid option - (higher or lower)")

        except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author.mention} Time Out!")


def setup(client):
    client.add_cog(Commands(client))
