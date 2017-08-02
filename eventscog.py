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
        self.events = fileIO('data/eventscog/events.json', 'load')
        self.queue = asyncio.PriorityQueue(loop=self.bot.loop)
        self.queue_lock = asyncio.Lock()
        self.to_kill = {}
        self._load_events()
        self.name = ""

    def save_events(self):
        fileIO('data/eventscog/events.json', 'save', self.events)
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

    async def _remove_event(self, name, server):
        await self.queue_lock.acquire()
        events = []
        while self.queue.qsize() != 0:
            time, event = await self.queue.get()
            if not (name == event.name and server.id == event.server):
                events.append((time, event))

        for event in events:
            await self.queue.put(event)
        self.queue_lock.release()       

    @commands.command(pass_context=True)    
    async def eventcreate(self, ctx, name, date, time):
        '''Used to create an event\n 
        Date format - YYYYMMDD\n
        Time format - 24hour HHMM in GMT'''
        event_name = name
        event_date = datetime.strptime(date, "%Y%m%d").date()
        event_time = datetime.strptime(time, "%H%M").time()
        channel = ctx.message.channel
        server = ctx.message.server
        author = ctx.message.author
        self.name = str(event_name) 

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
        
        one_hour = time_until_raid - 3658
        
        command = str(self.rancor1hr)
        command2 = str(self.rancornow)
        
        event_name2 = str(event_name + "_1hr")
        event_name1 = str(event_name + "_now")
           
        #create embedded notification in Discord
        urldate = str(datetime.strptime(date, "%Y%m%d").date()).replace("-", "")

        emb = discord.Embed(title=new_event["event_name"],
                            description=new_event["description"],
                            url="https://www.timeanddate.com/countdown/generic?iso="+urldate+"T"+time+"&p0=1440+&msg="+name+"&font=cursive&csz=1"
                            )
        emb.add_field(name="Start Date", value=(new_event["event_start_date"]))
        emb.add_field(name="Start Time", value=(new_event["event_start_time"]))
        await self.bot.say("@everyone A new "+self.name+" raid has been launched")
        await self.bot.say(embed=emb)
        

        await self._add_event(event_name2, command, server, channel, author, one_hour)
        #await self.bot.say('I will run "{}" in {}s'.format(command, one_hour))
        #await self._add_event(event_name1, command2, server, channel, author, until_raid)
        #await self.bot.say('I will run "{}" in {}s'.format(command2, time_until_raid))
        
    def run_coro(self, event):
        channel = self.bot.get_channel(event.channel)
        try:
            server = channel.server
            prefix = self.bot.settings.get_prefixes(server)[0]
        except AttributeError:
            log.debug("Channel no longer found, not running scheduled event.")
            return
        data = {}
        data['timestamp'] = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.gmtime())
        data['id'] = randint(10**(17), (10**18) - 1)
        data['content'] = prefix + event.command
        data['channel'] = self.bot.get_channel(event.channel)
        data['author'] = {'id': event.author}
        data['nonce'] = randint(-2**32, (2**32) - 1)
        data['channel_id'] = event.channel
        data['reactions'] = []
        fake_message = discord.Message(**data)
        # coro = self.bot.process_commands(fake_message)
        log.info("Running '{}' in {}".format(event.name, event.server))
        # self.bot.loop.create_task(coro)
        self.bot.dispatch('message', fake_message)

    async def queue_manager(self):
        while self == self.bot.get_cog('eventscog'):
            await self.queue_lock.acquire()
            if self.queue.qsize() != 0:
                curr_time = int(time.time())
                next_tuple = await self.queue.get()
                next_time = next_tuple[0]
                next_event = next_tuple[1]
                diff = next_time - curr_time
                diff = diff if diff >= 0 else 0
                if diff < 30:
                    log.debug('scheduling call of "{}" in {}s'.format(
                        next_event.name, diff))
                    fut = self.bot.loop.call_later(diff, self.run_coro,
                                                   next_event)
                    self.to_kill[next_time] = fut
                    if next_event.repeat:
                        await self._put_event(next_event, next_time,
                                              next_event.timedelta)
                    else:
                        del self.events[next_event.server][next_event.name]
                        self.save_events()
                else:
                    log.debug('Will run {} "{}" in {}s'.format(
                        next_event.name, next_event.command, diff))
                    await self._put_event(next_event, next_time)
            self.queue_lock.release()

            to_delete = []
            for start_time, old_command in self.to_kill.items():
                if time.time() > start_time + 30:
                    old_command.cancel()
                    to_delete.append(start_time)
            for item in to_delete:
                del self.to_kill[item]

            await asyncio.sleep(5)
        log.debug('manager dying')
        while self.queue.qsize() != 0:
            await self.queue.get()
        while len(self.to_kill) != 0:
            curr = self.to_kill.pop()
            curr.cancel()
    
    @commands.command(pass_context=True)
    async def rancor1hr(self, name):
        #await self.bot.say("@everyone "+str(self.event_name) + " FFA starting 1 hour from now")
        await self.bot.say("@everyone "+str(self.name) +" FFA starting 1 hour from now")
        await asyncio.sleep(3600)
        await self.bot.say("@everyone "+str(self.name) + " FFA starts now")
        

    
def check_folder():
    if not os.path.exists('data/eventscog'):
        os.mkdir('data/eventscog') 

def check_files():
    f = 'data/eventscog/events.json'
    if not os.path.exists(f):
        fileIO(f, 'save', {})    
        


        
def setup(bot):
    check_folder()
    check_files()
    n = eventscog(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(n.queue_manager())
    bot.add_cog(n)