@commands.command(pass_context=True)
    async def rotation(self, ctx):
        image = "pictures/giphy.gif"
        channel = ctx.message.channel
        Payout list for squad arena

        euorder = []
        ukorder = []
        estorder = []
        cstorder = []

        self.today = date.today()
            
        eu = open('cogs/order-eu.txt', 'r')
        uk = open('cogs/order-uk.txt', 'r')
        est = open('cogs/order-est.txt', 'r')
        cst = open('cogs/order-cst.txt', 'r')

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
        
        await self.bot.send_file(channel, image)
        await self.bot.say("Rotation list for " + str(self.today) + ':\n' +
                           ':flag_ru: MR: ' + 'Amarey\n' +
                           ':flag_eu: Viva: ' + ', '.join(euorder) + ', LouLou, Alex\n' +
                           ':flag_gb: UK: ' +', '.join(ukorder) + '\n' +
                           ':flag_us: EST: ' +', '.join(estorder)+ '\n'+
                           ':flag_us: CST: ' + ', '.join(cstorder) + '\n' +
                           ':flag_us: PST: ' + 'Awasa Ba\'hidar\n')

@commands.command(pass_context=True)
    async def newday(self): 
        '''Newday routine to change the payout order'''
    
        eufile = open('cogs/order-eu.txt', 'r')
        ukfile = open('cogs/order-uk.txt', 'r')
        estfile = open('cogs/order-est.txt', 'r')
        cstfile = open('cogs/order-cst.txt', 'r')
        shipfile = open('cogs/order-ships.txt', 'r')
        
        eulist = []
        uklist = []
        estlist = []
        cstlist = []
        shiplist = []
        
        for euname in eufile:
            eulist.append(euname.strip())
        eulist += [eulist.pop(0)]
        eufile.close()
        
        for estname in estfile:
            estlist.append(estname.strip())
        estlist += [estlist.pop(0)]
        estfile.close()
        
        for ukname in ukfile:
            uklist.append(ukname.strip())
        uklist += [uklist.pop(0)]
        ukfile.close()

        for cstname in cstfile:
            cstlist.append(cstname.strip())
        cstlist += [cstlist.pop(0)]
        cstfile.close()
        
        for shipname in shipfile:
            shiplist.append(shipname.strip())
        shiplist += [shiplist.pop(0)]
        shipfile.close() 
        
        writeeu_file = open('cogs/order-eu.txt','w')
        for item in eulist:
            writeeu_file.write('%s\n' % item)
        writeeu_file.close()
        
        writeest_file = open('cogs/order-est.txt','w')
        for item in estlist:
            writeest_file.write('%s\n' % item)
        writeest_file.close()
        
        writeuk_file = open('cogs/order-uk.txt','w')
        for item in uklist:
            writeuk_file.write('%s\n' % item)
        writeuk_file.close()
        
        writecst_file = open('cogs/order-cst.txt','w')
        for item in cstlist:
            writecst_file.write('%s\n' % item)
        writecst_file.close()
        
        writeships_file = open('cogs/order-ships.txt', 'w')
        for item in shiplist:
            writeships_file.write('%s\n' % item)
        writeships_file.close()
        
        await self.bot.say( 'New day routine complete')

    @commands.group(pass_context=True)
    async def payout(self, ctx):
        '''Payout list for squad arena'''
        ru = open('cogs/payouts-gmt+3.txt', 'r')
        eu = open('cogs/payouts-gmt+1.txt', 'r')
        uk = open('cogs/payouts-gmt.txt', 'r')
        est = open('cogs/payouts-gmt-5.txt', 'r')
        cst = open('cogs/payouts-gmt-6.txt', 'r')
        pst = open('cogs/payouts-gmt-8.txt', 'r')
        ruorder = []
        euorder = []
        ukorder = []
        estorder = []
        cstorder = []
        pstorder = []
        
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
            for pstline in pst:
                pstorder.append(pstline.strip())
            ru.close()
            eu.close()
            uk.close()
            est.close()
            cst.close()
            pst.close()
            await self.bot.say("Payout list: \n" +
                               ":flag_ru: GMT+3 - "+ ', '.join(ruorder) + "\n"
                               ":flag_eu: GMT+1 - "+', '.join(euorder) + "\n"
                               ":flag_gb: GMT - "+', '.join(ukorder) + "\n"
                               ":flag_us: GMT-5 - "+', '.join(estorder) +"\n"
                               ":flag_us: GMT-6 - "+', '.join(cstorder) +"\n"
                               ":flag_us: GMT-8 - "+', '.join(pstorder) +"\n")
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

            @commands.group(pass_context=True)
    async def ships(self, ctx):
        '''Payout list for ships arena'''
        india = open('cogs/ships-gmt+9.txt', 'r')
        sa = open('cogs/ships-gmt+2.txt', 'r')
        tai = open('cogs/ships-gmt+8.txt', 'r')
        eu = open('cogs/ships-gmt+1.txt', 'r')
        pst = open('cogs/ships-gmt-8.txt', 'r')
        est = open('cogs/ships-gmt-5.txt', 'r')
        mst = open('cogs/ships-gmt-7.txt', 'r')
        cst = open('cogs/ships-gmt-6.txt', 'r')
        ak = open('cogs/ships-gmt-9.txt', 'r')
        
        indorder = []
        taiorder = []
        saorder =[]
        euorder = []
        pstorder = []
        estorder = []
        cstorder = []
        mstorder = []
        akorder = []
        
        if ctx.invoked_subcommand is None:
            for indline in india:
                indorder.append(indline.strip())
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
            for akline in ak:
                akorder.append(akline.strip())
            for tailine in tai:
                taiorder.append(tailine.strip())

            india.close()
            sa.close()
            eu.close()
            pst.close()
            est.close()
            cst.close()
            mst.close()
            ak.close()
            tai.close()
            
            await self.bot.say("Payout list: \n" +
                               'GMT+9 - '+', '.join(sorted(indorder)) + "\n"+
                               'GMT+8 - '+', '.join(sorted(taiorder)) + "\n"+
                               'GMT+2 - '+', '.join(sorted(saorder)) + "\n"+
                               'GMT+1 - '+', '.join(sorted(euorder)) + "\n\n"+
                               'GMT-5 - '+', '.join(sorted(estorder)) + "\n\n"+
                               'GMT-6 - '+', '.join(sorted(cstorder)) + "\n"+
                               'GMT-7 - '+', '.join(sorted(mstorder)) + "\n"+
                               'GMT-8 - '+', '.join(sorted(pstorder)) + "\n"+
                               'GMT-9 - '+', '.join(sorted(akorder)))

    @ships.command(pass_context=True, name="add")
    async def _ships_add(self, ctx, timezone, *, name): 
        '''Add a person to a payout\n
        Valid timezones gmt-/+ #'''
        timezone_name = timezone.lower()
        person = name
        
        timezones = ['gmt+9', 'gmt+8','gmt+2', 'gmt+1', 'gmt-5','gmt-6','gmt-7','gmt-8', 'gmt-9']
        
        #Read in the correct payout list and add a user to it
        if timezone_name in timezones:
            ship_file = open('cogs/ships-'+timezone_name+'.txt', 'r')
            shiplist = []
            for name in ship_file:
                shiplist.append(name.strip())
            ship_file.close()
            shiplist.append(person)
            write_file = open('cogs/ships-'+timezone_name+'.txt', 'w')
            for item in shiplist:
                write_file.write('%s\n' % item)
            write_file.close()
        
        await self.bot.say(shiplist[-1] + ' added to the '+ timezone_name +' payout')