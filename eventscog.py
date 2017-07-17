import discord
import datetime
from discord.ext import commands

class eventscog():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)    
    async def eventcreate(self, ctx, name, date, time):
        '''Used to create an event\n 
        Date format - YYYYMMDD\n
        Time format - 24hour HHMM'''
        event_name = name
        event_date = datetime.datetime.strptime(date, "%Y%m%d").date()
        event_time = datetime.datetime.strptime(time, "%H%M").time()

        urldate = str(datetime.datetime.strptime(date, "%Y%m%d").date()).replace("-", "")
        
        new_event = {
            
            "event_name": event_name,
            "event_start_date": event_date,
            "event_start_time": event_time,
            "description": event_name+ " FFA"
        }
        
        emb = discord.Embed(title=new_event["event_name"],
                            description=new_event["description"],
                            url="https://www.timeanddate.com/countdown/generic?iso="+urldate+"T"+time+"&p0=1440+&msg="+name+"&font=cursive"
                            )
        emb.add_field(name="Start Date", value=(new_event["event_start_date"]))
        emb.add_field(name="Start Time", value=(new_event["event_start_time"]))
        await self.bot.say("<Disabled @ everyone for testing> A new raid has been launched")
        await self.bot.say(embed=emb)
    
        
def setup(bot):
    bot.add_cog(eventscog(bot))