# discord imports
import discord
from discord.ext import commands

# other imports
import string
import random
import img

# embeds
PrivacyEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
PrivacyEmbed.set_author(name = "Password Privacy", icon_url=img.ImgPassword)
PrivacyEmbed.add_field(name = "How we generate passwords?", value = "We generate the passwords by picking random numbers, letters and symbols and then combining them into a password.", inline = False)
PrivacyEmbed.add_field(name = "Do you store passwords?", value = "No, we will never store your password. The password will only be sent to you and once it has been generated and sent, the only person who can access you password is you.", inline = False)
PrivacyEmbed.add_field(name = "Can I check the source code?", value = "Yes! The source code can be viewed by running `$source password_generate`", inline = False)


class Password(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pg"])
    async def password_generate(self, ctx, password_len: int):
        """ Generates a random password and is directly sent to you! """
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
                await ctx.author.send(embed = PrivacyEmbed)
                await ctx.author.send(f"```{password}```")
            except discord.Forbidden:
                DMErrorEmbed = discord.Embed(
                    colour = discord.Colour.light_grey()
                )
                DMErrorEmbed.set_author("We cannot DM you, please check your privacy settings", icon_url=img.ImgPassword)
                await ctx.send(embed = DMErrorEmbed)


def setup(client):
    client.add_cog(Password(client))
