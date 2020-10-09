# imports
import discord
from discord.ext import commands
import json
import time
import os

# opening config.json file
with open('./config.json') as x:
    data = json.load(x)

# getting token and prefix from config file
BOTPREFIX = data['prefix']
BOTTOKEN = data['token']

# declaring the client object
client = commands.Bot(command_prefix = BOTPREFIX)

# removing the default help command so that a better one can be made using embeds
client.remove_command("help")

# changing the bot's status to "Listening to $help" and printing that the bot has logged in without any issues
@client.event
async def on_ready():
    ListeningTo = discord.Activity(type=discord.ActivityType.listening, name="$help")
    await client.change_presence(status=discord.Status.online, activity=ListeningTo)
    print('We have logged in as {0.user}'.format(client))

# automatically loading all cogs when started
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')
        print("Loaded cog: {0}".format(filename))

# command to reload cogs if not working properly
@client.command()
async def reload(ctx):
    await ctx.send("***Reloading cogs...***")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.unload_extension(f'cogs.{filename[:-3]}')
            await ctx.send("Unloaded cog: {0}".format(filename))
            time.sleep(1)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f'cogs.{filename[:-3]}')
            await ctx.send("Loaded cog: {0}".format(filename))
            time.sleep(1)

client.run(BOTTOKEN)