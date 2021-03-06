# discord imports
import discord
from discord import colour
from discord.ext import commands

# other imports
import asyncio
import random
from datetime import datetime
import calendar
from spellchecker import SpellChecker
import img


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # ping command
    @commands.command()
    async def ping(self, ctx):
        """ Gets the latency of the bot """
        async with ctx.channel.typing():
            LatencyEmbed = discord.Embed(
                colour=discord.Colour.light_gray()
            )
            LatencyEmbed.set_author(name=f"Latency - {round(self.client.latency * 1000)}")
            await ctx.send(embed=LatencyEmbed)

    # timer command
    @commands.command()
    async def timer(self, ctx, hour: int, minute: int, second: int):
        """ Sets a timer for <hour> <minute> <second> """
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
        """ Dice roll """
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
        """ Stone paper Scissor game """
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
        """
        Number Guessing game
        First two numbers are selected
        One of those two numbers are given to user
        the user needs to find that the second number is smaller or bigger than the given number
        """
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


    # member count command
    @commands.command(aliases=["mc"])
    async def member_count(self, ctx):
        """ Counts the members in the guild """
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
    async def announcement(self, ctx, topic: str, *, text: str):
        """ Makes a announcement embed for you """
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

    @commands.command()
    async def roman(self, ctx, num: int):
        """ Converts numbers to Roman Numerals """
        if num >= 4000:
            return await ctx.send(f"{ctx.author.mention} please specify a number lower or equal to 3999!")
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        await ctx.send(roman_num)

    @commands.command()
    async def bmi(self, ctx, weight: int, height: int):
        WarningEmbed = discord.Embed(
            colour = discord.Colour.light_gray(),
            description = "Please note that this IS NOT MEDICAL ADVICE, if you are concerned about your health or wellbeing, consult a doctor."
        )
        WarningEmbed.set_author(name = "Warning!", icon_url=img.ImgError)
        
        """
            Finds the BMI index for you
            formula -  weight (kg) / [height (m)] * [height (m)]
            Less than 15 	Very severely underweight
            Between 15 and 16 	Severely underweight
            Between 16 and 18.5 	Underweight
            Between 18.5 and 25 	Normal (healthy weight)
            Between 25 and 30 	Overweight
            Between 30 and 35 	Moderately obese
            Between 35 and 40 	Severely obese
            Over 40 	Very severely obese
        """
        height = height / 100
        bmi = weight / (height * height)

        if bmi < 15:
            return await ctx.send(f"{ctx.author.mention} your BMI index is {bmi} \nYou are Very severely underweight! \nConsult a doctor quickly!", embed = WarningEmbed)

        elif 15 >= bmi < 16:
            return await ctx.send(f"{ctx.author.mention} your BMI index is {bmi} \nYou are Severely underweight! \nGet a change in you diet and daily routine!", embed = WarningEmbed)

        elif 16 >= bmi < 18.5:
            return await ctx.send(f"{ctx.author.mention} your BMI index is {bmi} \nYou are Underweight! \nStart taking out some time for you", embed = WarningEmbed)

        elif 18.5 >= bmi < 25:
            return await ctx.send(f"{ctx.author.mention} your BMI index is {bmi} \nYou are Normal weighted!", embed = WarningEmbed)

        elif 25 >= bmi < 30:
            return await ctx.send(f"{ctx.author.mention} your BMI index is {bmi} \nYou are Overweight \nStart taking out some time for you", embed = WarningEmbed)

        elif 30 >= bmi < 35:
            return await ctx.send(f"{ctx.author.mention} your BMI index is {bmi} \nYou are Moderately obese! \nGet a change in you diet and daily routine!", embed = WarningEmbed)

        elif 35 >= bmi <= 40:
            return await ctx.send(f"{ctx.author.mention} your BMI index is {bmi} \nYou are Severely obese! \nPlease start doing some exercise!", embed = WarningEmbed)

        elif 40 > bmi:
            return await ctx.send(f"{ctx.author.mention} your BMI index is {bmi} \nYou are Very severely obese! \nConsult a doctor quickly!", embed = WarningEmbed)

    @commands.command()
    async def whois(self, ctx, mem: commands.MemberConverter = None):
        member = mem or ctx.author
        created_at = member.created_at
        joined_at = member.joined_at
        roles = member.roles

        embed = discord.Embed(color=discord.Colour.light_grey())
        embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Created", value=f"{calendar.day_name[created_at.weekday()]}, {created_at.day} {calendar.month_name[created_at.month]} {created_at.year} {created_at.hour}:{created_at.minute}", inline=False)
        embed.add_field(name="Joined", value=f"{calendar.day_name[joined_at.weekday()]}, {joined_at.day} {calendar.month_name[joined_at.month]} {joined_at.year} {joined_at.hour}:{joined_at.minute}", inline=False)
        embed.add_field(name=f"Roles [{len(roles)}]", value=" ".join(f"<@&{role.id}>" for role in roles))
        embed.set_footer(text=f"ID - {member.id}")
        await ctx.send(embed=embed)

        print(type(created_at), type(joined_at), roles)


    @commands.command(aliases=["av"])
    async def avatar(self, ctx, mem: commands.MemberConverter = None):
        member = mem or ctx.author
        embed = discord.Embed(color=discord.Colour.lighter_grey())
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_image(url=member.avatar_url)

        await ctx.send(embed=embed)


    @commands.command(aliases = ["spch"])
    async def spellcheck(self, ctx, arg):
        spell = SpellChecker()
        main = spell.correction(arg)
        others = spell.candidates(arg)
        otherstr = ""
        for others in others:
            otherstr = f"{otherstr}{others}, "

        SpellingEmbed = discord.Embed(
            colour = discord.Colour.light_grey()
        )
        SpellingEmbed.set_author(name = f"Spellcheck for: {arg}", icon_url = img.ImgDictionary)
        SpellingEmbed.add_field(name = "Most likely spelling", value = main, inline = False)
        SpellingEmbed.add_field(name = "Other possible corrections", value = otherstr, inline = False)

        await ctx.send(embed = SpellingEmbed)


    @commands.command()
    async def github(self, ctx):
        GithubEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        GithubEmbed.set_author(name = "SchoolBot Github", icon_url = img.ImgMain)
        GithubEmbed.add_field(name = "Contributers", value = "[Matt](https://github.com/mattmoody05), [Exainz](https://github.com/Exainz)", inline = False)
        GithubEmbed.add_field(name = "Text Editors / IDE", value = "Visual Studio Code, Atom by Github, PyCharm", inline = False)
        GithubEmbed.add_field(name = "Database used", value = "PostgreSQL", inline = False)
        GithubEmbed.add_field(name = 'Github Link', value = "[https://github.com/mattmoody05/SchoolBot](https://github.com/mattmoody05/SchoolBot)", inline = False)
        await ctx.send(embed = GithubEmbed)


def setup(client):
    client.add_cog(Commands(client))
