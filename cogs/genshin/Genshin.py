import discord
from discord.ext import commands

import res
from res.art import Art
from res.builds import builds, artifacts
from res.version_summary import version_summary

pullHistory = {
  'ryxke' : 'res/images/genshin/paimonmoe/ryxke_genshin_pull_history.jpg'
}

class Genshin(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  #Genshin Wishing History
  @commands.command(brief = "Genshin Wishing history from paimon.moe", aliases = ['wh'])
  async def wishhistory(self, ctx, user: str):

    user = user.lower()
    history = discord.File(pullHistory.get(user))
    await ctx.send(file = history)

  # EFFECTIVE ATTACK
  @commands.command(brief = "Used for comparing Builds")
  async def dmgcalc(self, ctx, atk: int, cr: float, cd: float):
    dmg = float(atk*(1 + cr*cd/10000))
    await ctx.send("Effective Attack is : " + str(dmg))

  #IMPORTS RANDOM ART FROM waifu_art.py
  @commands.command(brief = "Sends random art (May send NSFW art)", description = "Sends random art\n (may contain nsfw art)", aliases = ["art"])
  async def randomart(self, ctx):
    dir = "res/images/art/"
    image = discord.File(dir + Art.art())
    await ctx.send(file = image) 

  #CHARACTER BUILDS
  @commands.command(brief = "Jean Build")
  async def jean(self, ctx):
    
    embed = discord.Embed(title = "Jean", description = builds.jean(), color=0x06E5F5)
    embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/943505502682382406/944237761563603054/jean.png")
    embed.set_image(url = "https://media.discordapp.net/attachments/943505502682382406/944230219609436170/unknown.png")
    
    await ctx.send(embed=embed)


  #ARTIFACT CV
  @commands.command(brief="Artiact CV Chart")
  async def cv(self, ctx):
    image = "https://media.discordapp.net/attachments/865982244739874829/885365654079799326/image0.png"
    embed = discord.Embed(title = "Artifact CV chart")
    embed.set_image(url = image)
    await ctx.send(embed = embed)

  
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
  @commands.command(brief = "Ryxke's SSR  Weapon Collection", aliases = ["rw"])
  async def ryxke_weapon(self, ctx):
    link = "https://media.discordapp.net/attachments/943505502682382406/977056558053748736/IMG_20220520_065952.jpg"
    embed = discord.Embed(title = "Weapon flex by me")
    embed.set_image(url = link)
    await ctx.send(embed = embed)

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
      title = "«« ━━━━━━ ✥ 2.8 Presentation Summary ✥ ━━━━━━━ »»y"
      description = version_summary.v2_8(self)
      image = 'https://media.discordapp.net/attachments/943505502682382406/1008020971829067867/unknown.png?width=1073&height=603'

    elif (version == '3.0'):
      title = "«« ━━━━━━ ✥ 3.0 Presentation Summary ✥ ━━━━━━━ »»"
      description = version_summary().v3_0()
      image = 'https://media.discordapp.net/attachments/943505502682382406/1008019595443048609/unknown.png'

    elif (version == '3.1'):
      title = "«« ━━━━━━ ✥ 3.1 Presentation Summary ✥ ━━━━━━━ »»"
      description = version_summary().v3_1()
      image = 'https://media.discordapp.net/attachments/836722052924833798/1020327516281503825/unknown.png?width=1227&height=603'
      

    embed = discord.Embed(title = title, description = description, color=0x06E5F5)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/943505425742045267/992808669026721832/unknown.png?width=603&height=603")
    embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_image(url= image)
    await ctx.send(embed=embed)

  @commands.command(brief = "Genshin Char Infographics")
  async def info(self, ctx, name: str):
    if name == 'yoimiya':
      await ctx.send('https://media.discordapp.net/attachments/943505502682382406/994489866505179196/yF233Nb.png')
    

def setup(bot):
  bot.add_cog(Genshin(bot))
