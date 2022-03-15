# Push.py


import json
import discord

with open('./config.json', 'r') as f:
    data = json.load(f)
bot_token = data['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(
        f'{client.user} is online!\n'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    
client.run(bot_token)