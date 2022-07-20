import discord
from discord.ext import tasks, commands
import asyncio
import enkapy
from enkapy import Enka


client = Enka()
class EnkaShinShin(commands.Cog):

  async def enkaem(self, ctx, uid, char):
    # char = char.lower()
    await client.load_lang()
    user = await client.fetch_user(uid)


    # await ctx.send(f"Nickname: {user.player.nickname}")
    # await ctx.send(f"Level: {user.player.level}")
    for character in user.characters:
      if str(character.name) == str(char):
         embed = discord.Embed(title = user.player.nickname, description = char, color=0x06E5F5)
         embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        
         await ctx.send(embed=embed)

  @commands.command()
  async def enka(self, ctx, uid, char):
    # char = char.lower()
    await client.load_lang()
    user = await client.fetch_user(uid)
    await ctx.send(f"**Nickname :** {user.player.nickname}")
    await ctx.send(f"**Adventure Rank :** {user.player.level}")
    for character in user.characters:
      if str(character.name) == str(char):
        await ctx.send(f"**Character :** {character.name}")
        await ctx.send(f"**Weapon** : {character.weapon.nameText}")
        for artifact in character.artifacts:
            await ctx.send(f'\t **Artifact : **{artifact.setNameText} {artifact.nameText}:')
            await ctx.send(f'\t{artifact.main_stat.prop}:{artifact.main_stat.value}')
            for sub_stats in artifact.sub_stats:
                await ctx.send(f'\t\t{sub_stats.prop}:{sub_stats.value}')
           
def setup(bot):
  bot.add_cog(EnkaShinShin(bot))