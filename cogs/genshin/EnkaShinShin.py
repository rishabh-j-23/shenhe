import discord
from discord.ext import tasks, commands
import asyncio
import enkapy
from enkapy import Enka


client = Enka()
class EnkaShinShin(commands.Cog):

  @commands.command()
  async def player(self, ctx, uid):
    await client.load_lang()
    try:
      user = await client.fetch_user(uid)
    except:
      await ctx.send("Couldn't find that player")
      return
    player = user.player

    embed = discord.Embed(title = "Player Showcase : ",
                         color = 0x06E5F5)
    details = f"""**Nickname :** {player.nickname}
    **Adventure Rank :** {player.level}
    **World level :** {player.worldLevel}
    **Signature :** {player.signature}
    **Achievements :** {player.finishAchievementNum}
    """
    embed.add_field(name = "Player details : ",
                   value = details)
    
    charData = []
    for char in user.characters:
      charData.append(f'{char.name}')

    data = f"""{charData[0]} (lvl{player.showAvatarInfoList[0].level})
    {charData[1]} (lvl{player.showAvatarInfoList[1].level})
    {charData[2]} (lvl{player.showAvatarInfoList[2].level})
    {charData[3]} (lvl{player.showAvatarInfoList[3].level})
    {charData[4]} (lvl{player.showAvatarInfoList[4].level})
    {charData[5]} (lvl{player.showAvatarInfoList[5].level})
    {charData[6]} (lvl{player.showAvatarInfoList[6].level})
    {charData[7]} (lvl{player.showAvatarInfoList[7].level})
    """
    embed.add_field(name = "Characters :", 
                    value = data)
    
    abyss = f'{player.towerFloorIndex}-{player.towerLevelIndex}'
    embed.add_field(name = "Abyss Progess :", 
                    value = abyss)
    embed.add_field()
    embed.set_thumbnail(url = ctx.author.avatar_url)
   
    await ctx.send(embed = embed)

  
  @commands.command(brief = "Character Details")
  async def enka(self, ctx, uid, *, char: str):
    await client.load_lang()
    char = char.capitalize()
    try:
      user = await client.fetch_user(uid)
    except:
      await ctx.send("Your Character Details are Hidden")
      return

    for character in user.characters:
      if str(character.name) == str(char):
        description = f"**{character.name}**\n **Friendship :** {character.friendship.level}\n **Weapon** : {character.weapon.nameText}"
        embed = discord.Embed(title = user.player.nickname, description = description, color=0x06E5F5)
        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        for arti in character.artifacts: 
          embed1 = discord.Embed(title = f"{arti.nameText}({arti.main_stat.value})",description = arti.main_stat.prop, color=0x06E5F5)
          for subs in arti.sub_stats:
            embed1.add_field(name = subs.prop, value = subs.value)
          await ctx.send(embed=embed1)

           
def setup(bot):
  bot.add_cog(EnkaShinShin(bot))