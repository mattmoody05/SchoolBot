# discord imports
import discord
from discord.ext import commands

# functions
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour = discord.Colour.light_gray()
    )
    Embed.set_author(name = author)
    return Embed


class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.numbers = {
            1: '1️⃣',
            2: '2️⃣',
            3: '3️⃣',
            4: '4️⃣',
            5: '5️⃣',
            6: '6️⃣',
            7: '7️⃣',
            8: '8️⃣',
            9: '9️⃣',
            10: '🔟'}
        self.thumbs = ("👍", "👎")

    @commands.command()
    async def suggest(self, ctx, *, text: str):
        async with ctx.channel.typing():
            await ctx.message.delete()
            suggest_embed = discord.Embed(
                color=discord.Colour.light_grey()
            )
            suggest_embed.set_author(name=f"Poll by {ctx.author}", icon_url=ctx.author.avatar_url)
            suggest_embed.description = text
            message = await ctx.send(embed=suggest_embed)
            await message.add_reaction("👍")
            await message.add_reaction("👎")

    @commands.command()
    async def poll(self, ctx, text: str, *options):
        async with ctx.channel.typing():
            numbers = self.numbers
            if len(options) < 2:
                await ctx.message.delete()
                await ctx.send(ctx.author.mention, delete_after=10)
                await ctx.send(embed = SimpleEmbed("Please provide 2 or more options for the poll"), delete_after=10)
                return
            if len(options) > 10:
                await ctx.message.delete()
                await ctx.send(ctx.author.mention, delete_after=10)
                await ctx.send(SimpleEmbed("You cant make a poll with more than 10 options"), delete_after=10)
                return
            poll_embed = discord.Embed(
                color=discord.Colour.light_grey()
            )
            poll_embed.title = text

            description = """"""
            for option in range(len(options)):
                description += f"\n{numbers[option + 1]} {options[option]}\n"

            poll_embed.description = description

            poll_embed.set_footer(text=f"Poll by - {ctx.author}")
            msg = await ctx.send(embed=poll_embed)

            for option in range(len(options)):
                await msg.add_reaction(numbers[option + 1])

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.client.user.id:
            return
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        poll_checking = self.poll_check(message)

        if poll_checking:
            if str(payload.emoji) not in list(self.numbers.values()):
                user = self.client.get_user(payload.user_id)
                await message.remove_reaction(payload.emoji, user)
                return

            reaction_poll_checking = message.reactions
            member = self.client.get_user(payload.user_id)

            for reaction in reaction_poll_checking:
                async for user in reaction.users():
                    if str(user) == str(member) and str(payload.emoji) != str(reaction.emoji):
                        await message.remove_reaction(payload.emoji, member)
            return

        suggest_checking = self.suggest_check(message)

        if suggest_checking:
            if str(payload.emoji) not in self.thumbs:
                user = self.client.get_user(payload.user_id)
                await message.remove_reaction(payload.emoji, user)

            reactions_suggest_checking = message.reactions
            member = self.client.get_user(payload.user_id)

            for reaction in reactions_suggest_checking:
                async for user in reaction.users():
                    if str(user) == str(member) and str(payload.emoji) != str(reaction.emoji):
                        await message.remove_reaction(payload.emoji, member)

    def poll_check(self, message):
        try:
            embed = message.embeds[0]
        except:
            return False
        text = str(embed.footer.text)
        if text.startswith("Poll by") == 1 and message.author.id == self.client.user.id:
            return True
        return False

    def suggest_check(self, message):
        try:
            embed = message.embeds[0]
        except:
            return False
        text = str(embed.author.name)
        if text.startswith("Poll by") == 1 and message.author.id == self.client.user.id:
            return True
        return False


def setup(client):
    client.add_cog(Poll(client))
