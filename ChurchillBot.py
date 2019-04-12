# ChurchillBot by Rainverm38
# More info can be found on the GitHub here: https://github.com/Rainverm38/ChurchillBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                       # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
#import time                                # Doesn't appear to be working here, must be imported before the command that requires it is run.

# Checks time that bot was started
startTime = DT.datetime.now()

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Notify in console when bot is loaded and sets bot currently playing status
@bot.event
async def on_ready():
    endTime = DT.datetime.now()
    await bot.change_presence(game=discord.Game(name='Pwning Hitler'))   # Sets the bot's presence
    print('--------------------------')
    timeToLoad = endTime - startTime
    currentDT = DT.datetime.now()               # Gets current time
    print('Time to load:', timeToLoad)          # Prints the time to load
    print('Current Time:', currentDT)           # Prints current time in console
    print('Done Loading!')                      # Prints 'Done Loading!' in console
    print('--------------------------')

    bot.run('TOKEN HERE')         # User defined bot token