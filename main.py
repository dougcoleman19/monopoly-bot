# Tutorial Bot by RobustOne

import discord
from discord import Embed, Color
from discord.ext import commands
from discord.ext.commands import Bot
import subprocess
import asyncio

from time import gmtime, strftime
import sys

import STATICS
from commands import cmd_new #cmd_help, cmd_roll, cmd_play,

# Create Discord Client
client = discord.Client()

cmdmap = {
            #"help": cmd_help,
            #"roll": cmd_roll,
            #"play": cmd_play,
            "new": cmd_new,
}

# When the bot is started
@client.event
async def on_ready():
    print("\n-----------------------------\n"
            "The Monopoly Bot v.{}\n"
            "Ready to go\n"
    "-----------------------------".format(STATICS.VERSION))
    

@client.event
async def on_message(message):
    if message.content.startswith('!cmd'):
        await client.send_message(message.channel, 'Enter command')
        msg = await client.wait_for_message(author=message.author)
        proc = msg.content
        auth = msg.author

        cmd = cmdmap[proc]

        try:
            await cmd.ex(msg, client)
        except:
            await cmd.ex(msg, client)
            pass
        
        print(strftime("[%Y.%d.%m %H:%M:%S]", gmtime()) + ' [COMMAND] \"' + message.content + ' => '+ msg.content + "\" by " + message.author.name)


    elif message.content.startswith(STATICS.PREFIX) and not message.author == client.user:
        invoke = message.content.split(" ")[0].replace(STATICS.PREFIX, "",1)
        command_string = ""

        cmd = cmdmap[invoke]
      
        try:
            await cmd.ex(message, client)
        except:
            await cmd.ex(message, client)
            pass
    
        print(strftime("[%Y.%d.%m %H:%M:%S]", gmtime()) + ' [COMMAND] \"' + message.content + "\" by " + message.author.name)

client.run(STATICS.TOKEN)