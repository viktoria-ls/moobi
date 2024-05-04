import discord
from discord.ext import commands
from dotenv import dotenv_values
import my_db

config = dotenv_values(".env")

intents = discord.Intents.default()
intents.message_content = True

# TODO: Convert to use slash commands
# Refer to: https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#hybrid-commands

bot = commands.Bot(command_prefix='$', intents=intents)

# TODO: Yassify bot responses

@bot.command()
async def all(ctx):
    print("[CMD] Get all media.")

    media = my_db.readAllMedia()
    strVal = ""

    for m in media:
        strVal = strVal +  str(m) + "\n"

    await ctx.send(strVal)

# TODO: Command to get a random media by movie/series/all
@bot.command()
async def random(ctx, category="all"):
    pass

# TODO: Command to add new media; sets status to not started
@bot.command()
async def addNew(ctx, title):
    pass

# TODO: Command to mark media as currently watching; sets status to in progress
@bot.command()
async def watch(ctx):
    pass

# TODO: Command to mark media as watched; sets status to finished
@bot.command()
async def finish(ctx, title):
    pass

# TODO: Command to add media to queue; also add new media if doesn't exist
@bot.command()
async def addToQueue(ctx, title):
    pass

# TODO: Command to dequeue whatevers on the queue by "skipping" it
@bot.command()
async def skip(ctx):
    pass

# TODO: Command to mark episode to be watched
@bot.command()
async def bookmarkEp(ctx, title, epNum):
    pass

# TODO: Command to get the current episode of a series
@bot.command()
async def whatEp(ctx, title):
    pass

bot.run(config["TOKEN"])