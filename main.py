import os
import discord
from discord.ext import commands, tasks
from res.logger import logger

logger.run()

#BOT PREFIX
bot = commands.Bot(command_prefix = "!!",
                  intents = discord.Intents.default())
cogs = ["cogs.genshin.Genshin",
        "cogs.miscellaneous.Miscellaneous",
        "cogs.music.Music",
        "cogs.genshin.EnkaShinShin"]

spareCogs = ["cogs.genshin.yelan.Yelan", 
             "cogs.genshin.status"]

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
      
# @bot.event
# async def on_command_error(ctx, error):
#    await ctx.send("Not a Valid Command")


bot.run(os.environ['TOKEN'])