import discord
from discord.ext import tasks, commands

class changelogs(commands.Cog):

    @commands.command(brief = 'Changes in Bot', aliases = ['cl', 'change', 'logs'])
    async def changelogs(self, ctx):

        description = """
        - added uid resgistering (database) as shown in image below
        - added command for artifact cv ie !!artifactcv <uid> <char>.
        - Shows artifact cd, cr and cv in !!enka command
        - added char cons, talents and level in !!enka
        """
        embed = discord.Embed(title = 'Changelogs', description = description, color = 0x06E5F5)
        embed.set_image(url= 'https://media.discordapp.net/attachments/943505502682382406/1005801288182812733/unknown.png')
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(changelogs(bot))
    
