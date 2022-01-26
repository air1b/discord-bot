import os

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

# Recuperation des intents
default_intents = discord.Intents.default()
default_intents.members = True

# i - creation du client
## Instance du client 
## + passe en argument les intents du bot
client = discord.Client(intents=default_intents)

# decorateur depend de l'instance 
@client.event
async def on_ready():
    print("Le bot est pret.") # pret a executer des commandes sur le server
    
@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(935507531638382646)
    await general_channel.send(content=f"Bienvenue sur le server {member.display_name} !")

@client.event
async def on_message(message):
    if message.content.lower() == 'ping':
        await message.channel.send("pong")
    if message.content.startswith("!del"):
        number = int (message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        
        for each_message in messages:
            await each_message.delete()

client.run(os.getenv("TOKEN"))
