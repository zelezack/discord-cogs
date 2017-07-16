import discord
from discord.ext import commands
from __main__ import send_cmd_help

class shitlistcog:
    """Discord cog for shard chats"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def shitlist(self, ctx):
        '''The ever growing shitlist'''
        shitfile = open('cogs/shitfile.txt', 'r')
        shitorder = []
        if ctx.invoked_subcommand is None:
            for shitline in shitfile:
                shitorder.append(shitline.strip())
            await self.bot.say("Current shitlist: \n" + ', '.join(shitorder))
            await send_cmd_help(ctx)
            shitfile.close()
        
    @shitlist.command(pass_context=True, name="add")
    async def _shitlist_add(self, ctx, name): 
        '''- Add a person to the shitlist '''
        shitlist_name = name
        shitlistorder = []
        shitfile = open('cogs/shitfile.txt', 'r')
        for shit in shitfile:
            shitlistorder.append(shit.strip())
        shitlistorder.append(shitlist_name)
        shitfile.close()
        
        writeshit_file = open('cogs/shitfile.txt','w')
        for item in shitlistorder:
            writeshit_file.write('%s\n' % item)
        writeshit_file.close()
        
        await self.bot.say( name + ' added to the shitlist')
        
    @shitlist.command(pass_context=True, name="remove")
    async def _shitlist_remove(self, ctx, name): 
        '''- Remove a person from the shitlist '''
        shitlist_name = name
        shitlistorder = []
        shitfile = open('cogs/shitfile.txt', 'r')
        for shit in shitfile:
            shitlistorder.append(shit.strip())
        shitlistorder.remove(shitlist_name)
        shitfile.close()
        
        writeshit_file = open('cogs/shitfile.txt','w')
        for item in shitlistorder:
            writeshit_file.write('%s\n' % item)
        writeshit_file.close()
        
        await self.bot.say( name + ' removed from the shitlist')


    @shitlist.command(pass_context=True, name="choochoo")
    async def _shitlist_choochoo(self, ctx, name):
        ''' - Send out an alert for shitlist express'''
        shitname = name
        choochoo = "pictures/choochoo.gif"
        channel = ctx.message.channel
        
        await self.bot.send_file(channel, choochoo)
        await self.bot.say("@here " + shitname + " needs a ride on the shitlist express")
        
def setup(bot):
    bot.add_cog(shitlistcog(bot))