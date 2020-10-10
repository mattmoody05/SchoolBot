from discord.ext import commands
import math


class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def math(self, ctx):
        await ctx.send(f"{ctx.author.mention} please specify some task :)")

    @math.command(aliases=["addition", "sum"])
    async def add(self, ctx, *args):
        add = sum(int(i) for i in args)
        await ctx.send(add)

    @math.command()
    async def multiply(self, ctx, *args):
        mul = 1
        for i in map(int, args):
            mul *= i
        await ctx.send(mul)

    @math.command(aliases=["div"])
    async def divide(self, ctx, a: float, b: float):
        divide = a / b
        await ctx.send(divide)

    @math.command(aliases=["pow"])
    async def power(self, ctx, a: float, b: float):
        pow = a ** b
        await ctx.send(pow)

    @math.command(aliases=["root"])
    async def sqrt(self, ctx, a: float):
        sqrt = math.sqrt(a)
        await ctx.send(sqrt)

    @math.command()
    async def sin(self, ctx, a: float):
        sin = math.sin(a)
        await ctx.send(sin)

    @math.command()
    async def cos(self, ctx, a: float):
        cos = math.cos(a)
        await ctx.send(cos)

    @math.command()
    async def tan(self, ctx, a: float):
        tan = math.tan(a)
        await ctx.send(tan)

    @math.command(aliases=["cosecant", "asin"])
    async def cossec(self, ctx, a: float):
        cossec = math.asin(a)
        await ctx.send(cossec)

    @math.command()
    async def sec(self, ctx, a: float):
        sec = math.acos(a)
        await ctx.send(sec)

    @math.command()
    async def cot(self, ctx, a: float):
        cot = math.atan(a)
        await ctx.send(cot)

    @math.command(aliases=["gcd"])
    async def hcf(self, ctx, a: int, b: int):
        gcd = math.gcd(a, b)
        await ctx.send(gcd)

    @math.command()
    async def lcm(self, ctx, a: int, b: int):
        lcm = a * b // math.gcd(a, b)
        await ctx.send(lcm)

    @math.command()
    async def factorial(self, ctx, a: int):
        fact = math.factorial(a)
        await ctx.send(fact)

    @math.command()
    async def gamma(self, ctx, a: float):
        gamma = math.gamma(a)
        await ctx.send(gamma)

    @math.command(aliases=["floor"])
    async def round(self, ctx, a: float):
        floor = round(a)
        await ctx.send(floor)


def setup(client):
    client.add_cog(Math(client))
