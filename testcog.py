import discord
import json
from datetime import date
from discord.ext import commands
from cogs.utils.dataIO import fileIO

class testing:
    
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(testing(bot))