from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def math(self, ctx):
        await ctx.send(f"{ctx.author.mention} please specify some task :)")

    @math.command()
    async def add(self, ctx, *args):
        add = sum(int(i) for i in args)
        await ctx.send(add)

    @math.command()
    async def multiply(self, ctx, *args):
        mul = 1
        for i in map(int, args):
            mul *= i
        await ctx.send(mul)


def setup(client):
    client.add_cog(Math(client))
