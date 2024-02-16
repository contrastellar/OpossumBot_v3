# This example requires the 'message_content' intent.

import discord
from OpossumBotFunctions import OpossumBotFunctions

import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


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

    if message.content.startswith('!possum'):
        # TODO need to update this so that it returns an opossum picture
        await OpossumBotFunctions.ping(client, message)

TOKEN = open('run.token').read()
client.run(TOKEN)

if __name__ == '__main__':
    config = load_config()
    connect(config)