import discord
from discord.ext import tasks, commands

import modules.genshin_data
from modules.genshin_data import genshin_artifact_data, genshin_character_data, getCharIcon
from cogs.constants import constants

artiData = genshin_artifact_data()
charData = genshin_character_data()

class genshin_details(commands.Cog):

    @commands.command()
    async def char(self, ctx, *, name):
        
        print(name)
        baseData = charData.getCharBaseDetails(name)
        eleSkill = charData.getCharEleSkill(name)
        burstSkill = charData.getCharBurstSkill(name)
        naSkill = charData.getCharNormalAttack(name)

        embed = discord.Embed(title = 'Character Details', description = baseData, color = constants().COLOR)
        embed.add_field(name = 'Normal Attacks', value = naSkill)
        embed.add_field(name='Elemental skill', value= eleSkill)
        embed.add_field(name='Burst Skill', value= burstSkill)

        await ctx.send(embed = embed)

def setup(bot):
  bot.add_cog(genshin_details(bot))