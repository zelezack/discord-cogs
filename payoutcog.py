import discord
from discord.ext import commands
from __main__ import send_cmd_help

class payoutcog:
    """Discord cog for shard chats"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def payout(self, ctx):
        '''Payout list for squad arena'''
        ru = open('cogs/payouts-gmt+3.txt', 'r')
        eu = open('cogs/payouts-gmt+1.txt', 'r')
        uk = open('cogs/payouts-gmt.txt', 'r')
        est = open('cogs/payouts-gmt-5.txt', 'r')
        cst = open('cogs/payouts-gmt-6.txt', 'r')
        ruorder = []
        euorder = []
        ukorder = []
        estorder = []
        cstorder = []
        if ctx.invoked_subcommand is None:
            for ruline in ru:
                ruorder.append(ruline.strip())
            for euline in eu:
                euorder.append(euline.strip())
            for ukline in uk:
                ukorder.append(ukline.strip())
            for estline in est:
                estorder.append(estline.strip())
            for cstline in cst:
                cstorder.append(cstline.strip())
            ru.close()
            eu.close()
            uk.close()
            est.close()
            cst.close()
            await self.bot.say("Payout list: \n" +
                               ', '.join(ruorder) + " - GMT+3\n"+
                               ', '.join(euorder) + " - GMT+1\n"+
                               ', '.join(ukorder) + " - GMT\n"+
                               ', '.join(estorder) + " - GMT-5\n"+
                               ', '.join(cstorder) + " - GMT-6\n")
            await send_cmd_help(ctx)
            
    @payout.command(pass_context=True, name="add")
    async def _payout_add(self, ctx, timezone, *, name): 
        '''Add a person to a payout\n
        Valid timezone format gmt+/-#'''
        timezone_name = timezone.lower()
        person = name
        
        timezones = ['gmt+3', 'gmt+1', 'gmt', 'gmt-5','gmt-6','gmt-7','gmt-8']
        
        #Read in the correct payout list and add a user to it
        if timezone_name in timezones:
            payout_file = open('cogs/payouts-'+timezone_name+'.txt', 'r')
            payoutlist = []
            for name in payout_file:
                payoutlist.append(name.strip())
            payout_file.close()
            payoutlist.append(person)
            write_file = open('cogs/payouts-'+timezone_name+'.txt', 'w')
            for item in payoutlist:
                write_file.write('%s\n' % item)
            write_file.close()
        
        await self.bot.say( payoutlist[-1] + ' added to the '+ timezone_name +' payout')    
       
def setup(bot):
    bot.add_cog(payoutcog(bot))