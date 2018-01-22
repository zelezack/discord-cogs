import discord
import json
from datetime import datetime, date, time, timedelta, timezone
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import fileIO
from __main__ import send_cmd_help

import logging
import time

class shipscog:
    """Discord cog for shard chats"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(pass_context=True)
    async def ships(self, ctx):
        with open('cogs/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        indorder = []
        taiorder = []
        saorder =[]
        euorder = []
        pstorder = []
        estorder = []
        cstorder = []
        mstorder = []
        akorder = []

        self.today = date.today()
        current_time = time.strftime('%H:%M:%S', time.gmtime())
        if ctx.invoked_subcommand is None:
                for p in parsed['fleet']:
                    ordname = p['order']
                    if ordname == 'indorder':
                        members = ', '.join(map(str,p['members']))
                        indorder.append(members)
                        indtz = p['tzname']
                        indutc = datetime.strptime(p['utctime'],'%H:%M:%S') - datetime.strptime(current_time,'%H:%M:%S')
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            indpayout = ' :moneybag:'
                        else:
                            indpayout = ' - :clock130: ' + str(indutc)
                    if ordname == 'taiorder':
                        members = ', '.join(map(str,p['members']))
                        taiorder.append(members)
                        taitz = p['tzname']
                        taiutc = datetime.strptime(p['utctime'],'%H:%M:%S') - datetime.strptime(current_time,'%H:%M:%S')
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            taipayout = ' :moneybag:'
                        else:
                            taipayout = ' - :clock130: ' + str(taiutc)
                    if ordname == 'saorder':
                        members = ', '.join(map(str,p['members']))
                        saorder.append(members)
                        satz = p['tzname']
                        sautc = datetime.strptime(p['utctime'],'%H:%M:%S') - datetime.strptime(current_time,'%H:%M:%S')
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            sapayout = ' :moneybag:'
                        else:
                            sapayout = ' - :clock130: ' + str(sautc)
                    elif ordname == 'euorder':
                        members = ', '.join(map(str,p['members']))
                        euorder.append(members)
                        eutz = p['tzname']
                        euutc = datetime.strptime(p['utctime'],'%H:%M:%S') - datetime.strptime(current_time,'%H:%M:%S')
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            eupayout = ' :moneybag:'
                        else:
                            eupayout = ' - :clock130: ' + str(euutc)           
                    elif ordname == 'estorder':
                        members = ', '.join(map(str,p['members']))
                        estorder.append(members)
                        esttz = p['tzname']
                        estutc = (datetime.strptime(p['utctime'],'%H:%M:%S')+ timedelta(days=1))  - datetime.strptime(current_time,'%H:%M:%S')  
                        if datetime.strptime(p['utctime'],'%H:%M:%S') > datetime.strptime(current_time,'%H:%M:%S'):
                            estpayout = ' :moneybag:'
                        else:
                            estpayout = ' - :clock130: ' + str(estutc)                      
                    elif ordname == 'cstorder':
                        members = ', '.join(map(str,p['members']))
                        cstorder.append(members)
                        csttz = p['tzname']
                        cstutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S')-timedelta(hours=5))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') - timedelta(hours=1) < datetime.strptime(current_time,'%H:%M:%S'):
                            cstpayout = ' :moneybag:'
                        else:
                            cstpayout = ' - :clock130: ' + str(cstutc)
                    elif ordname == 'mstorder':
                        members = ', '.join(map(str,p['members']))
                        mstorder.append(members)
                        msttz = p['tzname']
                        mstutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S')-timedelta(hours=5))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') - timedelta(hours=2) < datetime.strptime(current_time,'%H:%M:%S'):
                            mstpayout = ' :moneybag:'
                        else:
                            mstpayout = ' - :clock130: ' + str(mstutc)  
                    elif ordname == 'akorder':
                        members = ', '.join(map(str,p['members']))
                        akorder.append(members)
                        aktz = p['tzname']
                        akutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S')-timedelta(hours=5))
                        if (datetime.strptime(p['utctime'],'%H:%M:%S')  - timedelta(hours=5)) < datetime.strptime(current_time,'%H:%M:%S'):
                            akpayout = ' :moneybag:'
                        else:
                            akpayout = ' - :clock130: ' + str(akutc)                    
                    elif ordname == 'pstorder':
                        members = ', '.join(map(str,p['members']))
                        pstorder.append(members)
                        psttz = p['tzname']
                        pstutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S')-timedelta(hours=5))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') - timedelta(hours=3) < datetime.strptime(current_time,'%H:%M:%S'):
                            pstpayout = ' :moneybag:'
                        else:
                            pstpayout = ' - :clock130: ' + str(pstutc)

                await self.bot.say("Payout list:\n" +
                    indtz + " - "+ ', '.join(indorder) + str(indpayout) +"\n"+
                    taitz + " - "+ ', '.join(taiorder) + str(taipayout) +"\n"+
                    satz + " - "+ ', '.join(saorder) + str(sapayout) +"\n"+
                    eutz + " - "+ ', '.join(euorder) + str(eupayout) +"\n"+
                    esttz + " - "+ ', '.join(estorder) + str(estpayout) +"\n"+
                    csttz + " - "+ ', '.join(cstorder) + str(cstpayout) +"\n"+
                    msttz + " - "+ ', '.join(mstorder) + str(mstpayout) +"\n"+
                    psttz + " - "+ ', '.join(pstorder) + str(pstpayout)+ "\n"+
                    aktz + " - "+ ', '.join(akorder) + str(akpayout) +"\n")
        await send_cmd_help(ctx)

    @ships.command(pass_context=True, name='add')    
    async def _ships_add(self,ctx,timezone, *, name):
        '''- Add a person to ships\n
        Valid timezone format gmt+/-#'''
        with open('cogs/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        log = logging.getLogger("red.testcog")
        log.setLevel(logging.INFO)
        person = name
        tz = timezone.upper()
        for p in parsed['fleet']:
            if tz == p['tzname'] and person in p['members']:
                await self.bot.say("User already in payout")
            elif tz == p['tzname'] and person not in p['members']:
                p['members'].append(person)
                await self.bot.say(str(person) +" added to "+ tz + " payout")
            elif tz != p['tzname']:
                log.debug("Timezone doesn't match")
            else:
                await self.bot.say("Something went wrong...blame Atreyu")
        with open('cogs/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
    
    @ships.command(pass_context=True, name='remove')    
    async def _ships_remove(self,ctx,timezone, *, name):
        '''- Remove a person from a payout\n
        Valid timezone format gmt+/-#'''
        with open('cogs/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        log = logging.getLogger("red.testcog")
        log.setLevel(logging.INFO)
        person = name
        tz = timezone.upper()
        for p in parsed['fleet']:
            if tz == p['tzname'] and person not in p['members']:
                await self.bot.say("User not in payout")
            elif tz == p['tzname'] and person in p['members']:
                p['members'].remove(person)
                await self.bot.say(str(person) +" removed from "+ tz + " payout")
            elif tz != p['tzname']:
                log.debug("Timezone doesn't match")
            else:
                await self.bot.say("Something went wrong...blame Atreyu")
        with open('cogs/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
            
    @commands.command(pass_context=True)
    async def starfleet(self, ctx):
        '''Payout list for ships arena'''
        self.today = date.today()
        starfleet = open('cogs/starships-gmt+2.txt', 'r')
        
        starorder = []

        
        if ctx.invoked_subcommand is None:
            for starline in starfleet:
                starorder.append(starline.strip()) 
            starfleet.close()
           
            
            await self.bot.say("Payout order for "+ str(self.today)+":\n" +
                               ', '.join(starorder))
                  
                               
    @commands.command(pass_context=True)
    async def starfleet_rotate(self):
        starfile = open('cogs/starships-gmt+2.txt', 'r')
        starlist = []
        
        for starname in starfile:
            starlist.append(starname.strip())
        starlist.insert(0, starlist.pop())
        starfile.close()
        
        writestar_file = open('cogs/starships-gmt+2.txt','w')
        for item in starlist:
            writestar_file.write('%s\n' % item)
        writestar_file.close()
        
        
def setup(bot):
    bot.add_cog(shipscog(bot))