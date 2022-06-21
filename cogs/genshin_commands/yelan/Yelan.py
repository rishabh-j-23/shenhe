import discord
from discord.ext import commands, tasks

class Yelan(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  #YELAN COMMANDS
  @commands.command(brief="Commands related to Yelan")
  async def yelan(self, ctx):
    yelan = "Hydro Bow (5*)"
    await self, ctx.send(yelan)

  @commands.command()
  async def model(ctx):
    await  ctx.send("https://cdn.discordapp.com/attachments/943505502682382406/943505548001816626/yelan.jpeg")
    await ctx.send("https://media.discordapp.net/attachments/943505502682382406/944786784770998302/dtbzabgkfvi81.jpg")
  
  @commands.command(brief = "Yelan Splash Art")
  async def splashart(ctx):
    await ctx.send("https://media.discordapp.net/attachments/943505502682382406/963650336164311051/unknown-1.png")

  @commands.command(brief = "Confirmed")
  async def kit(ctx):
    await ctx.send("https://genshin.honeyhunterworld.com/db/char/yelan/?lang=EN")

  @commands.command()
  async def mats(ctx):
    img = "https://media.discordapp.net/attachments/943505502682382406/958735635399704576/FPGhBTyVIAEfYlb.jpg"
    await ctx.send(img)

  @commands.command()
  async def gameplay (ctx):
    await ctx.send("https://fxtwitter.com/Ubatcha1/status/1509357312435183621")

  @commands.command(brief = "Yelan Infographic")
  async def info(ctx):
    await ctx.send("https://media.discordapp.net/attachments/943505502682382406/964397005570994196/yelan_infographic.png")

    
def setup(bot):
  bot.add_cog(Yelan(bot))