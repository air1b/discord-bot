
import os

#import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="config")

# creer un bot qui herite de command.Bot
# heritage
class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/") # overloading

    async def on_ready(self): # overriding
        print(f"{self.user.display_name} est connecte au server")

doc_bot = DocBot()
doc_bot.run(os.getenv("TOKEN"))
