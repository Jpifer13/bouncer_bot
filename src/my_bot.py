import random
from discord.ext.commands import Bot
from values import *

prefix = ("!", "$")
client = Bot(command_prefix=prefix)
lineList = [line.rstrip('\n') for line in open('../resources/insults.txt')]
# Create all bot commands after here

@client.command(name='test')
async def test_command(ctx):

    await ctx.send(random.choice(lineList))


client.run(token)