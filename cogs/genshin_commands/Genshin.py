import discord
from discord.ext import commands

from res.art import WaifuArt
from res.builds import builds, artifacts
from res.version_summary import version_summary

class Genshin(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  # EFFECTIVE ATTACK
  @commands.command(brief = "Used for comparing Builds")
  async def dmgcalc(self, ctx, atk: int, cr: float, cd: float):
    dmg = float(atk*(1 + cr*cd/10000))
    await ctx.send("Effective Attack is : " + str(dmg))

  #IMPORTS RANDOM ART FROM waifu_art.py
  @commands.command(brief = "Sends random art")
  async def randomart(self, ctx):
    await ctx.send(WaifuArt.ranArt()) 

  #CHARACTER BUILDS
  @commands.command(brief = "Jean Build")
  async def jean(self, ctx):
    embed = discord.Embed(title = "**Jean**", description = builds.jean(), color=0x06E5F5)
    embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/943505502682382406/944237761563603054/jean.png")
    await ctx.send(embed=embed)
    await ctx.send(artifacts.jean())


  #ARTIFACT CV
  @commands.command(brief="Artiact CV Chart")
  async def cv(self, ctx):
    image = "https://media.discordapp.net/attachments/865982244739874829/885365654079799326/image0.png"
    await ctx.send(image)

  
  #Raiden Q gif
  @commands.command()
  async def raiden(self, ctx):
    await ctx.send("https://c.tenor.com/i1N-3ZZkcucAAAAM/raiden-shogun-raiden.gif")

  #DIMINISHING RETURNS
  @commands.command(brief = "A quick explaination of Diminishing Returns")
  async def dimreturns(self, ctx):
    dimReturns = "https://media.discordapp.net/attachments/805680026229276696/877048804875067442/8us3bihon4g71.jpg"
    await ctx.send(dimReturns)

  #ENERGY CALCULATOR
  @commands.command(brief = "Energy Calculator")
  async def energycalc(self, ctx):
    link = "https://docs.google.com/spreadsheets/u/0/d/1-vkmgp5n0bI9pvhUg110Aza3Emb2puLWdeoCgrxDlu4/htmlview"
    await ctx.send(link)

  #All of Ryxke Weapons
  @commands.command(brief = "Ryxke's SSR  Weapon Collection")
  async def ryxke_weapon(self, ctx):
    link = "https://media.discordapp.net/attachments/943505502682382406/977056558053748736/IMG_20220520_065952.jpg"
    await ctx.send(link)

  #Mats required to level characters overall(Genshin)
  @commands.command(brief = "Genshin Character and Weapon mats")
  async def char_mats(self, ctx):
    await ctx.send("https://media.discordapp.net/attachments/943505502682382406/964883155448393798/image0-4.png")

  #Sends Genshin Character guides
  @commands.command(brief = "Genshin Character Guides")
  async def guide(self, ctx, char):
    await ctx.send(f"https://keqingmains.com/{char}/")

  @commands.command(brief= "Versions Summary")
  async def summary(self, ctx, version: str):
    if (version == "2.8"):
      embed = discord.Embed(title = "v2.8 Summary", description = version_summary.v2_8())
      embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
      # await ctx.send(version_summary.v2_8())

def setup(bot):
  bot.add_cog(Genshin(bot))
