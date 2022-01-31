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
    channel = client.get_channel(937376371733327872)
    await channel.send(message.content)
    au = str(message.author)
    ms = str(message.content)
    msg = au + " : " + ms
    
    logchannel = client.get_channel(937709682544484423)
    await logchannel.send(msg)

client.run(os.environ['token'])
