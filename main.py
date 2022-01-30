import discord
import re
from discord.ext import commands
from webserver import keep_alive
import os
import random
from dotenv import load_dotenv
import requests
from io import StringIO
load_dotenv(dotenv_path="config")

phrases = [
          'Comment allez vous ?',
            'Alors on ne dit pas bonjour a son vieux pote ?',
              'On se connait',
                'J\'ai acheter hier la switch un delice',
                  'C\'est amusant',
                    'On se capte quand tu veux sinon',
                      'Aller je vous laisse',
                        'Bye'
                        ]

client = commands.Bot (command_prefix = "!")
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is currently online!")

@client.event
async def on_message(message):
    if message.content == 'hey':
        r = requests.get("http://10.0.0.6:9000/test")
        print(r.json())
        await message.channel.send(r.json())
        #await message.channel.send(random.choice(phrases))
                      
    for guild in client.guilds:
        for member in guild.members:
            print(member)
                                              #print(client.get_guild(935507531638382642))
                                                # await client.send_message("Hello world !")


keep_alive()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
