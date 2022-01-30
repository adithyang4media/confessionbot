import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print('DM Your confessions and the message will be anonymous')

@client.event
async def on_message(message):

    if message.author == client.user:
       return

    await message.channel.send('hai')

client.run(os.environ['token'])
