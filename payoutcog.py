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
        eu = open('cogs/payouts-eu.txt', 'r')
        uk = open('cogs/payouts-uk.txt', 'r')
        est = open('cogs/payouts-est.txt', 'r')
        cst = open('cogs/payouts-cst.txt', 'r')
        euorder = []
        ukorder = []
        estorder = []
        cstorder = []
        if ctx.invoked_subcommand is None:
            for euline in eu:
                euorder.append(euline.strip())
            for ukline in uk:
                ukorder.append(ukline.strip())
            for estline in est:
                estorder.append(estline.strip())
            for cstline in cst:
                cstorder.append(cstline.strip())
            eu.close()
            uk.close()
            est.close()
            cst.close()
            await self.bot.say("Payout list: \n" + ', '.join(euorder) + " - 1PM EDT, 12PM CDT, 17:00 GMT\n"+
                               ', '.join(ukorder) + " - 2PM EDT, 1PM CDT, 18:00 GMT\n"+
                               ', '.join(estorder) + " - 7PM EDT, 6PM CDT, 23:00 GMT\n"+
                               ', '.join(cstorder) + " - 8PM EDT, 7PM CDT, 24:00 GMT\n")
            await send_cmd_help(ctx)
    @payout.command(pass_context=True, name="add")
    async def _payout_add(self, ctx, timezone, name): 
        '''Add a person to a payout\n
        Valid timezones eu, uk, est, cst'''
        timezone_name = timezone
        person = name
        
        #Add person to EU order
        if timezone_name == "eu":
            eufile = open('cogs/payouts-eu.txt', 'r')
            eulist = []
            for euname in eufile:
                eulist.append(euname.strip())
            eulist.append(person)
            eufile.close()
            
            writeeu_file = open('cogs/payouts-eu.txt','w')
            for item in eulist:
                writeeu_file.write('%s\n' % item)
            writeeu_file.close()
            
            await self.bot.say( name + ' added to the EU payout')
        
        #Add person to UK order
        elif timezone_name == "uk":
            ukfile = open('cogs/payouts-uk.txt', 'r')
            uklist = []
            for ukname in ukfile:
                uklist.append(ukname.strip())
            uklist.append(person)
            ukfile.close()
            
            writeuk_file = open('cogs/payouts-uk.txt','w')
            for item in uklist:
                writeuk_file.write('%s\n' % item)
            writeuk_file.close()
            
            await self.bot.say( name + ' added to the UK payout')
        
        #Add person to EST order
        elif timezone_name == "est":
            estfile = open('cogs/payouts-est.txt', 'r')
            estlist = []
            for estname in estfile:
                estlist.append(estname.strip())
            estlist.append(person)
            estfile.close()
            
            writeest_file = open('cogs/payouts-est.txt','w')
            for item in estlist:
                writeest_file.write('%s\n' % item)
            writeest_file.close()
            
            await self.bot.say( name + ' added to the EST payout')

        #Add person to CST order
        elif timezone_name == "cst":
            cstfile = open('cogs/payouts-cst.txt', 'r')
            cstlist = []
            for cstname in cstfile:
                cstlist.append(cstname.strip())
            cstlist.append(person)
            cstfile.close()
            writecst_file = open('cogs/payouts-cst.txt','w')
            for item in cstlist:
                writecst_file.write('%s\n' % item)
            writecst_file.close()
            
            await self.bot.say( name + ' added to the CST payout')
        
def setup(bot):
    bot.add_cog(payoutcog(bot))