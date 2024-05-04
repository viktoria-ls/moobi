# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from dotenv import dotenv_values
import my_db

config = dotenv_values(".env")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def all(ctx):
    print("[CMD] Get all media.")

    media = my_db.readAllMedia()
    strVal = ""

    for m in media:
        strVal = strVal +  str(m) + "\n"

    await ctx.send(strVal)


bot.run(config["TOKEN"])