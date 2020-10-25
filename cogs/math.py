# discord imports
from discord.ext import commands
import discord

# other imports 
import math
import img

# function to get an embed quickly
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour = discord.Colour.light_gray()
    )
    Embed.set_author(name = f"Answer: {str(author)}", icon_url=img.ImgMath)
    return Embed


class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def math(self, ctx):
        TaskErrorEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        TaskErrorEmbed.set_author(name = "Please specify a math task!")
        await ctx.send(embed = TaskErrorEmbed)

    @math.command(aliases=["addition", "sum"])
    async def add(self, ctx, *args):
        """ Adds n numbers """
        add = sum(int(i) for i in args)
        await ctx.send(embed = SimpleEmbed(add))

    @math.command()
    async def multiply(self, ctx, *args):
        """ Multiplies n numbers """
        mul = 1
        for i in map(int, args):
            mul *= i
        await ctx.send(embed = SimpleEmbed(mul))

    @math.command(aliases=["div"])
    async def divide(self, ctx, a: float, b: float):
        """ Divides two number """
        divide = a / b
        await ctx.send(embed = SimpleEmbed(divide))

    @math.command(aliases=["pow"])
    async def power(self, ctx, a: float, b: float):
        """ Gives the answer of n^m """
        pow = a ** b
        await ctx.send(embed = SimpleEmbed(pow))

    @math.command(aliases=["root"])
    async def sqrt(self, ctx, a: float):
        """ Gives the square root of a number """
        sqrt = math.sqrt(a)
        await ctx.send(embed = SimpleEmbed(sqrt))

    @math.command()
    async def sin(self, ctx, a: float):
        """ Gives the sin of a number """
        sin = math.sin(a)
        await ctx.send(embed = SimpleEmbed(sin))

    @math.command()
    async def cos(self, ctx, a: float):
        """ Gives the cos of a number """
        cos = math.cos(a)
        await ctx.send(embed = SimpleEmbed(cos))

    @math.command()
    async def tan(self, ctx, a: float):
        """ Gives the tan of a number """
        tan = math.tan(a)
        await ctx.send(embed = SimpleEmbed(tan))

    @math.command(aliases=["cosecant", "asin"])
    async def cossec(self, ctx, a: float):
        """ Gives the cossec/asin of a number """
        cossec = math.asin(a)
        await ctx.send(embed = SimpleEmbed(cossec))

    @math.command()
    async def sec(self, ctx, a: float):
        """ Gives the sec/acos of a number """
        sec = math.acos(a)
        await ctx.send(embed = SimpleEmbed(sec))

    @math.command()
    async def cot(self, ctx, a: float):
        """ Gives the cot/atan of a number """
        cot = math.atan(a)
        await ctx.send(embed = SimpleEmbed(cot))

    @math.command(aliases=["gcd"])
    async def hcf(self, ctx, a: int, b: int):
        """ Gives the hcf/gcd of two numbers """
        gcd = math.gcd(a, b)
        await ctx.send(embed = SimpleEmbed(gcd))

    @math.command()
    async def lcm(self, ctx, a: int, b: int):
        """ Gives the lcm of two numbers """
        lcm = a * b // math.gcd(a, b)
        await ctx.send(embed = SimpleEmbed(lcm))

    @math.command()
    async def factorial(self, ctx, a: int):
        """ Gives the factorial of a number """
        fact = math.factorial(a)
        await ctx.send(embed = SimpleEmbed(fact))

    @math.command()
    async def gamma(self, ctx, a: float):
        """ Gives the gamma of a number """
        gamma = math.gamma(a)
        await ctx.send(embed = SimpleEmbed(gamma))

    @math.command(aliases=["floor"])
    async def round(self, ctx, a: float):
        """ Rounds a number """
        floor = round(a)
        await ctx.send(embed = SimpleEmbed(floor))

    @math.command(aliases=["mean"])
    async def average(self, ctx, *numbers):
        """ Gives the average of n numbers """
        add = sum(i for i in map(int, numbers))
        total = len(numbers)
        await ctx.send(embed = SimpleEmbed(add/total))


def setup(client):
    client.add_cog(Math(client))
