import discord
from datetime import *
from cogs.utils.dataIO import fileIO
from discord.ext import commands
from cogs.utils.chat_formatting import *

import logging
import os
import asyncio
import time
from random import randint
from math import ceil

log = logging.getLogger("red.eventscog")
log.setLevel(logging.INFO)

class Event:
    def __init__(self, data=None):
        self.name = data.pop('name')
        self.channel = data.pop('channel')
        self.server = data.pop('server')
        self.author = data.pop('author')
        self.command = data.pop('command')
        self.timedelta = data.pop('timedelta')
        self.repeat = data.pop('repeat')
        self.starttime = data.pop('starttime', None)

    def __lt__(self, other):
        my_sig = "{}-{}-{}-{}".format(self.timedelta, self.name,
                                      self.starttime, self.channel)
        other_sig = "{}-{}-{}-{}".format(other.timedelta, other.name,
                                         other.starttime, other.channel)
        return hash(my_sig) < hash(other_sig)

class eventscog():
    def __init__(self, bot):
        self.bot = bot
        self.events = fileIO('data/scheduler/events.json', 'load')
        self.queue = asyncio.PriorityQueue(loop=self.bot.loop)
        self.queue_lock = asyncio.Lock()
        self.to_kill = {}
        self._load_events()

    def save_events(self):
        fileIO('data/scheduler/events.json', 'save', self.events)
        log.debug('saved events:\n\t{}'.format(self.events))

    def _load_events(self):
        # for entry in the self.events make an Event
        for server in self.events:
            for name, event in self.events[server].items():
                ret = {}
                ret['server'] = server
                ret.update(event)
                e = Event(ret)
                self.bot.loop.create_task(self._put_event(e))

    async def _put_event(self, event, fut=None, offset=None):
        if fut is None:
            now = int(time.time())
            fut = now + event.timedelta
        if offset:
            fut += offset
        await self.queue.put((fut, event))
        log.debug('Added "{}" to the scheduler queue at {}'.format(event.name,
                                                                   fut))

    async def _add_event(self, name, command, dest_server, dest_channel,
                         author, timedelta, repeat=False):
        if isinstance(dest_server, discord.Server):
            dest_server = dest_server.id
        if isinstance(dest_channel, discord.Channel):
            dest_channel = dest_channel.id
        if isinstance(author, discord.User):
            author = author.id
        
        if dest_server not in self.events:
            self.events[dest_server] = {}

        event_dict = {'name': name,
                      'channel': dest_channel,
                      'author': author,
                      'command': command,
                      'timedelta': timedelta,
                      'repeat': repeat,
                      }
        
        log.debug('event dict:\n\t{}'.format(event_dict))

        now = int(time.time())
        event_dict['starttime'] = now
        self.events[dest_server][name] = event_dict.copy()

        event_dict['server'] = dest_server
        e = Event(event_dict.copy())
        await self._put_event(e)
        self.save_events()

    @commands.command(pass_context=True)    
    async def eventcreate(self, ctx, name, date, time):
        '''Used to create an event\n 
        Date format - YYYYMMDD\n
        Time format - 24hour HHMM'''
        event_name = name
        event_date = datetime.strptime(date, "%Y%m%d").date()
        event_time = datetime.strptime(time, "%H%M").time()
        channel = ctx.message.channel
        server = ctx.message.server
        author = ctx.message.author

        new_event = { 
            "event_name": event_name,
            "event_start_date": event_date,
            "event_start_time": event_time,
            "description": event_name+ " FFA"
        }
        
        
        #Notifications - 1hr and at start
        current_time = datetime.now(timezone.utc).replace(tzinfo=timezone.utc)
        #await self.bot.say(current_time)
        raid_start = datetime.combine(event_date, event_time).replace(tzinfo=timezone.utc)
        #await self.bot.say(raid_start)

        time_until_raid = (raid_start - current_time)
        time_until_raid = time_until_raid.total_seconds()
        time_until_raid = time_until_raid - 480
        
        one_hour = time_until_raid - 3635
        
        command = str(self.rancor1hr)
        command2 = str(self.rancornow)
        
        event_name2 = str(event_name + "_1hr")
            
        #create embedded notification in Discord
        urldate = str(datetime.strptime(date, "%Y%m%d").date()).replace("-", "")

        emb = discord.Embed(title=new_event["event_name"],
                            description=new_event["description"],
                            url="https://www.timeanddate.com/countdown/generic?iso="+urldate+"T"+time+"&p0=1440+&msg="+name+"&font=cursive&csz=1"
                            )
        emb.add_field(name="Start Date", value=(new_event["event_start_date"]))
        emb.add_field(name="Start Time", value=(new_event["event_start_time"]))
        await self.bot.say("@everyone A new raid has been launched")
        await self.bot.say(embed=emb)
        
        await self._add_event(event_name2, command, server, channel, author, one_hour)
        #await self.bot.say('I will run "{}" in {}s'.format(command, one_hour))
        await self._add_event(event_name, command2, server, channel, author, time_until_raid)
        #await self.bot.say('I will run "{}" in {}s'.format(command2, time_until_raid))
        
    @commands.command(pass_context=True)
    async def rancor1hr(self, name):
        #await self.bot.say("@everyone "+str(self.event_name) + " FFA starting 1 hour from now")
        await self.bot.say("@everyone FFA starting 1 hour from now")
        
    @commands.command(pass_context=True)
    async def rancornow(self, name):
        #await self.bot.say("@everyone "+str(self.name) + " FFA starts now")
        await self.bot.say("@everyone FFA starts now")

        
def setup(bot):
    n = eventscog(bot)
    bot.add_cog(n)