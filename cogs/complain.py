import discord
from discord.ext import commands
import datetime

class Complain(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild and not message.channel.id == self.client.complain_channel:
            return

        attachments = message.attachments

        if not message.guild:
            try:
                if not message.author.id == self.client.user.id:
                    channel = self.client.get_channel(self.client.complain_channel)

                    title, description = str(message.content).split("|")
                    ComplainEmbed = discord.Embed(color=discord.Colour.light_grey(), timestamp=datetime.datetime.utcnow())
                    ComplainEmbed.set_author(name=title, icon_url=message.author.avatar_url)
                    ComplainEmbed.description = description
                    ComplainEmbed.set_footer(text=f"Complain by - {message.author} \nId - {message.author.id}")
                    await channel.send(embed=ComplainEmbed)

                    if attachments:
                        for attachment in attachments:
                            await channel.send(attachment.url)

                    doneEmbed = discord.Embed(color=discord.Colour.lighter_grey(), timestamp=datetime.datetime.utcnow())
                    doneEmbed.set_author(name=f"{message.author} your Complain delivered Successfully!")
                    doneEmbed.description = f"\nThank you for your report! The teachers will be back to you as soon as possible!"
                    doneEmbed.description += f"\nTitle - {title}"
                    doneEmbed.description += f"\nDescription - {description}\n"
                    await message.channel.send(embed=doneEmbed)
            except ValueError:
                if not message.author.id == self.client.user.id:
                    msg = """title | description"""
                    await message.channel.send(f"{message.author.mention} for registering a complain, type \n{msg}")

        try:
            if not message.author == self.client.user.id:
                member_id, msg1 = str(message.content).split("|")
                member = await self.client.fetch_user(int(member_id))

                ResponseEmbed = discord.Embed(color=discord.Colour.lighter_grey(), timestamp=datetime.datetime.utcnow())
                ResponseEmbed.set_author(name=message.author, icon_url=message.author.avatar_url)
                ResponseEmbed.description = msg1
                await member.send(embed=ResponseEmbed)

                if attachments:
                    for attachment in attachments:
                        await member.send(attachment.url)

        except ValueError:
            pass



def setup(client):
    client.add_cog(Complain(client))