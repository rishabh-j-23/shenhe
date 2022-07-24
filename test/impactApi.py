import discord
from discord.ext import tasks, commands

class impactApi(commands.Cog):

  @commands.command()
  async def ids(self, ctx):
    channelID = ctx.


def setup(bot):
  bot.add_cog(impactApi(bot))