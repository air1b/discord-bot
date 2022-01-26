

# CREER UN BOT SUR DISCORD

![Dicord, Bot](https://bots.ondiscord.xyz/favicon/android-chrome-256x256.png)



## SOMMAIRE

## Introduction

   - Pourquoi créer un bot ?
   - La différence entre application et bot
   - Les prérequis

## Créer le bot

   - Création du bot
   - Ajouter le bot à un serveur
   - Connecter le bot

## Réagir à des événements

   - L'événement 'on_ready'
   - Réagir à un message
   - Réagir à l'arrivée d'un membre

## Ajouter des commandes

   - Gérer une commande avec le client
   - Créer une commande avec un bot

## Améliorer notre code   

   - Masquer le Token
   - Créer une classe pour notre bot
   - Aller plus loin

_______

## Introduction

## A.1) A quoi sert un bot discord?

Execute le comportement d'une personne a sa place
Ex: donner un cours de bourse quand une personne le demande.

## A.2) Difference entre bot et application ?

Pour creer un bot il faut: creer une application dans discord ( a l'interieur de de cette app que l'on dev le bot )
infos: 
  - On peut dev une app sans bot.
  - On peut deployer un bot sur different server.
  - Le bot a des droits comme un utilisateur.
  - Le comportements ainsi que les reponses donnes par le bot sont codes au prealables

## A.3) Les prerequis 

  - une application discord
  - un bot 
  - server: dediee ou perso (tout depend des besoins)

techno:

  - python3.8
  - Environnement virtuel
  - discord.py (API de discord)

## Creation d'un bot

## B.1) Creation

Initialisation de notre projet

Creation du dossier
```bash
  mkdir DocBot;cd DocBot
  ```
Installation d'un environnement virtuel
```bash
python3.8 -m venv .env
  ```
Sourcer l'environnement virtuel
```bash
source .env/bin/activate
```
On va pouvoir installer la librairie discord dans cette environnement virtuel
```bash
pip install -U discord.py
```
Verifier que discord a bien ete installer
```bash
pip list
```
## B.2) Ajout du bot

Aller sur le portail de discord > section developer > application et creer une nouvelle application.

Aller sur la parti Bot, ajouter un bot, configurer selon besoin
( verifier si on authorise l'utilisation du bot sur d'autre server )

Ensuite nous allons cliquer sur la parti Oauth2 pour inviter le bot sur notre server
Oauth2 > URL Generator
Cocher bot, et donner les permissions a notre bot soit administratif soit autre.

Copier coller le lien, passer le processus d'ajout, et verifier sur le server la presence du nouveau bot.
Si on va sur les setting du server on pourra voir un role specifique au bot qui lui a ete attribuer, 
celui ci correspond a la partie Oauth2 > URL GENERATOR.

## B.3) connecter le bot

creer un script main.py et l'executer

```python
import discord


client = discord.Client()
client.run("<BOT-KEY-API>")
```
ce code permet de mettre le bot en ligne


## Reagir a des evenements

## C.1) L'evenement on_ready
 
Se connecter est un evenement definit par la methode: on_ready()
en executant cette methode on va pouvoir mettre en ligne notre robot.
[Check ici l'api sur la parti 'event reference' pour plus d'info](https://discordpy.readthedocs.io/en/stable/api.html)
> > Called when the client is done preparing the data received from Discord. Usually after login is successful and the Client.guilds and co. are filled up.

la methode on_ready permet d'ecouter si le bot est pret a executer des commandes.


## C.2) Reagir a un message

on_message() permettra de parser le contenu des messages des 
users sur le server et introduire a partir de conditions
des reponses adapter.
message.channel.send -> permet au bot d'envoyer un messsage.
Dans notre cas present on va inclure async/await pour:
respecter le bonne ordre et permettre a l'application de
ne pas bloquer.

![ping pong bot](https://github.com/air1b/discord-bot/raw/master/assets/gif/discordbot-ping-pong.mp4)

on peut dire a notre robot par ex d'envoyer un message et qu'il
s'autodetruit 5 secondes plus tard

```python
await message.channel.send ("pong", delete_after=5)
```

## C.3) Reagir a l'arrivée d'un membre

Les Intents sont des trackers,
Nous avons configurer ceux la au moment de l'ajout/la creation de notre bot.
On peut par exemple tracker le status de nos utilisateurs a travers:
Member.status ( faire du monitoring pour voir l'etat de l'utilisateur au sein
  de la communaute et effectuer des operations par rapports a ses status. )

Autre exemple:
avec on_member_join() et on_member_remove() on peut savoir quand un utilisateur
a rejoint le server ou quand il a quitter le server.

Pour effectuer ce genre d'operation il faut activer au prealable sur discord
dans la parti bot tous les "intents" du bot.
( intent = intention ).

on va activer le mode developer dans la parti UTILISATEUR 
( et NON PAS SERVER - cette fois ci )
UTILISATEUR > Advanced > DEVELOPER MODE✅

```python
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
```

## Ajouter des commandes

## D.1) Gérer une commande avec le client

Si un user veut supprimer par exemple un de ces messages
on va avoir recours a un type de commande
exemple:
en tapant !del cette commande va detruire les n derniers messages
creons cette commande pour l'utilisateur.


```python
@client.event
async def on_message(message):
      if message.content.startswith("!del"):
        number = int (message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()

        for each_message in messages:
        await each_message.delete()
```

Dans notre cas on devra gerer avec un try/catch les erreurs de ce code:
 - dans le cas ou apres !del on a un string
 - ou un nombre trop important
 - ...

Ces problematiques nous introduit au sujet suivant

## D.2) Creer une commande avec un bot

Dans cette parti nous allons voir la second maniere de faire:

```python
from discord.ext import commands

# prefix pour tout type de commande
bot commands.Bot(command prefix="!")

@bot.event
async def on_ready():
  print("Le bot est prêt")

@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
  messages = await ctx.channel.history(Limit=number_of_messages + 1).flatten()

  for each_message in messages:
    await each_message.delete()

bot.run("Nzg4MDUwjk1MTc5NTc1MzM2.X9d3Bw.tsV-CQYeCa0aD21864a6-XymiEo")
```
l'avantage de cette maniere est le cote pensee du code,
  pour eviter de rentrer dans des complexites.

## Ameliorer notre code

## E.1) Masquer le token

La problematique: ecrire le token dans notre fichier.
si on heberge sur un endroit publique: exemple un repos github ou autre.
tout le monde pourra voir notre token et on mettrai en danger notre server.
pour cela:
on va installer une librairie pythondotenv pour proceder a l'inclusion de notre token
sans mettre en danger notre server.
On va recuperer cette cle depuis un fichier externe a ce script.
ne SURTOUT PAS OUBLIER d'inclure dans .gitignore ce fichier.

```bash
pip install -U python-dotenv
```

checker si l'installation a bien ete faite :

```bash
pip list | grep dotenv
```

ensuite dans notre main.py on va rajouter ces lignes de code:


```python
# on va importer la variable d'environnement 
import os

from dotenv import load_dotenv

# onload le fichier ou se trouve notre token
load_dotenv (dotenv_path="config")

  ...

client.run(os.getenv("TOKEN"))
```

de cette maniere on ne va jamais retrouver de problematique d'usurpation de token.


## E.2) Creer une classe pour notre bot

On utilisera le bot plutot que le client pour l'oriente-objet
car comme on l'a vu plus haut, le code est plus versatile.
l'avantage est qu'on aura plus besoin des decorateurs
