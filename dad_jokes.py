import requests
import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.environ.get("DISCORD_TOKEN")

description = '''A Bot that tells dad jokes'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

api_url = "https://icanhazdadjoke.com/"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def dad_joke(ctx):
    try:
        response = requests.get(api_url, headers={"Accept": "application/json"})
    except Exception:
        await ctx.send('Could\'t get a joke!')
        return

    joke = response.json()['joke']
    await ctx.send(joke)

bot.run(token)