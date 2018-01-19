import discord
import json
from discord.ext import commands
from __main__ import send_cmd_help

import logging

class shitlistcog:
    """Discord cog for shard chats"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def shitlist(self, ctx):
        '''The ever growing shitlist'''
        with open('cogs/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        shitorder = []
        if ctx.invoked_subcommand is None:
                for p in parsed['shitlist']:
                    members = ', '.join(map(str,p['members']))
                    shitorder.append(members)
                await self.bot.say("Current shitlist: \n" + ', '.join(shitorder))
                await send_cmd_help(ctx)

    @shitlist.command(pass_context=True, name='add')    
    async def _shitlist_add(self,ctx, *, name):
        '''- Add a person to the shitlist'''
        with open('cogs/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        log = logging.getLogger("red.testcog")
        log.setLevel(logging.INFO)
        person = name
        for p in parsed['shitlist']:
            if  person in p['members']:
                await self.bot.say("User already on the shitlist")
            elif person not in p['members']:
                p['members'].append(person)
                await self.bot.say(str(person) +" added to the shitlist")
            else:
                await self.bot.say("Something went wrong...blame Cherno")
        with open('cogs/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
    
    @shitlist.command(pass_context=True, name='remove')    
    async def _shitlist_remove(self,ctx, *, name):
        '''- Remove a person from the shitlist\n
        Valid timezone format gmt+/-#'''
        with open('cogs/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        log = logging.getLogger("red.testcog")
        log.setLevel(logging.INFO)
        person = name
        for p in parsed['shitlist']:
            if person not in p['members']:
                await self.bot.say("User not on the shitlist")
            elif person in p['members']:
                p['members'].remove(person)
                await self.bot.say(str(person) +" removed from the shitlist")
            elif tz != p['tzname']:
                log.debug("Timezone doesn't match")
            else:
                await self.bot.say("Something went wrong...blame Cherno")
        with open('cogs/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
        
    "==================================================================================================="
    @commands.group(pass_context=True)
    async def hitlist(self, ctx):
        '''The ever growing hitlist'''
        shipshitfile = open('cogs/shipshitfile.txt', 'r')
        shipshitorder = []
        if ctx.invoked_subcommand is None:
            for shipshitline in shipshitfile:
                shipshitorder.append(shipshitline.strip())
            await self.bot.say("Current hitlist: \n" + ', '.join(shipshitorder))
            await send_cmd_help(ctx)
            shipshitfile.close()
        
    @hitlist.command(pass_context=True, name="add")
    async def _hitlist_add(self, ctx, *, name): 
        '''- Add a person to the hitlist '''
        shipshitlist_name = name
        shipshitlistorder = []
        shipshitfile = open('cogs/shipshitfile.txt', 'r')
        for shipshit in shipshitfile:
            shipshitlistorder.append(shipshit.strip())
        shipshitlistorder.append(shipshitlist_name)
        shipshitfile.close()
        
        writeshipshit_file = open('cogs/shipshitfile.txt','w')
        for item in shipshitlistorder:
            writeshipshit_file.write('%s\n' % item)
        writeshipshit_file.close()
        
        await self.bot.say( name + ' added to the hitlist')
        
    @hitlist.command(pass_context=True, name="remove")
    async def _hitlist_remove(self, ctx, *, name): 
        '''- Remove a person from the hitlist '''
        shipshitlist_name = name
        shipshitlistorder = []
        shipshitfile = open('cogs/shipshitfile.txt', 'r')
        for shit in shipshitfile:
            shipshitlistorder.append(shit.strip())
        shipshitlistorder.remove(shipshitlist_name)
        shipshitfile.close()
        
        writeshipshit_file = open('cogs/shipshitfile.txt','w')
        for item in shipshitlistorder:
            writeshipshit_file.write('%s\n' % item)
        writeshipshit_file.close()
        
        await self.bot.say( name + ' removed from the hitlist')


def setup(bot):
    bot.add_cog(shitlistcog(bot))