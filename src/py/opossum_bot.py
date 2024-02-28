# pylint: disable=R1732
# pylint: disable=W0718
# pylint: disable=I1101
# pylint: disable=R1710
# pylint: disable=W0621
"""
OpossumBot core
This module is used as the __main__ script of the OpossumBot functionality
"""

import discord
import psycopg2
from config import load_config
from opossum_bot_functions import opossum_bot_functions


def connect_config(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

DATABASE_CONN = None

# We want to connect to/verify the connection to the DB
# BEFORE we do anything else, because w/o the DB
# we'll run into errors later
if __name__ == '__main__':
    config = load_config()
    DATABASE_CONN = connect_config(config)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """
    Print to stdout what user is being connected to (useful for debugging)
    """
    await client.change_presence(activity=discord.Game(name="Alpha Build! Pls no touch!"))
    print(f'We have logged in as {client.user}')
    return

@client.event
async def on_message(message):
    """
    Handler for all on_message events.
    """
    if message.author == client.user:
        return
    
    if message.content.startswith('!ping'):
        await opossum_bot_functions.ping(client, message)
        print(f'Sent a ping to {message.author.name}')
        return
    
    if message.content.startswith('!possum'):
        file = await opossum_bot_functions.return_opossum(DATABASE_CONN, client, message, 0)
        await message.reply(file=file)
        print(f'Sent a opossum to {message.author.name} in {message.guild.name}')
        return
    
    #if message.content.startswith('!add_possum'):
    #    image = await message.attachments[0].read()
    #    await opossum_bot_functions.add_opossum(DATABASE_CONN, client, message, image)
    #    return
    
    if message.content.startswith('!admins'):
        message_content = await opossum_bot_functions.return_admins(DATABASE_CONN, client, message)
        await message.channel.send(message_content)
        return
    

# This needs to be the bottom of the file
TOKEN = open('run.token', encoding="utf-8").read()
client.run(TOKEN)
