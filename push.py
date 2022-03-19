# Push.py


import json
from re import L
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

'''@client.event
async def auto_response(message):
    if message.content.startswith('$hi'):
        channel = message.channel
        await channel.send('hello human')
'''

@client.event
async def on_message(message):

    
    await log(message)
    # to avoid 'commands not working'
    client.process_commands(message)

    async def log(message):
        # get the guild from the message
        guild = message.guild
        # find the channel with name 'logs'
        log_channel = discord.utils.get(guild.channels, name="bot-testing")
        try:
            # if the channel exists and the bot has permissions to send messages in 'logs' channel, 
            # this will pass, else an exception will be thrown
            await log_channel.send("*{0.content}*, sent by **{0.author.nick}**, in **msg.channel.name**".format(message))
        except Exception:
            # exceptions will be raised if any of those said above, are missing
            print("'logs' channel not found, or bot missing permissions")


    if message.content.startswith('$thumb'):
        async def ping(ctx):
             await ctx.send(f"{client.latency}")
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
    
    elif message.content.startswith('$hi'):
        channel = message.channel
        await channel.send('Hello there human')

    elif message.content.startswith('$ping'):
        async def ping(ctx):
             await ctx.send(f"{client.latency}")
        await channel.send(ping)
    
client.run(bot_token)