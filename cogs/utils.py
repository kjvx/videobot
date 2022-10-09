import discord 

from discord.ext import commands


class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Cog {self} ready')


    @commands.slash_command()
    async def pingutilscog(self, ctx):
        await ctx.respond(f'utils cog is ready')





    @commands.slash_command()
    async def calculate(self, ctx, number1, operator, number2):
        if operator == '+':
            await ctx.respond(f"Done! our bot has calculated {int(number1) + int(number2)}")
        if operator == '-':
            await ctx.respond(f"Done! our bot has calculated {int(number1) - int(number2)}")
        if operator == '/':
            await ctx.respond(f"Done! our bot has calculated {int(number1) / int(number2)}")
        if operator == '*':
            await ctx.respond(f"Done! our bot has calculated {int(number1) * int(number2)}")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        filtered_words = ["blue", "red", "green", "yellow"]
        for word in filtered_words:
            if word in message.content:
                print(f"message deleted! {message.content}")
                await message.delete()

def setup(bot):
    bot.add_cog(utils(bot))