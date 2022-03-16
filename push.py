# Push.py


import json
import discord
import asyncio

with open('./config.json', 'r') as f:
    data = json.load(f)
bot_token = data['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    game=discord.Game("Minecraft")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print(
        f'{client.user} is online!\n'
    )
    

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )



@client.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')
    
client.run(bot_token)