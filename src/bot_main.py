import discord

from values import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    messageStart = message.content.lower()
    if messageStart.startswith('$hello'):
        await message.channel.send('Hello!')
    elif messageStart.startswith('$bot'):
        await message.channel.send('You rang?')

client.run(token)