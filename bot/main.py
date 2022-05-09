import discord
from random import randint
import os

TOKEN = os.getenv()

client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="majk spirit")
    await client.change_presence(activity=activity)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    seed = randint(0,10)

    if (seed == 5) or (message.content.startswith("počuvaj")):
        await message.channel.send('hej, no', reference=message)

client.run(TOKEN)