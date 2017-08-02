import discord
from discord.ext import commands
from __main__ import send_cmd_help
from .utils import checks
import urllib
import requests
from bs4 import BeautifulSoup

class shardcog:
    """Discord cog for shard chats"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def welcome(self):
        await self.bot.say('Welcome to shard chat\n'+
                           'The Basics:\n'+
                           "We're all about making sure you can get the best position for your payout. We watch out for each other and lock / block unknowns.\n\n"+
                           "Who can you hit?  Anyone who isn't in this room is fair game (we usually don't hit Darth Dislnick, he used to be in the room, but isn't, and he usually plays nice, long story). If someone is in this room and has a payout before you, feel free to hit them to move up.\n\n"+
                           "Basically, don't hit people who are in payouts ahead of you.  Johny usually stays in the top 5 at all times, he created this chat and he's usually very busy during his payout window and doesn't get a lot of chances to move up.\n\n"
                           "Use the @ mentions to get people's attention, especially when the shtlist is on the move. To help set up locks or pull people back who don't belong in position.")
        await self.bot.say("Helpful tools for you to use to remember:\n\n"+
                           "!payout - displays the payout by timezones\n"+
                           "!rotation - who is taking 1-5ish on that day.  It dynamically changes.\n"+
                           "!shitlist - these are people who come up and try to snipe or fuck with us during the day, we fuck punch first!\n"
                           "!reacharound # - Put in a number and it tells you the maximum jump you can make for next position.\n"+
                           "!swgoh <name> - will search swgoh.gg for practically anything.\n\n"+
                           "Some bonus bot commands:\n"+
                           "!choochoo\n"+
                           "!zetabobba\n"+
                           "!buttstuff\n"+
                           "!gif\n"+
                           "!urban\n"
                           )
            
    @commands.command(pass_context=True, no_pm=True)
    async def swgoh(self, ctx, *,text):

        """Its google, you search with it."""
        search_type = ctx.message.content[len(ctx.prefix + ctx.command.name) + 1:].lower().split(" ")

        uri = "https://www.google.com/search?q=swgoh.gg+"
        quary = str(ctx.message.content[len(ctx.prefix + ctx.command.name) + 1:])
        encode = urllib.parse.quote_plus(quary, encoding='utf-8', errors='replace')
        searchURL= (uri + encode)
        r = requests.get(searchURL)
        soup = BeautifulSoup(r.text, "html.parser")
        urlfinder = soup.find('cite').text
        await self.bot.say(urlfinder)
        
        
    @commands.command(pass_context=True, no_pm=True)
    async def helper(self):
        await self.bot.say("List of helpful commands:\n\n"+
                           "!reacharound # - Put in a number and it tells you the maximum jump you can make for next position.\n"+
                           "!swgoh <name> - will search swgoh.gg for practically anything.\n"+
                           "!ships - displays the payout by timezones\n"+
                           "!gif <text> - displays a gif based on the text\n"+
                           "!urban <text> - displays urban dictionary references\n")
            
    @commands.command(pass_context=True)
    async def reacharound(self, ctx, position):
        #used to determine biggest jump
        winner = "pictures/winner.gif"
        channel = ctx.message.channel
        wru = int(position)
        if wru >= 37:
            await self.bot.say("You're fucking lost, move up to find a better position")
        elif wru == 36:
            await self.bot.say("Farthest you can jump to is 28")
        elif wru == 35:
            await self.bot.say("Farthest you can jump to is 27")
        elif wru == 34 or wru == 33:
            await self.bot.say("Farthest you can jump to is 26")
        elif wru == 32:
            await self.bot.say("Farthest you can jump to is 25")
        elif wru == 31:
            await self.bot.say("Farthest you can jump to is 24")
        elif wru == 30:
            await self.bot.say("Farthest you can jump to is 23")            
        elif wru == 29:
            await self.bot.say("Farthest you can jump to is 22")
        elif wru == 28:
            await self.bot.say("Farthest you can jump to is 21")
        elif wru == 27:
            await self.bot.say("Farthest you can jump to is 20")
        elif wru == 26:
            await self.bot.say("Farthest you can jump to is 19")
        elif wru == 25 or wru ==24:
            await self.bot.say("Farthest you can jump to is 18")
        elif wru == 23:
            await self.bot.say("Farthest you can jump to is 17")            
        elif wru == 22:
            await self.bot.say("Farthest you can jump to is 16")
        elif wru == 21:
            await self.bot.say("Farthest you can jump to is 15")
        elif wru == 20:
            await self.bot.say("Farthest you can jump to is 14")
        elif wru == 19 or wru ==18:
            await self.bot.say("Farthest you can jump to is 13")
        elif wru == 17:
            await self.bot.say("Farthest you can jump to is 12")
        elif wru == 16:
            await self.bot.say("Farthest you can jump to is 11")
        elif wru == 15:
            await self.bot.say("Farthest you can jump to is 10")            
        elif wru == 14:
            await self.bot.say("Farthest you can jump to is 9")
        elif wru == 13 or wru ==12:
            await self.bot.say("Farthest you can jump to is 8")
        elif wru == 11:
            await self.bot.say("Farthest you can jump to is 7")
        elif wru == 10:
            await self.bot.say("Farthest you can jump to is 6")
        elif wru == 9:
            await self.bot.say("Farthest you can jump to is 5")
        elif wru == 8:
            await self.bot.say("Farthest you can jump to is 4")            
        elif wru == 7:
            await self.bot.say("Farthest you can jump to is 3")
        elif wru == 6:
            await self.bot.say("Farthest you can jump to is 2")
        elif wru == 1:
            await self.bot.send_file(channel, winner)
        else:
            await self.bot.say("You really need me to tell you to go for #1?")
            
        
            
def setup(bot):
    bot.add_cog(shardcog(bot))