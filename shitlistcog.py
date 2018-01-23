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
        with open('cogs/assets/payouts.json', 'r') as json_file:
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
        with open('cogs/assets/payouts.json', 'r') as json_file:
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
        with open('cogs/assets/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
    
    @shitlist.command(pass_context=True, name='remove')    
    async def _shitlist_remove(self,ctx, *, name):
        '''- Remove a person from the shitlist\n
        Valid timezone format gmt+/-#'''
        with open('cogs/assets/payouts.json', 'r') as json_file:
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
            else:
                await self.bot.say("Something went wrong...blame Cherno")
        with open('cogs/assets/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
        
    #===================================================================================================
    @commands.group(pass_context=True)
    async def hitlist(self, ctx):
        '''The ever growing shitlist'''
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        shitorder = []
        if ctx.invoked_subcommand is None:
                for p in parsed['fleet-shit']:
                    members = ', '.join(map(str,p['members']))
                    shitorder.append(members)
                await self.bot.say("Current hitlist: \n" + ', '.join(shitorder))
                await send_cmd_help(ctx)

    @hitlist.command(pass_context=True, name='add')    
    async def _hitlist_add(self,ctx, *, name):
        '''- Add a person to the hitlist'''
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        log = logging.getLogger("red.testcog")
        log.setLevel(logging.INFO)
        person = name
        for p in parsed['fleet-shit']:
            if  person in p['members']:
                await self.bot.say("User already on the hitlist")
            elif person not in p['members']:
                p['members'].append(person)
                await self.bot.say(str(person) +" added to the hitlist")
            else:
                await self.bot.say("Something went wrong...blame Atreyu")
        with open('cogs/assets/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)
    
    @hitlist.command(pass_context=True, name='remove')    
    async def _hitlist_remove(self,ctx, *, name):
        '''- Remove a person from the hitlist'''
        with open('cogs/assets/payouts.json', 'r') as json_file:
            parsed = json.load(json_file)
        log = logging.getLogger("red.testcog")
        log.setLevel(logging.INFO)
        person = name
        for p in parsed['fleet-shit']:
            if person not in p['members']:
                await self.bot.say("User not on the hitlist")
            elif person in p['members']:
                p['members'].remove(person)
                await self.bot.say(str(person) +" removed from the hitlist")
            else:
                await self.bot.say("Something went wrong...blame Atreyu")
        with open('cogs/assets/payouts.json', 'w') as json_file:
            json.dump(parsed,json_file, sort_keys= True, indent=4)

def setup(bot):
    bot.add_cog(shitlistcog(bot))