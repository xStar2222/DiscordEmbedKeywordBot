import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    # so it won't respond to itself
    if message.author == client.user:
        return

    if message.webhook_id is not None:
        # webhook message
        if message.embeds:
            # embedded message
            embed = message.embeds[0]
            # remove next line and adjust message if no mwntion is needed
            role = discord.utils.get(message.guild.roles, name='ROLE NAME')
            if 'KEYWORD #1' in embed.description:
                await message.channel.send(f'Keyword has been mentioned! {role.mention} ')

        if message.embeds:
            # embedded message
            embed = message.embeds[0]
            # remove next line and adjust message if no mwntion is needed
            role = discord.utils.get(message.guild.roles, name='ROLE NAME')
            if 'KEYWORD #2' in embed.description:
                await message.channel.send(f'Keyword has been mentioned! {role.mention} ')
                
        if message.embeds:
            # embedded message
            embed = message.embeds[0]
            # remove next line and adjust message if no mwntion is needed
            role = discord.utils.get(message.guild.roles, name='ROLE NAME')
            if 'KEYWORD #3' in embed.description:
                await message.channel.send(f'Keyword has been mentioned! {role.mention} ')

    else:
        # this is a message sent by a user
        if message.content.startswith('!hello'):
            await message.channel.send('Hello from a user!')

client.run('PUT TOKEN HERE')
