import discord
from discord.ext import commands
import json
import os
with open("./config.json") as config_file:
    data=json.load(config_file)
token = data["token"]

description = "hi im a bot"
intents=discord.Intents.all()
bot = discord.Bot(command_prefix=commands.when_mentioned_or("$"), description=description, intents=intents)




for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

























filtered_words = ["blue", "red", "green", "yellow"]
@bot.event
async def on_message(message):
    for word in filtered_words:
        if word in message.content:
            print(f"message deleted! {message.content}")
            await message.delete()








@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready ")












        


    

    









bot.run(token)