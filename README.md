

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


> A.1) A quoi sert un bot discord?

Execute le comportement d'une personne a sa place
Ex: donner un cours de bourse quand une personne le demande.

> A.2) difference entre bot et application ?

Pour creer un bot il faut: creer une application dans discord ( a l'interieur de de cette app que l'on dev le bot )
infos: 
  - On peut dev une app sans bot.
  - On peut deployer un bot sur different server.
  - Le bot a des droits comme un utilisateur.
  - Le comportements ainsi que les reponses donnes par le bot sont codes au prealables

> A.3) Les prerequis 

  - une application discord
  - un bot 
  - server: dediee ou perso (tout depend des besoins)

techno:

  - python3.8
  - Environnement virtuel
  - discord.py (API de discord)

> B.1)

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
> B.2) Ajout du bot

Aller sur le portail de discord > section developer > application et creer une nouvelle application.

Aller sur la parti Bot, ajouter un bot, configurer selon besoin
( verifier si on authorise l'utilisation du bot sur d'autre server )

Ensuite nous allons cliquer sur la parti Oauth2 pour inviter le bot sur notre server
Oauth2 > URL Generator
Cocher bot, et donner les permissions a notre bot soit administratif soit autre.

Copier coller le lien, passer le processus d'ajout, et verifier sur le server la presence du nouveau bot.
Si on va sur les setting du server on pourra voir un role specifique au bot qui lui a ete attribuer, 
celui ci correspond a la partie Oauth2 > URL GENERATOR.

> B.3) connecter le bot

creer un script main.py et l'executer

```python
import discord


client = discord.Client()
client.run("<BOT-KEY-API>")
```
ce code permet de mettre le bot en ligne

> C.1) on_ready
 
Se connecter est un evenement definit par la methode: on_ready()
en executant cette methode on va pouvoir mettre en ligne notre robot.
[Check ici l'api sur la parti 'event reference' pour plus d'info](https://discordpy.readthedocs.io/en/stable/api.html)
> > Called when the client is done preparing the data received from Discord. Usually after login is successful and the Client.guilds and co. are filled up.

la methode on_ready permet d'ecouter si le bot est pret a executer des commandes.


> C.2) Reagir a un message

on_message() permettra de parser le contenu des messages des 
users sur le server et introduire a partir de conditions
des reponses adapter.
message.channel.send -> permet au bot d'envoyer un messsage.
Dans notre cas present on va inclure async/await pour:
respecter le bonne ordre et permettre a l'application de
ne pas bloquer.

on peut dire a notre robot par ex d'envoyer un message et qu'il
s'autodetruit 5 secondes plus tard

```python
await message.channel.send ("pong", delete_after=5)
```

> C.3) Reagire a l'arrivée d'un membre

