import discord
import json
from datetime import datetime, date, time, timedelta, timezone
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import fileIO
from __main__ import send_cmd_help

import logging
import time

class rotationcog:
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def rotation(self, ctx):
        image = "cogs/giphy.gif"
        channel = ctx.message.channel
        self.today = date.today()
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        utcp2 = []

        for p in parsed['newsquad']:
            ordname = p['order']
            if ordname == 'utcp2':
                rotation = ', '.join(map(str,p['rotation']))
                utcp2.append(rotation)
                utcp2flag = p['flag']
                utcp2tz = p['tzname']

                    
        await self.bot.send_file(channel, image)
        await self.bot.say("Rotation list for " + str(self.today) + ':\n' +
                utcp2flag + utcp2tz + " - " + ', '.join(utcp2) +"\n"
                )
    @commands.command(pass_context=True)
    async def rotationSFW(self, ctx):
        channel = ctx.message.channel
        self.today = date.today()
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        utcp2 = []

        for p in parsed['squad']:
            ordname = p['order']
            if ordname == 'utcp2':
                rotation = ', '.join(map(str,p['rotation']))
                utcp2.append(rotation)
                utcp2flag = p['flag']
                utcp2tz = p['tzname']
                    
        await self.bot.say("Rotation list for " + str(self.today) + ':\n' +
                utcp2flag + utcp2tz + ', - '.join(utcp2) +'\n'
                )

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_messages=True)
    async def newday(self, ctx):
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        for p in parsed['newsquad']:
            ordname = p['order']
            if ordname == 'utcp2order':
                rotation = ', '.join(map(str,p['rotation']))
                person = p['rotation'].pop(0)
                p['rotation'].append(person)
        await self.bot.say("New day complete")
        with open('cogs/assets/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)

def setup(bot):
    bot.add_cog(rotationcog(bot))
