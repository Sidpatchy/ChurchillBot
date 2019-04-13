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

# Adds a help command that sends a message to the user rather than spamming the chat channel
@bot.command(pass_context=True)
async def help(ctx):
    currentDT = DT.datetime.now()
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    embed.set_author(name='Help')
    embed.add_field(name='!info', value='Gives some information about the bot', inline=False)
    embed.add_field(name='!canihastenk', value='Doesn\'t even consider giving the user a tenk', inline=False)
    embed.add_field(name='!pleasecanihastenk', value='Gives the user a tenk since they asked so nicely', inline=False)
    embed.add_field(name='!moretanks', value='Fetches more tanks for the war effort', inline=False)
    embed.add_field(name='!democracy', value='States what Churchill thought about democracy (A message from the author: What he said is fact, anyone who says otherwise can bugger off)')
    embed.add_field(name='fightwhere', value='Says where we will fight', inline=False)
    await bot.send_message(author, embed=embed)
    print('--------------------------')
    print('Current Time:', currentDT)
    print('Help has been run')
    print('--------------------------')

# 'Info' command
@bot.command(pass_context=True)
async def info(ctx):
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('Rainverm38 noticed that the choices for bots dedicated to former British Prime Minister Winston Churchill was empty.') 
    print('--------------------------')
    print('Current Time:', currentDT)
    print('info has been run')
    print('--------------------------')

# 'Can I has Tenk' command
@bot.command(pass_context=True)
async def canihastenk(ctx):
    currentDT = DT.datetime.now()
    await bot.say('No, say please and maybe my answer will change')
    print('')
    print('--------------------------')
    print('Current Time:', currentDT)
    print('canihastenk has been run')
    print('--------------------------')

# 'Please Can I has Tenk' command
@bot.command(pass_context=True)
async def pleasecanihastenk(ctx):
    currentDT = DT.datetime.now()
    await bot.say('Thank you for asking so nicely, yes you may has tenk.')
    await bot.say('https://i.imgur.com/a9GfFqO.jpg')
    print('')
    print('--------------------------')
    print('Current Time:', currentDT)
    print('pleasecanihastenk has been run')
    print('--------------------------')

# 'More tanks' command
@bot.command(pass_context=True)
async def moretanks(ctx):
    currentDT = DT.datetime.now()
    await bot.say('Getting more tanks stat!')
    await bot.say('https://media.giphy.com/media/VFZR04kiwRtbZcMjAH/giphy.gif')
    print('')
    print('--------------------------')
    print('Current Time:', currentDT)
    print('moretanks has been run')
    print('--------------------------')

# 'Democracy' command
@bot.command(pass_context=True)
async def democracy(ctx):
    currentDT = DT.datetime.now()
    await bot.say('Democracy is the worst form of government, except for all the others.')
    print('')
    print('--------------------------')
    print('Current Time:', currentDT)
    print('democracy has been run')
    print('--------------------------')

#  'Fight Where?' command
@bot.command(pass_context=True)
async def fightwhere(ctx):
    currentDT = DT.datetime.now()
    await bot.say('WE SHALL FIGHT EVERYWHERE!')
    await bot.say('(I stole this meme from r/HistoryMemes) https://i.imgur.com/O6n5PV9.jpg')
    print('')
    print('--------------------------')
    print('Current Time:', currentDT)
    print('fightwhere has been run')
    print('--------------------------')

bot.run('TOKEN HERE')         # User defined bot token