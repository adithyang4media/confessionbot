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

    await message.channel.send('Your Confesion is anonymously forwarded Successfully')
    channel = client.get_channel(937709682544484423)
    await channel.send(message.content)
    au = message.author
    ms = message.content
    msg = au + ms
    print(msg)
    logchannel = client.get_channel(937709682544484423)
    await logchannel.send(msg)

client.run(os.environ['token'])
