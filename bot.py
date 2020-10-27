# imports
import json
import os
from cogs.DataBase.client import DataBase
import img

# discord imports
import discord
from discord.ext import commands

# functions
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour = discord.Colour.light_gray()
    )
    Embed.set_author(name = author, icon_url = img.ImgMain)
    return Embed


# opening config.json file
with open('./config.json') as x:
    data = json.load(x)

# getting token and prefix from config file
BOTPREFIX = data['prefix']
BOTTOKEN = data['token']

# declaring the client object
client = commands.AutoShardedBot(command_prefix=BOTPREFIX, intents=discord.Intents.all())

client.info = {
    "host": data["host"],
    "database": data["database"],
    "user": data["user"],
    "port": data["port"],
    "password": data["password"],
    "max_size": data["max_size"],
    "min_size": data["min_size"]
}
client.complain_channel = data["complain_channel"]

# removing the default help command so that a better one can be made using embeds
client.remove_command("help")


@client.event
async def on_connect():
    client.db = await DataBase.create_pool(client=client, info=client.info)


# changing the bot's status to "Listening to $help" and printing that the bot has logged in without any issues
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{BOTPREFIX}help"))

    print("\nLoading cogs...\n")

    # automatically loading all cogs when started
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f'cogs.{filename[:-3]}')
            print("Loaded cog: {0}".format(filename))

    # showing the user that the bot has logged in successfully and with what bot user
    print(f'\nLogged in as {client.user}\n')


# command to reload cogs if not working properly
@commands.has_guild_permissions(administrator=True)
@client.command()
async def reload(ctx):
    NoOfCogs = 0
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.unload_extension(f'cogs.{filename[:-3]}')
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f'cogs.{filename[:-3]}')
            NoOfCogs = NoOfCogs + 1
    await ctx.send(embed = SimpleEmbed(f"{str(NoOfCogs)} cogs have been reloaded"), delete_after = 10)


client.run(BOTTOKEN)
