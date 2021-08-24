from discord.ext import commands
import discord
import os
import sys
bot = commands.Bot(command_prefix='!*')

@bot.event
async def on_ready():
  print("ok")

@bot.command()
async def TCP_DOWN(ctx, ip, port):
  os.system(f"python3 TCP_DOWN.py {ip} {port}")
bot.run(sys.argv[1])
