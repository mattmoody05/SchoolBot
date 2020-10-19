import discord
from discord.ext import commands
import asyncio


class NotesSharing(commands.Cog):
    def __init__(self, client):
        self.client = client

    def check(self, message):
        try:
            embed = message.embeds[0]
        except:
            return False
        text = str(embed.footer.text)
        if text.startswith("Notes By") == 1 and message.author.id == self.client.user.id:
            return True
        return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild:
            return
        if not message.channel.name.lower().count("note") > 0:
            return
        check = self.check(message)
        if check:
            return

        attachments = message.attachments
        if len(attachments) < 1:
            await message.delete()
            return

        title, description = str(message.content).split("|")

        for attachment in attachments:
            embed = discord.Embed(color=discord.Color.light_grey())
            embed.set_author(name=title, icon_url=message.author.avatar_url)
            embed.description = description
            embed.set_image(url=attachment.url)
            embed.set_footer(text=f"Notes By - {message.author}")
            await message.channel.send(embed=embed)

        await asyncio.sleep(1)
        await message.delete()


def setup(client):
    client.add_cog(NotesSharing(client))
