import discord
from discord.ext import commands
from __main__ import send_cmd_help

class shipscog:
    """Discord cog for shard chats"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def ships(self, ctx):
        '''Payout list for ships arena'''
        sa = open('cogs/ships-sa.txt', 'r')
        eu = open('cogs/ships-eu.txt', 'r')
        pst = open('cogs/ships-pst.txt', 'r')
        est = open('cogs/ships-est.txt', 'r')
        mst = open('cogs/ships-mst.txt', 'r')
        cst = open('cogs/ships-cst.txt', 'r')
        
        saorder =[]
        euorder = []
        pstorder = []
        estorder = []
        cstorder = []
        mstorder = []
        
        if ctx.invoked_subcommand is None:
            for euline in eu:
                euorder.append(euline.strip())
            for pstline in pst:
                pstorder.append(pstline.strip())
            for estline in est:
                estorder.append(estline.strip())
            for cstline in cst:
                cstorder.append(cstline.strip())
            for mstline in mst:
                mstorder.append(mstline.strip())
            for saline in sa:
                saorder.append(saline.strip())                
            sa.close()
            eu.close()
            pst.close()
            est.close()
            cst.close()
            mst.close()
            
            await self.bot.say("Payout list: \n" +
                               ', '.join(saorder) + " - GMT+2\n"+
                               ', '.join(euorder) + " - GMT+1\n"+
                               ', '.join(estorder) + " - GMT-5\n"+
                               ', '.join(cstorder) + " - GMT-6\n"+
                               ', '.join(mstorder) + " - GMT-7\n"+
                               ', '.join(pstorder) + " - GMT-8\n")

    @ships.command(pass_context=True, name="add")
    async def _ships_add(self, ctx, timezone, name): 
        '''Add a person to a payout\n
        Valid timezones gmt-/+ #'''
        timezone_name = timezone.upper()
        person = name
        
        #Add person to EU order
        if timezone_name == "GMT+1":
            eufile = open('cogs/ships-eu.txt', 'r')
            eulist = []
            for euname in eufile:
                eulist.append(euname.strip())
            eulist.append(person)
            eufile.close()
            
            writeeu_file = open('cogs/ships-eu.txt','w')
            for item in eulist:
                writeeu_file.write('%s\n' % item)
            writeeu_file.close()
            
            await self.bot.say( name + ' added to the GMT+1 payout')
        
        #Add person to UK order
        elif timezone_name == "GMT-8":
            pstfile = open('cogs/ships-pst.txt', 'r')
            pstlist = []
            for pstname in pstfile:
                pstlist.append(pstname.strip())
            pstlist.append(person)
            pstfile.close()
            
            writepst_file = open('cogs/ships-pst.txt','w')
            for item in pstlist:
                writepst_file.write('%s\n' % item)
            writepst_file.close()
            
            await self.bot.say( name + ' added to the GMT-8 payout')
        
        #Add person to EST order
        elif timezone_name == "GMT-5":
            estfile = open('cogs/ships-est.txt', 'r')
            estlist = []
            for estname in estfile:
                estlist.append(estname.strip())
            estlist.append(person)
            estfile.close()
            
            writeest_file = open('cogs/ships-est.txt','w')
            for item in estlist:
                writeest_file.write('%s\n' % item)
            writeest_file.close()
            
            await self.bot.say( name + ' added to the GMT-5 payout')

        #Add person to CST order
        elif timezone_name == "GMT-6":
            cstfile = open('cogs/ships-cst.txt', 'r')
            cstlist = []
            for cstname in cstfile:
                cstlist.append(cstname.strip())
            cstlist.append(person)
            cstfile.close()
            writecst_file = open('cogs/ships-cst.txt','w')
            for item in cstlist:
                writecst_file.write('%s\n' % item)
            writecst_file.close()
            
            await self.bot.say( name + ' added to the GMT-6 payout')
            
        #Add person to MST order
        elif timezone_name == "GMT-7":
            mstfile = open('cogs/ships-mst.txt', 'r')
            mstlist = []
            for mstname in mstfile:
                mstlist.append(mstname.strip())
            mstlist.append(person)
            mstfile.close()
            writemst_file = open('cogs/ships-mst.txt','w')
            for item in mstlist:
                writemst_file.write('%s\n' % item)
            writemst_file.close()
            
            await self.bot.say( name + ' added to the GMT-7 payout')
        
def setup(bot):
    bot.add_cog(shipscog(bot))