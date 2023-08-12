import os
import discord
from discord.ext import commands, tasks
from res.logger import logger

logger.run()

#BOT PREFIX
intents = discord.Intents().default()
intents.message_content = True

bot = commands.Bot(command_prefix="!!", intents=intents)
cogs = [
    "cogs.genshin.Genshin", 
    "cogs.miscellaneous.Miscellaneous",
    "cogs.genshin.Artifacts",
    "cogs.genshin.EnkaShinShin",
    "cogs.changelogs", 
    "cogs.genshin.GenshinDetails"
]

color = 0x06E5F5

#SET PRESENSE AND ACTIVITY
# @bot.event
# async def on_connect():
#     await bot.change_presence(activity=discord.Activity(
#         type=discord.ActivityType.listening, name="Ryxke"))


@bot.event
async def on_ready():
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(cog + " Loaded")

        except Exception as e:
            print(e)

    print("Bot is Online")



# @bot.event
# async def on_command_error(ctx, error):
#     print(error)
#     embed = discord.Embed(title = error, description = "", color = color)
#     await ctx.send(embed = embed)

bot.run(os.environ['TOKEN'])
