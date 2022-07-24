import discord
from discord.ext import tasks, commands
import asyncio
import enkapy
from enkapy import Enka


client = Enka()
class EnkaShinShin(commands.Cog):

  @commands.command()
  async def enka(self, ctx, uid, char):
    await client.load_lang()
    user = await client.fetch_user(uid)

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