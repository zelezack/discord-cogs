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
        utcp11 = []
        utcp10 = []
        utcp9 = []
        utcp8 = []
        utcp7 = []
        utcp6 = []
        utcp5 = []
        utcp4 = []
        utcp3 = []
        utcp2 = []
        utcp1 = []
        utc = []
        utcm1 = []
        utcm2 = []
        utcm3 = []
        utcm4 = []
        utcm5 = []
        utcm6 = []
        utcm7 = []
        utcm8 = []
        utcm9 = []
        utcm10 = []
        utcm11 = []

        self.today = date.today()
        servertime = datetime.utcnow() + timedelta(hours=-4)
        current_time = datetime.strftime(servertime, '%H:%M:%S')
        add_a_day = datetime.utcnow() + timedelta(hours=-4)
        plus_day = datetime.strftime(add_a_day, '%H:%M:%S')

        if ctx.invoked_subcommand is None:
                for p in parsed['newsquad']:
                    ordname = p['order']
                    if ordname == 'utcp11':
                        members = ', '.join(map(str,p['members']))
                        utcp11.append(members)
                        utcp11flag = p['flag']
                        utcp11tz = p['tzname']
                        utcp11utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp11payout = ' :moneybag:'
                        else:
                            utcp11payout = ' - :clock130: ' + str(utcp11utc)
                            
                    if ordname == 'utcp10':
                        members = ', '.join(map(str,p['members']))
                        utcp10.append(members)
                        utcp10flag = p['flag']
                        utcp10tz = p['tzname']
                        utcp10utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp10payout = ' :moneybag:'
                        else:
                            utcp10payout = ' - :clock130: ' + str(utcp10utc)
                            
                    if ordname == 'utcp9':
                        members = ', '.join(map(str,p['members']))
                        utcp9.append(members)
                        utcp9flag = p['flag']
                        utcp9tz = p['tzname']
                        utcp9utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp9payout = ' :moneybag:'
                        else:
                            utcp9payout = ' - :clock130: ' + str(utcp9utc)
                            
                    if ordname == 'utcp8':
                        members = ', '.join(map(str,p['members']))
                        utcp8.append(members)
                        utcp8flag = p['flag']
                        utcp8tz = p['tzname']
                        utcp8utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp8payout = ' :moneybag:'
                        else:
                            utcp8payout = ' - :clock130: ' + str(utcp8utc)
                            
                    if ordname == 'utcp7':
                        members = ', '.join(map(str,p['members']))
                        utcp7.append(members)
                        utcp7flag = p['flag']
                        utcp7tz = p['tzname']
                        utcp7utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp7payout = ' :moneybag:'
                        else:
                            utcp7payout = ' - :clock130: ' + str(utcp7utc)
                            
                    if ordname == 'utcp6':
                        members = ', '.join(map(str,p['members']))
                        utcp6.append(members)
                        utcp6flag = p['flag']
                        utcp6tz = p['tzname']
                        utcp6utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp6payout = ' :moneybag:'
                        else:
                            utcp6payout = ' - :clock130: ' + str(utcp6utc)
                    if ordname == 'utcp5':
                        members = ', '.join(map(str,p['members']))
                        utcp5.append(members)
                        utcp5flag = p['flag']
                        utcp5tz = p['tzname']
                        utcp5utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp5payout = ' :moneybag:'
                        else:
                            utcp5payout = ' - :clock130: ' + str(utcp5utc)
                    if ordname == 'utcp4':
                        members = ', '.join(map(str,p['members']))
                        utcp4.append(members)
                        utcp4flag = p['flag']
                        utcp4tz = p['tzname']
                        utcp4utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp4payout = ' :moneybag:'
                        else:
                            utcp4payout = ' - :clock130: ' + str(utcp4utc)
                    if ordname == 'utcp3':
                        members = ', '.join(map(str,p['members']))
                        utcp3.append(members)
                        utcp3flag = p['flag']
                        utcp3tz = p['tzname']
                        utcp3utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp3payout = ' :moneybag:'
                        else:
                            utcp3payout = ' - :clock130: ' + str(utcp3utc)
                    if ordname == 'utcp2':
                        members = ', '.join(map(str,p['members']))
                        utcp2.append(members)
                        utcp2flag = p['flag']
                        utcp2tz = p['tzname']
                        utcp2utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp2payout = ' :moneybag:'
                        else:
                            utcp2payout = ' - :clock130: ' + str(utcp2utc)
                    if ordname == 'utcp1':
                        members = ', '.join(map(str,p['members']))
                        utcp1.append(members)
                        utcp1flag = p['flag']
                        utcp1tz = p['tzname']
                        utcp1utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcp1payout = ' :moneybag:'
                        else:
                            utcp1payout = ' - :clock130: ' + str(utcp1utc)
                    if ordname == 'utc':
                        members = ', '.join(map(str,p['members']))
                        utc.append(members)
                        utcflag = p['flag']
                        utctz = p['tzname']
                        utcutc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcpayout = ' :moneybag:'
                        else:
                            utcpayout = ' - :clock130: ' + str(utcutc)
#=============================================================================================================================
                    if ordname == 'utcm11':
                        members = ', '.join(map(str,p['members']))
                        utcm11.append(members)
                        utcm11flag = p['flag']
                        utcm11tz = p['tzname']
                        utctime = p['utctime']
                        newtime = datetime.strptime(utctime, '%H:%M:%S')+ timedelta(hours=24)
                        newpayouttime = datetime.strftime(newtime, '%H:%M:%S')
                        utcm11utc = datetime.strptime(newpayouttime,'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strftime(newtime,'%H:%M:%S') < datetime.strftime(servertime,'%H:%M:%S'):
                            
                            utcm11payout = ' - :clock130: ' + str(utcm11utc)
                        else:
                            utcm11payout = ' :moneybag:'
                            
                    if ordname == 'utcm10':
                        members = ', '.join(map(str,p['members']))
                        utcm10.append(members)
                        utcm10flag = p['flag']
                        utcm10tz = p['tzname']
                        utcm10utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm10payout = ' :moneybag:'
                        else:
                            utcm10payout = ' - :clock130: ' + str(utcm10utc)
                            
                    if ordname == 'utcm9':
                        members = ', '.join(map(str,p['members']))
                        utcm9.append(members)
                        utcm9flag = p['flag']
                        utcm9tz = p['tzname']
                        utcm9utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm9payout = ' :moneybag:'
                        else:
                            utcm9payout = ' - :clock130: ' + str(utcm9utc)
                            
                    if ordname == 'utcm8':
                        members = ', '.join(map(str,p['members']))
                        utcm8.append(members)
                        utcm8flag = p['flag']
                        utcm8tz = p['tzname']
                        utcm8utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm8payout = ' :moneybag:'
                        else:
                            utcm8payout = ' - :clock130: ' + str(utcm8utc)
                            
                    if ordname == 'utcm7':
                        members = ', '.join(map(str,p['members']))
                        utcm7.append(members)
                        utcm7flag = p['flag']
                        utcm7tz = p['tzname']
                        utcm7utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm7payout = ' :moneybag:'
                        else:
                            utcm7payout = ' - :clock130: ' + str(utcm7utc)
                            
                    if ordname == 'utcm6':
                        members = ', '.join(map(str,p['members']))
                        utcm6.append(members)
                        utcm6flag = p['flag']
                        utcm6tz = p['tzname']
                        utcm6utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm6payout = ' :moneybag:'
                        else:
                            utcm6payout = ' - :clock130: ' + str(utcm6utc)
                    if ordname == 'utcm5':
                        members = ', '.join(map(str,p['members']))
                        utcm5.append(members)
                        utcm5flag = p['flag']
                        utcm5tz = p['tzname']
                        utcm5utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm5payout = ' :moneybag:'
                        else:
                            utcm5payout = ' - :clock130: ' + str(utcm5utc)
                    if ordname == 'utcm4':
                        members = ', '.join(map(str,p['members']))
                        utcm4.append(members)
                        utcm4flag = p['flag']
                        utcm4tz = p['tzname']
                        utcm4utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm4payout = ' :moneybag:'
                        else:
                            utcm4payout = ' - :clock130: ' + str(utcm4utc)
                    if ordname == 'utcm3':
                        members = ', '.join(map(str,p['members']))
                        utcm3.append(members)
                        utcm3flag = p['flag']
                        utcm3tz = p['tzname']
                        utcm3utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm3payout = ' :moneybag:'
                        else:
                            utcm3payout = ' - :clock130: ' + str(utcm3utc)
                    if ordname == 'utcm2':
                        members = ', '.join(map(str,p['members']))
                        utcm2.append(members)
                        utcm2flag = p['flag']
                        utcm2tz = p['tzname']
                        utcm2utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm2payout = ' :moneybag:'
                        else:
                            utcm2payout = ' - :clock130: ' + str(utcm2utc)
                    if ordname == 'utcm1':
                        members = ', '.join(map(str,p['members']))
                        utcm1.append(members)
                        utcm1flag = p['flag']
                        utcm1tz = p['tzname']
                        utcm1utc = datetime.strptime(p['utctime'],'%H:%M:%S') - (datetime.strptime(current_time,'%H:%M:%S'))
                        if datetime.strptime(p['utctime'],'%H:%M:%S') < datetime.strptime(current_time,'%H:%M:%S'):
                            utcm1payout = ' :moneybag:'
                        else:
                            utcm1payout = ' - :clock130: ' + str(utcm1utc)

                await self.bot.say("Payout list:\n" +
                    utcp11flag + utcp11tz + " - " + ', '.join(utcp11) + str(utcp11payout) +"\n"+
                    #utcp10flag + utcp10z + " - " + ', '.join(utcp10) + str(utcp10payout) +"\n"+
                    #utcp9flag + utcp9tz + " - " + ', '.join(utcp9) + str(utcp9payout) +"\n"+
                    utcp8flag + utcp8tz + " - " + ', '.join(utcp8) + str(utcp8payout) +"\n"+
                    utcp7flag + utcp7tz + " - " + ', '.join(utcp7) + str(utcp7payout) +"\n"+
                    utcp6flag + utcp6tz + " - " + ', '.join(utcp6) + str(utcp6payout) +"\n"+
                    utcp5flag + utcp5tz + " - " + ', '.join(utcp5) + str(utcp5payout) +"\n"+
                    utcp4flag + utcp4tz + " - " + ', '.join(utcp4) + str(utcp4payout) +"\n"+
                    utcp3flag + utcp3tz + " - " + ', '.join(utcp3) + str(utcp3payout) +"\n"+
                    utcp2flag + utcp2tz + " - " + ', '.join(utcp2) + str(utcp2payout) +"\n"+
                    utcp1flag + utcp1tz + " - " + ', '.join(utcp1) + str(utcp1payout) +"\n"+
                    utcflag + utctz + " - " + ', '.join(utc) + str(utcpayout) +"\n"+
                    utcm1flag + utcm1tz + " - " + ', '.join(utcm1) + str(utcm1payout) +"\n"+
                    utcm2flag + utcm2tz + " - " + ', '.join(utcm2) + str(utcm2payout) +"\n"+
                    utcm3flag + utcm3tz + " - " + ', '.join(utcm3) + str(utcm3payout) +"\n"+
                    utcm4flag + utcm4tz + " - " + ', '.join(utcm4) + str(utcm4payout) +"\n"+
                    utcm5flag + utcm5tz + " - " + ', '.join(utcm5) + str(utcm5payout) +"\n"+
                    utcm6flag + utcm6tz + " - " + ', '.join(utcm6) + str(utcm6payout) +"\n"+
                    utcm7flag + utcm7tz + " - " + ', '.join(utcm7) + str(utcm7payout) +"\n"+
                    utcm8flag + utcm8tz + " - " + ', '.join(utcm8) + str(utcm8payout) +"\n"+
                    utcm9flag + utcm9tz + " - " + ', '.join(utcm9) + str(utcm9payout) +"\n"+
                    utcm10flag + utcm10tz + " - " + ', '.join(utcm10) + str(utcm10payout) +"\n"+
                    utcm11flag + utcm11tz + " - " + ', '.join(utcm11) + str(utcm11payout) +"\n"
                    )
        await send_cmd_help(ctx)
            
    @payout.command(pass_context=True, name='add')    
    async def _payout_add(self,ctx,timezone, *, name):
        '''- Add a person to a payout\n
        Valid timezone format utc+/-#'''
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
        Valid timezone format utc+/-#'''
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
