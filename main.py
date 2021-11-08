# bot.py
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')


def initialize():
  try:
    with open('user_data.json') as json_file:
      data = json.load(json_file)
      if not data:
        print("no data")
      else:
        print(data)
  except IOError:
    print("No file found")


def start():
  print("hello")
  initialize()
  bot.run(TOKEN)


start()
