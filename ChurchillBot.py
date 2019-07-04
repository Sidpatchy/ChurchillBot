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

# Handles what needs to be printed in the console
def consoleOutput(commandName, commandTime):    # Defines consoleOutput()
    startTime = commandTime                     # (laziness) passing startTime from the beginning of the command into the function
    timeToRun = DT.datetime.now() - startTime   # Does the calculation for how long it took the command to run
    print('')                                   # Adds a space in the console so everything looks far better
    print('-------ChurchillBot-------')         # Divider to make console readable
    print('Time to Run:', timeToRun)            # Prints how long it took the bot to run the command
    print('Current Time:', DT.datetime.now())   # Prints time command was run in the console, from the variable 'currentDT'
    print(commandName, 'has been run')          # Prints 'test has been run' in console
    print('--------------------------')         # Divider to make console readable

# Notify in console when bot is loaded and sets bot currently playing status
@bot.event
async def on_ready():
    endTime = DT.datetime.now()
    await bot.change_presence(activity=discord.Game(name='Pwning Hitler | !help'))   # Sets the bot's presence
    print('-------ChurchillBot-------')
    timeToLoad = endTime - startTime
    currentDT = DT.datetime.now()                                            # Gets current time
    print('Time to load:', timeToLoad)                                       # Prints the time the bot took to load
    print('Current Time:', currentDT)                                        # Prints current time in console
    print('Done Loading!')                                                   # Prints 'Done Loading!' in console
    print('--------------------------')

# Adds a help command that sends a message to the user rather than spamming the chat channel
@bot.command(pass_context=True)
async def help(ctx):
    startTime = DT.datetime.now()
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
    embed.add_field(name='!fightwhere', value='Says where we will fight', inline=False)
    embed.add_field(name='!birthday', value='States some info about the former Prime Minister\'s birthday')
    await author.send(embed=embed)
    consoleOutput('help', startTime)

# 'Info' command
@bot.command(pass_context=True)
async def info(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Rainverm38 noticed that the market for bots dedicated to former British Prime Minister Winston Churchill was empty.') 
    consoleOutput('info', startTime)

# 'Can I has Tenk' command
@bot.command(pass_context=True)
async def canihastenk(ctx):
    startTime = DT.datetime.now()
    await ctx.send('No, say please and maybe my answer will change')
    consoleOutput('canihadtenk', startTime)

# 'Please Can I has Tenk' command
@bot.command(pass_context=True)
async def pleasecanihastenk(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Thank you for asking so nicely, yes you may has tenk.')
    await ctx.send('https://i.imgur.com/a9GfFqO.jpg')
    consoleOutput('pleasecanihastenk', startTime)

# 'More tanks' command
@bot.command(pass_context=True)
async def moretanks(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Getting more tanks stat!')
    await ctx.send('https://media.giphy.com/media/VFZR04kiwRtbZcMjAH/giphy.gif')
    consoleOutput('moretanks', startTime)

# 'Democracy' command
@bot.command(pass_context=True)
async def democracy(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Democracy is the worst form of government, except for all the others.')
    consoleOutput('democracy', startTime)

#  'Fight Where?' command
@bot.command(pass_context=True)
async def fightwhere(ctx):
    startTime = DT.datetime.now()
    await ctx.send('WE SHALL FIGHT EVERYWHERE!')
    await ctx.send('(I stole this meme from r/HistoryMemes) https://i.imgur.com/O6n5PV9.jpg')
    consoleOutput('fightwhere', startTime)

# Happy Birthday sir Winston Churchill
@bot.command(pass_context=True)
async def birthday(ctx):
    startTime = DT.datetime.now()
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    year = startTime.year
    year2 = year
    time = startTime.replace(year=year, month=11, day=30, hour=0, minute=0, second=0, microsecond=0)
    if DT.datetime.now() >= time:
        year = year + 1
    if DT.datetime.now() <= time:
        year2 = year2 - 1
    rainverm38RolemodelBirthday = startTime.replace(year=year, month=11, day=30, hour=0, minute=0, second=0, microsecond=0)
    age = year2 - 1874
    timeToBirthday = rainverm38RolemodelBirthday - DT.datetime.now()
    embed.set_author(name='Winston Churchill Was born on November 30, 1874')
    embed.add_field(name='He would be:', value=age, inline=False)
    embed.add_field(name='Less than a year until his birthday:', value=timeToBirthday, inline=False)
    await ctx.send(embed=embed)
    consoleOutput('birthday', startTime)

bot.run('INSERT_TOKEN')         # User defined bot token