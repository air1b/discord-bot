import discord

# Instance du client 
client = discord.Client()
i=0

# decorateur depend de l'instance 
@client.event
async def on_ready():
    print("Le bot est pret.") # pret a executer des commandes sur le server
    

@client.event
async def on_message(message):
    global i
    if i == 0:
        await message.channel.send("Hello World!")
        i=1
    if message.content.lower() == 'ping':
        await message.channel.send("pong")


client.run("OTM1NTU3Mjc5Mjk2NjYzNjQy.YfAXnQ.7U7lHl_RDGfzKC2aOItP9ASD4tg")
