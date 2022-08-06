import discord
from discord.ext import tasks, commands

class changelogs(commands.Cog):

    @commands.command(brief = 'Changes in Bot', aliases = ['cl', 'change', 'logs'])
    async def changelogs(self, ctx):

        description = """- added char cons, talents and level in !!enka"""
        embed = discord.Embed(title = 'Changelogs', description = description, color = 0x06E5F5)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(changelogs(bot))
    
