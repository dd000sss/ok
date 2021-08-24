from discord.ext import commands
import discord
import os
bot = commands.Bot(command_prefix='!*')

@bot.event
async def on_ready():
  print("ok")

@bot.command()
async def TCP_DOWN(ctx, ip, port):
  os.system(f"python3 TCP_DOWN.py {ip} {port}")
bot.run("ODcyMjE4OTcxNDc3MjU4MzEx.YQmrNw.3Mwi0f2UOgPOCVeuaU-Q_7ckOd4")
