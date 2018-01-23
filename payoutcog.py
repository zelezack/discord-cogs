import discord
import json
from datetime import datetime, date, time, timedelta, timezone
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import fileIO
from __main__ import send_cmd_help

import logging
import time

class payoutcog:
    """Discord cog for shard chats"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def payout(self, ctx):
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        ruorder = []
        euorder = []
        ukorder = []
        estorder = []
        cstorder = []
        pstorder = []

        self.today = date.today()
        current_time = time.strftime('%H:%M:%S', time.localtime())
        if ctx.invoked_subcommand is None:
                for p in parsed['squad']:
                    ordname = p['order']
                    if ordname == 'ruorder':
                        members = ', '.join(map(str,p['members']))
                        ruorder.append(members)
                        ruflag = p['flag']
                        rutz = p['tzname']
                        ruutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            rupayout = ' :moneybag:'
                        else:
                            rupayout = ' - :clock130: ' + str(ruutc)
                    elif ordname == 'euorder':
                        members = ', '.join(map(str,p['members']))
                        euorder.append(members)
                        euflag = p['flag']
                        eutz = p['tzname']
                        euutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            eupayout = ' :moneybag:'
                        else:
                            eupayout = ' - :clock130: ' + str(euutc)
                    elif ordname == 'ukorder':
                        members = ', '.join(map(str,p['members']))
                        ukorder.append(members)
                        ukflag = p['flag']
                        uktz = p['tzname']
                        ukutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            ukpayout = ' :moneybag:'
                        else:
                            ukpayout = ' - :clock130: ' + str(ukutc)              
                    elif ordname == 'estorder':
                        members = ', '.join(map(str,p['members']))
                        estorder.append(members)
                        usflag = p['flag']
                        esttz = p['tzname']
                        estutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))  
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            estpayout = ' :moneybag:'
                        else:
                            estpayout = ' - :clock130: ' + str(estutc)                      
                    elif ordname == 'cstorder':
                        members = ', '.join(map(str,p['members']))
                        cstorder.append(members)
                        csttz = p['tzname']
                        cstutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            cstpayout = ' :moneybag:'
                        else:
                            cstpayout = ' - :clock130: ' + str(cstutc)                   
                    else:
                        members = ', '.join(map(str,p['members']))
                        pstorder.append(members)
                        psttz = p['tzname']
                        psttz = p['tzname']
                        pstutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            pstpayout = ' :moneybag:'
                        else:
                            pstpayout = ' - :clock130: ' + str(pstutc)

                await self.bot.say("Payout list:\n" +
                    ruflag + rutz + " - "+ ', '.join(ruorder) + str(rupayout) +"\n"+
                    euflag +  eutz + " - "+ ', '.join(euorder) + str(eupayout) +"\n"+
                    ukflag +  uktz + " - "+ ', '.join(ukorder) + str(ukpayout) +"\n"+
                    usflag +  esttz + " - "+ ', '.join(estorder) + str(estpayout) +"\n"+
                    usflag +  csttz + " - "+ ', '.join(cstorder) + str(cstpayout) +"\n"+
                    usflag +  psttz + " - "+ ', '.join(pstorder) + str(pstpayout)+ "\n")
        await send_cmd_help(ctx)
            
    @payout.command(pass_context=True, name='add')    
    async def _payout_add(self,ctx,timezone, *, name):
        '''- Add a person to a payout\n
        Valid timezone format gmt+/-#'''
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        log = logging.getLogger("red.testcog")
        log.setLevel(logging.INFO)
        person = name
        tz = timezone.upper()
        for p in parsed['squad']:
            if tz == p['tzname'] and person in p['members']:
                await self.bot.say("User already in payout")
            elif tz == p['tzname'] and person not in p['members']:
                p['members'].append(person)
                await self.bot.say(str(person) +" added to "+ tz + " payout")
            elif tz != p['tzname']:
                log.debug("Timezone doesn't match")
            else:
                await self.bot.say("Something went wrong...blame Cherno")
        with open('cogs/assets/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
    
    @payout.command(pass_context=True, name='remove')    
    async def _payout_remove(self,ctx,timezone, *, name):
        '''- Remove a person from a payout\n
        Valid timezone format gmt+/-#'''
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        log = logging.getLogger("red.testcog")
        log.setLevel(logging.INFO)
        person = name
        tz = timezone.upper()
        for p in parsed['squad']:
            if tz == p['tzname'] and person not in p['members']:
                await self.bot.say("User not in payout")
            elif tz == p['tzname'] and person in p['members']:
                p['members'].remove(person)
                await self.bot.say(str(person) +" removed from "+ tz + " payout")
            elif tz != p['tzname']:
                log.debug("Timezone doesn't match")
            else:
                await self.bot.say("Something went wrong...blame Cherno")
        with open('cogs/assets/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
       
def setup(bot):
    bot.add_cog(payoutcog(bot))