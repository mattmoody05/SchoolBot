# imports
from discord.ext import commands
import discord

# help embed
HelpEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
HelpEmbed.set_author(name = "SchoolBot help")
HelpEmbed.add_field(name = "Math", value="*math add* - Adds the numbers given (each seperated by a space)\n*math multiply* - Multiplies the numbers given (each seperated by a space)\n*math divide* - Divides the numbers given (each seperated by a space)\n*math power <a> <b>* - Calculates a to the power of b\n*math sqrt <number>* - Finds the square root of the number entered", inline=False)
HelpEmbed.add_field(name = "Dictionary", value="*define <word>* - Deines the word given\n*synonym <word>* - Returns synonyms for the word given", inline=False)
HelpEmbed.add_field(name = "Moderation", value="*purge <number>* - Deletes the number of messages specified\n*kick @member* - Kicks the metioned member\n*ban @member* - Bans the mentioned member", inline=False)
HelpEmbed.add_field(name = "Wikipedia", value="*wiki summary <query>* - Searches wikipedia for your query, returning a summary of that topic\n*wiki full <query>* - Searches wikipedia for your query and returns the full article", inline=False)
HelpEmbed.add_field(name = "Other", value="*ping* - Returns your latency to bot (in miliseconds)", inline=False)

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        await ctx.send(embed = HelpEmbed)



def setup(client):
    client.add_cog(help(client))