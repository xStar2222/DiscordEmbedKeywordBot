import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send(f'Hello! @{discord.user}')



client.run('token')
