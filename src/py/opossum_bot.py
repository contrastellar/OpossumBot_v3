"""

"""

import discord
import psycopg2
from config import load_config
from opossum_bot_functions import opossum_bot_functions


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
    """
    Print to stdout what user is being connected to (useful for debugging)
    """
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    """
    Handler for all on_message events.
    """
    if message.author == client.user:
        return

    if message.content.startswith('!possum'):
        
        # TODO need to change the call here so that it sends an opossum
        await opossum_bot_functions.ping(client, message)

TOKEN = open('run.token', encoding="utf-8").read()
client.run(TOKEN)

if __name__ == '__main__':
    config = load_config()
    connect(config)
