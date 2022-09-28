import discord
from discord.ext import commands
import json

with open("./config.json") as config_file:
    data=json.load(config_file)
token = data["token"]


description = "hi im a bot"

intents=discord.Intents.all()


bot = discord.Bot(command_prefix=commands.when_mentioned_or("$"), description=description, intents=intents)


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




@bot.slash_command()
async def ping(ctx, name):
    await ctx.respond(f"Pong! our bots ping is {bot.latency} seconds,  your name is {name}")



@bot.slash_command()
async def calculate(ctx, number1, operator, number2):
    
    def add(num1, num2):
        return num1 + num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2

    def subtract(num1, num2):
        return num1 - num2

    
    if operator == "+":
        result = add(int(number1), int(number2))


        await ctx.respond(f"Done! you number is {result}")

    elif operator == "-":
        result = subtract(int(number1), int(number2))
        await ctx.respond(f"Done! you number is {result}")

    elif operator == "*":
        result = multiply(int(number1), int(number2))
        await ctx.respond(f"Done! you number is {result}")

    elif operator == "/":
        result = divide(int(number1), int(number2))
        await ctx.respond(f"Done! you number is {result}")
    









bot.run(token)
