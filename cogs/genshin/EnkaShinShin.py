import discord
from discord.ext import tasks, commands
import asyncio
import enkapy
from enkapy import Enka


client = Enka()
Ryxke = 712994834
class EnkaShinShin(commands.Cog):

  @commands.command(brief = "Character Details")
  async def enka(self, ctx, uid, char):
    await client.load_lang()
    try:
      user = await client.fetch_user(uid)
    except:
      await ctx.send("Your Character Details are Hidden")
      return

    des = ""
    artifactData = []
    artiSubsData = []
    flowerSubs, featherSubs, sandsSubs, gobletSubs, circletSubs = [],[],[],[],[]
    
    for character in user.characters:
      if str(character.name) == str(char):
        des = f"**Character :** {character.name}\n **Friendship :** {character.friendship.level}\n **Weapon** : {character.weapon.nameText}"
      
        for arti in character.artifacts: 
          
          artifactData.append(f"{arti.nameText}({statName(arti.main_stat.prop)} : {arti.main_stat.value})")
          
          for subs in arti.sub_stats:
            f"subs.prop : subs.value"
            artiSubsData.append(f"{statName(subs.prop)} : {subs.value}")

            if len(artiSubsData) > 0 and  len(artiSubsData) <= 4:
                flowerSubs.append(f"{statName(subs.prop)} : {subs.value}")

            elif len(artiSubsData) > 4 and len(artiSubsData) <= 8:
                featherSubs.append(f"{statName(subs.prop)} : {subs.value}")
                
            elif len(artiSubsData) > 8 and len(artiSubsData) <= 12:
                sandsSubs.append(f"{statName(subs.prop)} : {subs.value}")
                
            elif len(artiSubsData) > 12 and len(artiSubsData) <= 16:
                gobletSubs.append(f"{statName(subs.prop)} : {subs.value}")
                
            elif len(artiSubsData) > 16 and len(artiSubsData) <= 20:
                circletSubs.append(f"{statName(subs.prop)} : {subs.value}")

    embedDataMainProp = ""
    for i in range(len(artifactData)):
      artiData = f"{artifactData[i]}"
      embedDataMainProp = embedDataMainProp + "\n" + artiData

    embedDataSubProp = ''
    for i in range(len(artiSubsData)):
      subsData = f"{artiSubsData[i]}"
      embedDataSubProp = embedDataSubProp + '\n' + subsData

    flower = ''
    for i in range(len(flowerSubs)):
      flower = flower + '\n' + flowerSubs[i]
    feather = ''
    for i in range(len(flowerSubs)):
      feather = feather + '\n' + featherSubs[i]
    sands = ''
    for i in range(len(flowerSubs)):
      sands = sands + '\n' + sandsSubs[i]
    goblet = ''
    for i in range(len(flowerSubs)):
      goblet = goblet + '\n' + gobletSubs[i]
    circlet = ''
    for i in range(len(flowerSubs)):
      circlet = circlet + '\n' + circletSubs[i]   
        
    embed = discord.Embed(title = f"{user.player.nickname} Wl{user.player.worldLevel} {uid}", description = des, color=0x06E5F5)
    embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/943505502682382406/992816537645887589/unknown.png")
    try:
       embed.add_field(name = artifactData[0], value = flower)
       embed.add_field(name = artifactData[1], value = feather)
       embed.add_field(name = artifactData[2], value = sands)
       embed.add_field(name = artifactData[3], value = goblet)
       embed.add_field(name = artifactData[4], value = circlet)
    except:
      await ctx.send("Character is missing artifact \nOther reason : Character not using fully leveled 5star/4star artifact")
      return

    await ctx.send(embed = embed)
    

  @commands.command(brief = "Shows Player Details")
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
    **Signature :** *{player.signature}*
    **Achievements :** {player.finishAchievementNum}
    """
    embed.add_field(name = "Player details : ",
                   value = details)
    
    charData = []
    for char in user.characters:
      charData.append(f'{char.name}')

    data = f""
    for i in range(len(charData)):
      data = data + '\n' +  f'{charData[i]} (lvl{player.showAvatarInfoList[i].level})'
      
    embed.add_field(name = "Characters :", value = data)
    
    abyss = f'Floor {player.towerFloorIndex} Chamber {player.towerLevelIndex}'
    embed.add_field(name = "Abyss Progess :", 
                    value = abyss)
    embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url = ctx.author.avatar_url)
   
    await ctx.send(embed = embed)

  
  # async def enka(self, ctx, uid, *, char):
  #   await client.load_lang()
  #   try:
  #     user = await client.fetch_user(uid)
  #   except:
  #     await ctx.send("Your Character Details are Hidden")
  #     return

  #   for character in user.characters:
  #     if str(character.name) == str(char):
  #       description = f"**{character.name}**\n **Friendship :** {character.friendship.level}\n **Weapon** : {character.weapon.nameText}"
  #       embed = discord.Embed(title = user.player.nickname, description = description, color=0x06E5F5)
  #       embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  #       await ctx.send(embed=embed)

  #       for arti in character.artifacts: 
  #         embed1 = discord.Embed(title = f"{arti.nameText}({arti.main_stat.value})",description = arti.main_stat.prop, color=0x06E5F5)
  #         for subs in arti.sub_stats:
  #           embed1.add_field(name = subs.prop, value = subs.value)
  #         await ctx.send(embed=embed1)
           
def setup(bot):
  bot.add_cog(EnkaShinShin(bot))

def statName(propname):

    stats = {
      "FIGHT_PROP_CRITICAL" : "CR%",
      "FIGHT_PROP_CRITICAL_HURT" : "CD%",
      "FIGHT_PROP_ATTACK_PERCENT" : "Atk%",
      "FIGHT_PROP_DEFENSE_PERCENT" : "Def%",
      "FIGHT_PROP_HP_PERCENT" : "HP%",
      "FIGHT_PROP_CHARGE_EFFICIENCY" : "ER%",
      "FIGHT_PROP_ATTACK" : "Atk",
      "FIGHT_PROP_DEFENSE" : "Def",
      "FIGHT_PROP_HP" : "HP",
      "FIGHT_PROP_ELEMENT_MASTERY" : "EM",
      "FIGHT_PROP_WIND_ADD_HURT" : "Anemo Dmg%",
      "FIGHT_PROP_FIRE_ADD_HURT" : "Pyro Dmg%",
      "FIGHT_PROP_WATER_ADD_HURT" : "Hydro Dmg%",
      "FIGHT_PROP_ELEC_ADD_HURT" : "Electro Dmg%",
      "FIGHT_PROP_ICE_ADD_HURT" : "Cryo Dmg%",
      "FIGHT_PROP_PHYSICAL_ADD_HURT" : "Physical Dmg%",
      "FIGHT_PROP_ROCK_ADD_HURT" : "Geo Dmg%"      
    }

    return stats.get(propname)