# imports
import discord
from discord.ext import commands

# image urls
import img

# main embed
MainEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
MainEmbed.set_author(name="Schoolbot Help", icon_url=img.ImgMain)
MainEmbed.add_field(name="Help Areas",
                    value="Below are the diffent areas of help you can access\nPlease run ***help <area>*** to get specific help. e.g ***help math***",
                    inline=False)
MainEmbed.add_field(name="Areas of help",
                    value="- math\n- wikipedia\n- dictionary\n- moderation\n- todo\n- youtube\n- time_table\n- Notes Sharing\n- tag\n- translate\n- currency\n- music\n- other",
                    inline=False)

# other embed
OtherEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
OtherEmbed.set_author(name="Schoolbot - Other help", icon_url=img.ImgMain)
OtherEmbed.add_field(name="ping", value="Returns your latency to the bot in ms", inline=False)
OtherEmbed.add_field(name="timer <h> <m> <s>", value="Sets a timer for the amount of time you have provided",
                     inline=False)
OtherEmbed.add_field(name="suggest", value="Makes a yes no poll", inline=False)
OtherEmbed.add_field(name='poll "description" "choice1" "choice2"', value="Makes a poll with multiple choices",
                     inline=False)
OtherEmbed.add_field(name='study_mode', value="Sets a study_mode for you, to help you concentrate on studies",
                     inline=False)
OtherEmbed.add_field(name='source <command>', value="Gives the source of a command", inline=False)
OtherEmbed.add_field(name='password_generate <len of password>',
                     value="Gives a random password of the specified length", inline=False)
OtherEmbed.add_field(name="roll_dice", value="Rolls a dice for you", inline=False)
OtherEmbed.add_field(name="stone_paper_scissor <option>", value="Plays Stone Paper game with you", inline=False)
OtherEmbed.add_field(name="number_guess", value="Game in which you need to guess that a number is higher or lower than the number which is sent", inline=False)
OtherEmbed.add_field(name="announcement <topic> <description>", value="Only for Admins \nMakes a announcement channel is not and sends a message as a Server Announcement", inline=False)
OtherEmbed.add_field(name="roman <number>", value="Converts the number into roman numeral, number should be less than 3999", inline=False)
OtherEmbed.add_field(name="bmi <weight> <height>", value="Tells you your BMI and your current health status according to your BMI", inline=False)

# wiki embed
WikiEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
WikiEmbed.set_author(name="Schoolbot - Wikipedia help", icon_url=img.ImgWikipedia)
WikiEmbed.add_field(name="wiki summary <query>",
                    value="Searches wikipedia for your query, returning a summary of that topic", inline=False)
WikiEmbed.add_field(name="wiki full <query>", value="Searches wikipedia for your query and returns the full article",
                    inline=False)

# dictionary embed
DictEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
DictEmbed.set_author(name="Schoolbot - Dictionary help", icon_url=img.ImgDictionary)
DictEmbed.add_field(name="dict define <word>", value="Defines the word provided", inline=False)
DictEmbed.add_field(name="dict synonym <word>", value="Gives alternative words for the word provided", inline=False)

# moderation embed
ModEmbed = discord.Embed(
    colour=discord.Colour.light_gray(),
    description="Please note that these moderation commands will require the correct permissions"
)
ModEmbed.set_author(name="Schoolbot - Moderation help", icon_url=img.ImgMain)
ModEmbed.add_field(name="kick @member", value="Kicks the mentioned member", inline=False)
ModEmbed.add_field(name="ban @member", value="Bans the mentioned member", inline=False)
ModEmbed.add_field(name="purge <number>", value="Deletes the specified number of messages", inline=False)

# math embed
MathEmbed = discord.Embed(
    colour=discord.Colour.light_gray(),
    description="The names of these commands are self-explanitary, please use common sense to determine what they do."
)
MathEmbed.set_author(name="Schoolbot - Math help", icon_url=img.ImgMath)
MathEmbed.add_field(name="Commands",
                    value="math add\nmath multiply\nmath divide\nmath power\nmath root\nmath sin\nmath cos\nmath tan\nmath cossec\nmath sec\nmath cot\nmath hcf\nmath lcm\nmath factorial\nmath gamma\nmath round\nmath average")

# youtube embed
YTEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
YTEmbed.set_author(name="Schoolbot help - Youtube", icon_url=img.ImgYoutube)
YTEmbed.add_field(name="youtube search <query>", value="Searches youtube and returns info on your query", inline=False)

# time-table embed
TTEmbed = discord.Embed(
    colour=discord.Colour.light_grey())
TTEmbed.set_author(name="Schoolbot help - Time Table", icon_url=img.ImgTimetable)
TTEmbed.add_field(name="time_table insert <Name of the day> <Time in GMT> <Work>",
                  value="Reminds you for for that task in your DM's \n e.g - $time_table insert Monday 03:33 Maths class",
                  inline=False)
TTEmbed.add_field(name="time_table delete <Name of the day> <Time>", value="Deletes the task if it exists",
                  inline=False)
TTEmbed.add_field(name="time_table all", value="Sends all your schedule", inline=False)

# todo
TDEmbed = discord.Embed(
    colour=discord.Colour.light_gray())
TDEmbed.set_author(name="Schoolbot help - Todo", icon_url=img.ImgTodo)
TDEmbed.add_field(name="todo insert <work>", value="Inserts the work in your todo list", inline=False)
TDEmbed.add_field(name="todo delete <work>", value="Deletes the work from your todo list", inline=False)
TDEmbed.add_field(name="todo all", value="Sends your todo list")

# notes sharing
NSEmbed = discord.Embed(colour=discord.Colour.light_grey())
NSEmbed.set_author(name="Schoolbot help - Notes Sharing", icon_url=img.ImgNotes)
NSEmbed.add_field(name="Pasting with - <title> | <description>",
                  value="Just paste the picture and it would be formatted into a well embed \n Note: The picture should be in a proper channel name e.g - #notes-sharing")

# tag
TEmbed = discord.Embed(color=discord.Colour.light_grey())
TEmbed.set_author(name="Schoolbot help - Tag", icon_url=img.ImgTag)
TEmbed.add_field(name="tag create <name> <content>", value="Creates a tag with that name and content", inline=False)
TEmbed.add_field(name="tag edit <name> <content>", value="Edits the tag with that name if you own that", inline=False)
TEmbed.add_field(name="tag rename <old name> <new name>", value="Renames the tag with that name if you own it",
                 inline=False)
TEmbed.add_field(name="tag delete <name>", value="Deletes the tag with that name if you own it", inline=False)
TEmbed.add_field(name="tag info <name>", value="Gives the info of a tag with that name", inline=False)
TEmbed.add_field(name="tag list <member>", value="Lists all the tags of that member", inline=False)
TEmbed.add_field(name="tag all", value="DM's all the tags", inline=False)

# translate
TSEmbed = discord.Embed(color=discord.Colour.light_grey())
TSEmbed.set_author(name="Schoolbot help - Translator", icon_url=img.ImgTranslate)
TSEmbed.add_field(name="translate <language unicode> <text>",
                  value="Translate the text in the language provided by you", inline=False)
TSEmbed.add_field(name="translate detect <text>", value="Detects the language of the text that you have entered",
                  inline=False)
TSEmbed.add_field(name="translate all", value="Gives all the unicode of all the languages supported", inline=False)

# currency embed
CurrencyEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
CurrencyEmbed.set_author(name="Schoolbot help - Currency", icon_url=img.ImgCurrency)
CurrencyEmbed.add_field(name="currency convert <amount> <input currency> <output currency>",
                        value="Converts the amount specified from the input currency specified to the output currency specified",
                        inline=False)
CurrencyEmbed.add_field(name="currency value <currency>", value="Show the value of the input currency in USD",
                        inline=False)
CurrencyEmbed.add_field(name="currency list", value="Shows a list of all the currencies supported by the converter",
                        inline=False)

# music embed
MusicEmbed = discord.Embed(color=discord.Color.light_grey())
MusicEmbed.set_author(name="Schoolbot help - Music", icon_url=img.ImgMusic)
MusicEmbed.add_field(name="music play <query/Youtube url to video or playlist>",
                     value="Plays the song according to the given query/url", inline=False)
MusicEmbed.add_field(name="music disconnect", value="Disconnects the bot from the VoiceChannel", inline=False)
MusicEmbed.add_field(name="music pause", value="Pauses the song", inline=False)
MusicEmbed.add_field(name="music resume", value="Resumes the song", inline=False)
MusicEmbed.add_field(name="music volume <amount>", value="Sets the volume of the player, it should be below 1000",
                     inline=False)
MusicEmbed.add_field(name="music skip", value="Skips the current song", inline=False)
MusicEmbed.add_field(name="music current", value="Shows the song which is currently playing", inline=False)
MusicEmbed.add_field(name="music queue", value="Shows total queue of the songs", inline=False)


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        """ Sends the help embed """
        await ctx.send(embed=MainEmbed)

    @help.command()
    async def math(self, ctx):
        """ Sends the math help embed """
        await ctx.send(embed=MathEmbed)

    @help.command()
    async def other(self, ctx):
        """ Sends the other help embed """
        await ctx.send(embed=OtherEmbed)

    @help.command(aliases=["wikipedia"])
    async def wiki(self, ctx):
        """ Sends the wiki help embed """
        await ctx.send(embed=WikiEmbed)

    @help.command(aliases=["dict"])
    async def dictionary(self, ctx):
        """ Sends the dictionary help embed """
        await ctx.send(embed=DictEmbed)

    @help.command(aliases=["mod"])
    async def moderation(self, ctx):
        """ Sends the moderation help embed """
        await ctx.send(embed=ModEmbed)

    @help.command(aliases=["yt"])
    async def youtube(self, ctx):
        """ Sends the youtube help embed """
        await ctx.send(embed=YTEmbed)

    @help.command(aliases=["tt"])
    async def time_table(self, ctx):
        """ Sends the timetable help embed """
        await ctx.send(embed=TTEmbed)

    @help.command(aliases=["td"])
    async def todo(self, ctx):
        """ Sends the todo help embed """
        await ctx.send(embed=TDEmbed)

    @help.command(aliases=["ns"])
    async def notes_sharing(self, ctx):
        """ Sends the notes_sharing help embed """
        await ctx.send(embed=NSEmbed)

    @help.command()
    async def tag(self, ctx):
        """ Sends the tag help embed """
        await ctx.send(embed=TEmbed)

    @help.command()
    async def translate(self, ctx):
        """ Sends the translate help embed """
        await ctx.send(embed=TSEmbed)

    @help.command()
    async def currency(self, ctx):
        """ Sends the currency help embed """
        await ctx.send(embed=CurrencyEmbed)

    @help.command()
    async def music(self, ctx):
        """ Sends the music help embed """
        await ctx.send(embed=MusicEmbed)


def setup(client):
    client.add_cog(Help(client))
