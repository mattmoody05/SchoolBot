# function to get an embed
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour = discord.Colour.light_gray()
    )
    Embed.set_author(name = "Answer: " + str(author))
    return Embed

# discord imports
from discord.ext import commands
import discord

# other imports 
import math




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
        add = sum(int(i) for i in args)
        await ctx.send(embed = SimpleEmbed(add))

    @math.command()
    async def multiply(self, ctx, *args):
        mul = 1
        for i in map(int, args):
            mul *= i
        await ctx.send(embed = SimpleEmbed(mul))

    @math.command(aliases=["div"])
    async def divide(self, ctx, a: float, b: float):
        divide = a / b
        await ctx.send(embed = SimpleEmbed(divide))

    @math.command(aliases=["pow"])
    async def power(self, ctx, a: float, b: float):
        pow = a ** b
        await ctx.send(embed = SimpleEmbed(pow))

    @math.command(aliases=["root"])
    async def sqrt(self, ctx, a: float):
        sqrt = math.sqrt(a)
        await ctx.send(embed = SimpleEmbed(sqrt))

    @math.command()
    async def sin(self, ctx, a: float):
        sin = math.sin(a)
        await ctx.send(embed = SimpleEmbed(sin))

    @math.command()
    async def cos(self, ctx, a: float):
        cos = math.cos(a)
        await ctx.send(embed = SimpleEmbed(cos))

    @math.command()
    async def tan(self, ctx, a: float):
        tan = math.tan(a)
        await ctx.send(embed = SimpleEmbed(tan))

    @math.command(aliases=["cosecant", "asin"])
    async def cossec(self, ctx, a: float):
        cossec = math.asin(a)
        await ctx.send(embed = SimpleEmbed(cossec))

    @math.command()
    async def sec(self, ctx, a: float):
        sec = math.acos(a)
        await ctx.send(embed = SimpleEmbed(sec))

    @math.command()
    async def cot(self, ctx, a: float):
        cot = math.atan(a)
        await ctx.send(embed = SimpleEmbed(cot))

    @math.command(aliases=["gcd"])
    async def hcf(self, ctx, a: int, b: int):
        gcd = math.gcd(a, b)
        await ctx.send(embed = SimpleEmbed(gcd))

    @math.command()
    async def lcm(self, ctx, a: int, b: int):
        lcm = a * b // math.gcd(a, b)
        await ctx.send(embed = SimpleEmbed(lcm))

    @math.command()
    async def factorial(self, ctx, a: int):
        fact = math.factorial(a)
        await ctx.send(embed = SimpleEmbed(fact))

    @math.command()
    async def gamma(self, ctx, a: float):
        gamma = math.gamma(a)
        await ctx.send(embed = SimpleEmbed(gamma))

    @math.command(aliases=["floor"])
    async def round(self, ctx, a: float):
        floor = round(a)
        await ctx.send(embed = SimpleEmbed(floor))

    @math.command(aliases=["mean"])
    async def average(self, ctx, *numbers):
        add = sum(i for i in map(int, numbers))
        total = len(numbers)
        await ctx.send(embed = SimpleEmbed(add/total))


def setup(client):
    client.add_cog(Math(client))
