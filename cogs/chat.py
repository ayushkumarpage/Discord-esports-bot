import discord
import random
from discord.ext import commands

class Chat(commands.Cog, name="Extras"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("chat file is loaded")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "??":
            await message.channel.send(f"{message.author.name} didn't understand what you told!")
        elif message.content == "idk":
            await message.channel.send(f"{message.author.name} don't know what you asked!'")
        elif message.content == "hi":
            await message.channel.send(f"Hi {message.author.name}, welcome to the chat!")
        elif message.content == "dead chat":
            await message.channel.send(f"{message.author.name}, if it is dead chat then why are you chatting here!")
        elif "<@699566190842085439>" in message.content:
            r = [":expressionless:",":rolling_eyes:"]
            await message.channel.send(random.choice(r))
        elif "<@651506861844987906>" in message.content:
            t = [":expressionless:",":rolling_eyes:"]
            await message.channel.send(random.choice(t))

def setup(bot):
    bot.add_cog(Chat(bot))
