import discord
from discord.ext import tasks, commands
import random

class Miscellaneous(commands.Cog):

  @commands.command(brief = "Github link for the bot", aliases = ['gh', 'git'])
  async def github(self, ctx):
    await ctx.send('https://github.com/Ryxke/shenhe')

  #TO CHECK IF BOT IS WORKING
  @commands.command(brief = "Replies with Pong")
  async def ping(self, ctx):
    latency = round(self.bot.latency*1000)
    await ctx.send("Pong! {}ms".format(latency)) 

  #CALCULATOR
  @commands.command(brief = "It calculates Stuffs")
  async def calc(self, ctx, operation:str):
    await ctx.send(eval(operation))

  #EMOTIONAL DAMAGE
  @commands.command(brief = "EMOTIONAL DAMAGE")
  async def damage(self, ctx):
    await ctx.send("https://c.tenor.com/K9-SqJMNjkEAAAAM/emotional-damage.gif")

  #Coin Flip 
  @commands.command(brief = "Coin Flip")
  async def flip(self, ctx):
    sides = ["Heads", "Tails"]
    await ctx.send(random.choice(sides))

def setup(bot):
  bot.add_cog(Miscellaneous(bot))