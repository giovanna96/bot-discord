# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.command(name='plist', help='list all user connected to a  voice channel)
async def pslist(ctx):
    teste = ctx.message.author.voice
    if(ctx.message.author.voice == None):
        await ctx.send("it's necessary to join into a voice channel to use this command")
    else:
        channel = ctx.message.author.voice.channel
        members = channel.members
        message = 'Users (voice channel '+ str(channel) +'): \n'
        for member in members:
            message = message + member.name + '\n'
        await ctx.send(message)

bot.run(TOKEN)
