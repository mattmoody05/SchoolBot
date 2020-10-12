# imports
from discord.ext import commands
import discord


# main embed
MainEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
MainEmbed.set_author(name = "Schoolbot Help")
MainEmbed.add_field(name = "Help Areas", value = "Below are the diffent areas of help you can access\nPlease run ***help <area>*** to get specific help. e.g ***help math***", inline = False)
MainEmbed.add_field(name = "Areas of help", value="- math\n- wikipedia\n- dictionary\n- moderation\n- youtube\n- other")


# other embed
OtherEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
OtherEmbed.set_author(name = "Schoolbot - Other help")
OtherEmbed.add_field(name = "ping", value = "Returns your latency to the bot in ms")
OtherEmbed.add_field(name = "timer <h> <m> <s>", value = "Sets a timer for the amount of time you have provided")


# wiki embed
WikiEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
WikiEmbed.set_author(name = "Schoolbot - Wikipedia help")
WikiEmbed.add_field(name = "wiki summary <query>", value = "Searches wikipedia for your query, returning a summary of that topic")
WikiEmbed.add_field(name = "wiki full <query>", value = "Searches wikipedia for your query and returns the full article")


# dictionary embed
DictEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
DictEmbed.set_author(name = "Schoolbot - Dictionary help")
DictEmbed.add_field(name = "dict define <word>", value="Defines the word provided")
DictEmbed.add_field(name = "dict synonym <word>", value="Gives alternative words for the word provided")


# moderation embed
ModEmbed = discord.Embed(
    colour = discord.Colour.light_gray(),
    description = "Please note that these moderation commands will require the correct permissions"
)
ModEmbed.set_author(name = "Schoolbot - Moderation help")
ModEmbed.add_field(name = "kick @member", value = "Kicks the mentioned member")
ModEmbed.add_field(name = "ban @member", value = "Bans the mentioned member")
ModEmbed.add_field(name = "purge <number>", value = "Deletes the specified number of messages")


# math embed
MathEmbed = discord.Embed(
    colour = discord.Colour.light_gray(),
    description = "The names of these commands are self-explanitary, please use common sense to determine what they do."
)
MathEmbed.set_author(name = "Schoolbot - Math help")
MathEmbed.add_field(name = "Commands", value = "math add\nmath multiply\nmath divide\nmath power\nmath root\nmath sin\nmath cos\nmath tan\nmath cossec\nmath sec\nmath cot\nmath hcf\nmath lcm\nmath factorial\nmath gamma\nmath round")


# youtube embed
YTEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
YTEmbed.set_author(name = "Schoolbot help - Youtube")
YTEmbed.add_field(name = "youtube search <query>", value = "Searches youtube and returns info on your query", inline=False)
YTEmbed.add_field(name = "youtube mp3 <url>", value = "Converts the youtube video, that is linked to the url provided, into an MP3 file", inline=False)
YTEmbed.add_field(name = "youtube video <url>", value = "Outputs a download link for the youtube video url provided", inline=False)


class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        await ctx.send(embed = MainEmbed)

    @help.command()
    async def math(self, ctx):
        await ctx.send(embed = MathEmbed)

    @help.command()
    async def other(self, ctx):
        await ctx.send(embed = OtherEmbed)

    @help.command(aliases=["wikipedia"])
    async def wiki(self, ctx):
        await ctx.send(embed = WikiEmbed)

    @help.command()
    async def dictionary(self, ctx):
        await ctx.send(embed = DictEmbed)

    @help.command()
    async def moderation(self, ctx):
        await ctx.send(embed = ModEmbed)

    @help.command(aliases = ["yt"])
    async def youtube(self, ctx):
        await ctx.send(embed = YTEmbed)



def setup(client):
    client.add_cog(help(client))