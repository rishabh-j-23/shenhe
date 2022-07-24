import discord
from discord.ext import tasks, commands
import json

class Artifacts(commands.Cog):

  def printarti(name):
    with open("res/genshin/artifacts.json", "r") as op:
      data = json.load(op)
      print(data[name]["name"])
      bonus = data[name]["bonuses"]
    
      print(bonus[0]['desc'])
      print(bonus[1]['desc'])
    
  @commands.command(brief = "Artifacts Set Bonus Details")
  async def artifact(self, ctx, *, name):
    try:
     with open("res/genshin/artifacts.json", "r") as op:
      data = json.load(op)
    except:
      await ctx.send(FileNotFoundError)
      
    bonus = data[name]["bonuses"]
    setBonus = f"""**2pc :** {bonus[0]['desc']}
    **4pc :** {bonus[1]['desc']}"""
    embed = discord.Embed(title = name, description = setBonus, color = 0x06E5F5)
    embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Artifacts(bot))