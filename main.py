import os
import math
import random
import logging
import discord
from discord.ext import commands, tasks
from flask import Flask

#KEEPSEYE ON WARNING LEVEL LOGS
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#BOT PREFIX
bot = commands.Bot(command_prefix = "!!")

cogs = ["cogs.genshin_commands.Genshin",
        "cogs.genshin_commands.yelan.Yelan"
       , "cogs.miscellaneous.Miscellaneous"]

@bot.event
#SET PRESENSE AND ACTIVITY
@bot.event
async def on_connect():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Ryxke"))

@bot.event
async def on_ready():
  print("Bot is Online")

  for cog in cogs:
    try:
      bot.load_extension(cog)
      print(cog + " Loaded")

    except Exception as e:
      print(e)
      
@bot.event
async def on_command_error(ctx, error):
   await ctx.send("Not a Valid Command.")

bot.run(os.environ['TOKEN'])