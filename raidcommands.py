import discord
from discord.ext import commands

class raidcoms():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def rancor1hr(self):
        await self.bot.say("@everyone Rancor FFA starting 1 hour from now")
        
    @commands.command(pass_context=True)
    async def rancornow(self):
        await self.bot.say("@everyone Rancor FFA starts now")
        
def setup(bot):
    n = raidcoms(bot)
    bot.add_cog(n)