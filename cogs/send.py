###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# imports and stuff
from distutils.fancy_getopt import FancyGetopt
import disnake
from disnake.ext import commands
import os
from datetime import datetime
import random
import config
from helpers import errors

class send(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Send')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            channel = self.bot.get_channel(config.send_channel) 
            await channel.send(f"{member.mention}", delete_after=0.2)
        except Exception as e:
            print(f'Error sending welcome message: {e}')

def setup(bot):
    bot.add_cog(send(bot))