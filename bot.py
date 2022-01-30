import discord
client = discord.Client()

@client.event
async def on_ready():
    print('DM Your confessions and the message will be anonymous')

@client.event
async def on_message(message):

    if message.author == client.user:
       return

    await message.channel.send('hai')

client.run('OTM3Mzk1MTU3NDEyNzQxMjUz.YfbHRQ.VNd7mTmMyEkrNKQwRQPZ9j9xZ6Y')
