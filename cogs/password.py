import discord
from discord.ext import commands
import string
import random


class Password(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pg"])
    async def password_generate(self, ctx, password_len: int):
        async with ctx.channel.typing():
            if password_len >= 1995:
                await ctx.send(f"{ctx.author.mention} cant DM a password of that length, please specify a len lower than 1995")
                return
            upper_case = list(string.ascii_uppercase)
            lower_case = list(string.ascii_lowercase)
            numbers = list(string.digits)
            special_characters = list(string.punctuation)
            mega_list = []
            mega_list.extend(upper_case)
            mega_list.extend(lower_case)
            mega_list.extend(numbers)
            mega_list.extend(special_characters)
            mega_list.remove("`")
            random.shuffle(mega_list)

            password = "".join(random.choice(mega_list)for char in range(password_len))

            try:
                await ctx.author.send(f"```{password}```")
            except discord.Forbidden:
                await ctx.send(f"Cant DM you")


def setup(client):
    client.add_cog(Password(client))
