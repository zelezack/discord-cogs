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
        image = "pictures/giphy.gif"
        channel = ctx.message.channel
        self.today = date.today()
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        ruorder = []
        euorder = []
        ukorder = []
        estorder = []
        cstorder = []
        pstorder = []

        for p in parsed['squad']:
            ordname = p['order']
            if ordname == 'ruorder':
                rotation = ', '.join(map(str,p['rotation']))
                ruorder.append(rotation)
                ruflag = p['flag']
                rutz = p['tzname']
            elif ordname == 'euorder':
                rotation = ', '.join(map(str,p['rotation']))
                euorder.append(rotation)
                euflag = p['flag']
                eutz = p['tzname']
            elif ordname == 'ukorder':
                rotation = ', '.join(map(str,p['rotation']))
                ukorder.append(rotation)
                ukflag = p['flag']
                uktz = p['tzname']
            elif ordname == 'estorder':
                rotation = ', '.join(map(str,p['rotation']))
                estorder.append(rotation)
                usflag = p['flag']
                esttz = p['tzname']
            elif ordname == 'cstorder':
                rotation = ', '.join(map(str,p['rotation']))
                cstorder.append(rotation)
                csttz = p['tzname']
            else:
                rotation = ', '.join(map(str,p['rotation']))
                pstorder.append(rotation)
                psttz = p['tzname']
                    
        await self.bot.send_file(channel, image)
        await self.bot.say("Rotation list for " + str(self.today) + ':\n' +
                ':flag_ru: MR: ' + ', '.join(ruorder) +'\n' +
                ':flag_eu: Viva: ' + ', '.join(euorder) + ', LouLou, Alex\n' +
                ':flag_gb: UK: ' +', '.join(ukorder) + '\n' +
                ':flag_us: EST: ' +', '.join(estorder)+ '\n'+
                ':flag_us: CST: ' + ', '.join(cstorder) + '\n' +
                ':flag_us: PST: ' +  ', '.join(pstorder) + '\n')

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_messages=True)
    async def newday(self, ctx):
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        for p in parsed['squad']:
            ordname = p['order']
            if ordname == 'euorder':
                rotation = ', '.join(map(str,p['rotation']))
                person = p['rotation'].pop(0)
                p['rotation'].append(person)
            if ordname == 'ukorder':
                rotation = ', '.join(map(str,p['rotation']))
                person = p['rotation'].pop(0)
                p['rotation'].append(person)
            if ordname == 'estorder':
                rotation = ', '.join(map(str,p['rotation']))
                person = p['rotation'].pop(0)
                p['rotation'].append(person)
            if ordname == 'cstorder':
                rotation = ', '.join(map(str,p['rotation']))
                person = p['rotation'].pop(0)
                p['rotation'].append(person)
        await self.bot.say("New day complete")
        with open('cogs/assets/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)

def setup(bot):
    bot.add_cog(rotationcog(bot))