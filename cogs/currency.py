# discord imports
import discord
from discord.ext import commands

# other imports
from currency_converter import CurrencyConverter
from datetime import datetime


class Currency(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def currency(self, ctx):
        NoCommandEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        NoCommandEmbed.set_author(name = "Please provide a currency command")
        await ctx.send(embed = NoCommandEmbed)


    @currency.command()
    async def convert(self, ctx, arg1, arg2, arg3):
        Converted = str(CurrencyConverter().convert(arg1, arg2, arg3))
        
        CurrencyConvertedEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        CurrencyConvertedEmbed.set_author(name = "Currency Conversion")
        CurrencyConvertedEmbed.add_field(name = "Input Currency", value = arg2)
        CurrencyConvertedEmbed.add_field(name = "Output Currency", value = arg3)
        CurrencyConvertedEmbed.add_field(name = "Output Value", value = f"{str(Converted)} {arg3}")

        await ctx.send(embed = CurrencyConvertedEmbed)


    @currency.command()
    async def value(self, ctx, arg1):
        Value = str(CurrencyConverter().convert(1, arg1, "USD"))
        
        CurrencyValueEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        CurrencyValueEmbed.set_author(name = f"1 {arg1} == {Value} USD")

        await ctx.send(embed = CurrencyValueEmbed)


    @currency.command()
    async def list(self, ctx):
        Currencies = str(CurrencyConverter().currencies).replace("'", "").replace("{", "").replace("}", "")
        
        CurrencyListEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        CurrencyListEmbed.set_author(name = "Currency Conversion List")
        CurrencyListEmbed.add_field(name = "The below currencies are supported by the converter", value = Currencies)
        
        await ctx.send(embed = CurrencyListEmbed)

def setup(client):
    client.add_cog(Currency(client))