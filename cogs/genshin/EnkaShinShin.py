import discord
from discord.ext import tasks, commands
import asyncio
import enkapy
from enkapy import Enka
from modules.mongo_genshin import MongoGenshin


client = Enka()
mongoClient = MongoGenshin()
class EnkaShinShin(commands.Cog):

  def isInteger(self, s):
 
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
 
    return True

  @commands.command()
  async def register(self, ctx, user: str, uid: int):

    mongoClient.add(user, uid)

    embed = discord.Embed(title = 'Successful Added', 
                          description = f'Successful added {user} {uid} \n*uids and username are not shared so rest assured while registering*', color = 0x06E5F5)
    embed.set_thumbnail(url= ctx.author.avatar_url)
    embed.set_footer(text='used for !!enka and !!player commands currently')
    await ctx.send(embed = embed)

  @commands.command(brief = 'Shows Artifact Crit Value', aliases = ['articv', 'acv'])
  async def artifactcv(self, ctx, id, *, char):
    
    cr, cd = 0, 0
    
    # if uid == 'ryxke':
    #   uid = 712994834

    if self.isInteger(id) == True:
      uid = id
    else:
      id = str(id)
      uid = mongoClient.get_uid(id)
  
    await client.load_lang()
    user = await client.fetch_user(uid)
    
    for character in user.characters:
      if str(character.name) == char:
        for arti in character.artifacts:
          if str(arti.main_stat.prop) == "FIGHT_PROP_CRITICAL":
            cr = cr + arti.main_stat.value
          elif str(arti.main_stat.prop) == 'FIGHT_PROP_CRITICAL_HURT':
            cd = cd + arti.main_stat.value

          for subs in arti.sub_stats:
            if str(subs.prop) == "FIGHT_PROP_CRITICAL":
              cr = cr + subs.value
            elif str(subs.prop) == 'FIGHT_PROP_CRITICAL_HURT':
              cd = cd + subs.value

    cv = cd + cr*2

    embed = discord.Embed(title = f'Artifact CV for {char}', description = f'CV : {cv}',
                          color = 0x06E5F5)
    await ctx.send(embed = embed)

      
  @commands.command(brief = "Character Details")
  async def enka(self, ctx, id, *, char):
    
    
    cr, cd = 0, 0
    if self.isInteger(id) == True:
      uid = id
    else:
      id = str(id)
      uid = mongoClient.get_uid(id)
    
    await client.load_lang()
    try:
      user = await client.fetch_user(uid)
    except:
      await ctx.send("Please recheck the UID or Turn on Character Details in game")
      return

    des = ""
    artifactData = []
    artiSubsData = []
    flowerSubs, featherSubs, sandsSubs, gobletSubs, circletSubs = [],[],[],[],[]

    for character in user.characters:
      if str(character.name) == char:
        for arti in character.artifacts:
          if str(arti.main_stat.prop) == "FIGHT_PROP_CRITICAL":
            cr = cr + arti.main_stat.value
          elif str(arti.main_stat.prop) == 'FIGHT_PROP_CRITICAL_HURT':
            cd = cd + arti.main_stat.value

          for subs in arti.sub_stats:
            if str(subs.prop) == "FIGHT_PROP_CRITICAL":
              cr = cr + subs.value
            elif str(subs.prop) == 'FIGHT_PROP_CRITICAL_HURT':
              cd = cd + subs.value
    
    for character in user.characters:
      if str(character.name) == str(char):

        levels = []
        for i in character.skill_level.values():
         levels.append(i)

        cons = 0
        for constellation in character.constellations:
          if constellation.activated:
            cons = cons + 1

        des = f"Lvl{character.level} C{cons} {character.name} \n**Friendship :** {character.friendship.level} \n**Weapon** : R{character.weapon.refine + 1} {character.weapon.nameText} (Lvl{character.weapon.level})"
        des = des + f'\n**Talents :**  {levels[0]}/{levels[1]}/{levels[2]}'
        des = des + f'\nArtifact CR : {cr} \nArtifact CD : {cd}'

        com = character.combat

        stats = f'Max HP : {com.FIGHT_PROP_CUR_HP} \nAttack :{com.FIGHT_PROP_CUR_ATTACK} \nDef : {com.FIGHT_PROP_CUR_DEFENSE} \nEM : {com.FIGHT_PROP_ELEMENT_MASTERY}'
        stats = stats + f'\nArtifact CV : {cr * 2 + cd}'
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
       embed.add_field(name = 'Character Stats', value = stats)
       embed.add_field(name = artifactData[0], value = flower)
       embed.add_field(name = artifactData[1], value = feather)
       embed.add_field(name = artifactData[2], value = sands)
       embed.add_field(name = artifactData[3], value = goblet)
       embed.add_field(name = artifactData[4], value = circlet)
    except:
      await ctx.send('Error while getting data for specified character \nPossible reasons \n-Character dont have artifact \n-UID is not available')
      return

    await ctx.send(embed = embed)
    

  @commands.command(brief = "Shows Player Details")
  async def player(self, ctx, id):

    if self.isInteger(id) == True:
      uid = id
    else:
      id = str(id)
      uid = mongoClient.get_uid(id)
      
    await client.load_lang()
    try:
      user = await client.fetch_user(uid)
    except:
      await ctx.send("Couldn't find that player")
      return
      
    player = user.player

    embed = discord.Embed(title = "Player Showcase : ",
                         color = 0x06E5F5)
    details = f"**Nickname :** {player.nickname} \n**Adventure Rank :** {player.level} \n**World level :** {player.worldLevel} \n**Signature :** *{player.signature}* \n**Achievements :** {player.finishAchievementNum}"
    
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
    embed.add_field(name = "Abyss Progess :", value = abyss)
    embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url = ctx.author.avatar_url)
   
    await ctx.send(embed = embed)

           
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