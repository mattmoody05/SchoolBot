# imports
from discord.ext import commands
import discord

# main embed
MainEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
MainEmbed.set_author(name="Schoolbot Help")
MainEmbed.add_field(name="Help Areas",
                    value="Below are the diffent areas of help you can access\nPlease run ***help <area>*** to get specific help. e.g ***help math***",
                    inline=False)
MainEmbed.add_field(name="Areas of help", value="- math\n- wikipedia\n- dictionary\n- moderation\n- todo\n- youtube\n- time_table\n- Notes Sharing\n- other", inline=False)

# other embed
OtherEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
OtherEmbed.set_author(name="Schoolbot - Other help")
OtherEmbed.add_field(name="ping", value="Returns your latency to the bot in ms", inline=False)
OtherEmbed.add_field(name="timer <h> <m> <s>", value="Sets a timer for the amount of time you have provided", inline=False)
OtherEmbed.add_field(name="suggest", value="Makes a yes no poll", inline=False)
OtherEmbed.add_field(name='poll "description" "choice1" "choice2"', value="Makes a poll with multiple choices", inline=False)
OtherEmbed.add_field(name='study_mode', value="Sets a study_mode for you, to help you concentrate on studies", inline=False)
OtherEmbed.add_field(name='source <command>', value="Gives the source of a command", inline=False)

# wiki embed
WikiEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
WikiEmbed.set_author(name="Schoolbot - Wikipedia help")
WikiEmbed.add_field(name="wiki summary <query>",
                    value="Searches wikipedia for your query, returning a summary of that topic", inline=False)
WikiEmbed.add_field(name="wiki full <query>", value="Searches wikipedia for your query and returns the full article", inline=False)

# dictionary embed
DictEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
DictEmbed.set_author(name="Schoolbot - Dictionary help")
DictEmbed.add_field(name="dict define <word>", value="Defines the word provided", inline=False)
DictEmbed.add_field(name="dict synonym <word>", value="Gives alternative words for the word provided", inline=False)

# moderation embed
ModEmbed = discord.Embed(
    colour=discord.Colour.light_gray(),
    description="Please note that these moderation commands will require the correct permissions"
)
ModEmbed.set_author(name="Schoolbot - Moderation help")
ModEmbed.add_field(name="kick @member", value="Kicks the mentioned member", inline=False)
ModEmbed.add_field(name="ban @member", value="Bans the mentioned member", inline=False)
ModEmbed.add_field(name="purge <number>", value="Deletes the specified number of messages", inline=False)

# math embed
MathEmbed = discord.Embed(
    colour=discord.Colour.light_gray(),
    description="The names of these commands are self-explanitary, please use common sense to determine what they do."
)
MathEmbed.set_author(name="Schoolbot - Math help")
MathEmbed.add_field(name="Commands",
                    value="math add\nmath multiply\nmath divide\nmath power\nmath root\nmath sin\nmath cos\nmath tan\nmath cossec\nmath sec\nmath cot\nmath hcf\nmath lcm\nmath factorial\nmath gamma\nmath round\nmath average")

# youtube embed
YTEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
YTEmbed.set_author(name="Schoolbot help - Youtube")
YTEmbed.add_field(name="youtube search <query>", value="Searches youtube and returns info on your query", inline=False)

# time-table embed
TTEmbed = discord.Embed(
    colour=discord.Colour.light_grey())
TTEmbed.set_author(name="Schoolbot help - Time Table")
TTEmbed.add_field(name="time_table insert <Name of the day> <Time in GMT> <Work>", value="Reminds you for for that task in your DM's \n e.g - $time_table insert Monday 03:33 Maths class", inline=False)
TTEmbed.add_field(name="time_table delete <Name of the day> <Time>", value="Deletes the task if it exists", inline=False)
TTEmbed.add_field(name="time_table all", value="Sends all your schedule", inline=False)

# todo
TDEmbed = discord.Embed(
    colour=discord.Colour.light_gray())
TDEmbed.set_author(name="Schoolbot help - Todo")
TDEmbed.add_field(name="todo insert <work>", value="Inserts the work in your todo list", inline=False)
TDEmbed.add_field(name="todo delete <work>", value="Deletes the work from your todo list", inline=False)
TDEmbed.add_field(name="todo all", value="Sends your todo list")

# notes sharing
NSEmbed = discord.Embed(colour=discord.Colour.light_grey())
NSEmbed.set_author(name="Schoolbot help - Notes Sharing")
NSEmbed.add_field(name="Pasting with - <title> | <description>", value="Just paste the picture and it would be formatted into a well embed \n Note: The picture should be in a proper channel name e.g - #notes-sharing")


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        await ctx.send(embed=MainEmbed)

    @help.command()
    async def math(self, ctx):
        await ctx.send(embed=MathEmbed)

    @help.command()
    async def other(self, ctx):
        await ctx.send(embed=OtherEmbed)

    @help.command(aliases=["wikipedia"])
    async def wiki(self, ctx):
        await ctx.send(embed=WikiEmbed)

    @help.command(aliases=["dict"])
    async def dictionary(self, ctx):
        await ctx.send(embed=DictEmbed)

    @help.command(aliases=["mod"])
    async def moderation(self, ctx):
        await ctx.send(embed=ModEmbed)

    @help.command(aliases=["yt"])
    async def youtube(self, ctx):
        await ctx.send(embed=YTEmbed)

    @help.command(aliases=["tt"])
    async def time_table(self, ctx):
        await ctx.send(embed=TTEmbed)

    @help.command(aliases=["td"])
    async def todo(self, ctx):
        await ctx.send(embed=TDEmbed)

    @help.command(aliases=["ns"])
    async def notes_sharing(self, ctx):
        await ctx.send(embed=NSEmbed)


def setup(client):
    client.add_cog(Help(client))
