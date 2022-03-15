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

client.run(bot_token)