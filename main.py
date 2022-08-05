import os
import discord
from discord.ext import commands, tasks
from res.logger import logger

logger.run()

#BOT PREFIX
bot = commands.Bot(command_prefix="!!", intents=discord.Intents.default())
cogs = [
    "cogs.genshin.Genshin", "cogs.miscellaneous.Miscellaneous",
    "cogs.music.Music",
    "cogs.genshin.EnkaShinShin",
    "cogs.genshin.Artifacts"
]

color = 0x06E5F5

#SET PRESENSE AND ACTIVITY
@bot.event
async def on_connect():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="Ryxke"))


@bot.event
async def on_ready():
    print("Bot is Online")

    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(cog + " Loaded")

        except Exception as e:
            print(e)


# @bot.command()
# async def load(ctx):
#     if ctx.author.id == 783221172560855081 or ctx.author.id == 536554334033543183:
#         for cog in cogs:
#             try:
#                 await ctx.message.add_reaction("✅")
#             except Exception as e:
#                 print(e)

#     else:
#         await ctx.message.add_reaction("❎")


# @bot.event
# async def on_command_error(ctx, error):
#    await ctx.send("Not a Valid Command")

bot.run(os.environ['TOKEN'])
