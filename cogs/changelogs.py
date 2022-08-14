import discord
from discord.ext import tasks, commands

class changelogs(commands.Cog):

    @commands.command(brief = 'Changes in Bot', aliases = ['cl', 'change', 'logs'])
    async def changelogs(self, ctx):
        description = """
- added Genshin v3.0 summary
        """
        embed = discord.Embed(title = 'Changelogs', description = description, color = 0x06E5F5)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(changelogs(bot))

"""
before genshin v3.0
- added uid resgistering (database) as shown in image below
- added command for artifact cv ie !!artifactcv <uid> <char>.
- Shows artifact cd, cr and cv in !!enka command
- added char cons, talents and level in !!enka
"""
    
