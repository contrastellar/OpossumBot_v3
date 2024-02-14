# This example requires the 'message_content' intent.

import discord
from OpossumBotFunctions import OpossumBotFunctions

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await OpossumBotFunctions.ping(client, message)

TOKEN = open('test.token').read()
client.run(TOKEN)
