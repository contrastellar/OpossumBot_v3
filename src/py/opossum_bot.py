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
from random import randint


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
    Print to stdout what user is being connected to, for logging purposes
    """
    # await client.change_presence(activity=discord.Game(name="Alpha Build! Pls no touch!"))
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
        number = await opossum_bot_functions.number_opossums(DATABASE_CONN, client, message)
        file = await opossum_bot_functions.return_opossum(DATABASE_CONN, client, message, randint(1, number))
        await message.reply(file=file)
        print(f'Sent a opossum to {message.author.name} in {message.guild.name}')
        return
    
    if message.content.startswith('!add_possum'):
        admins = await opossum_bot_functions.return_admins(DATABASE_CONN, client, message)
        if admins.__contains__(message.author.id):
            image = await message.attachments[0].read()
            await opossum_bot_functions.add_opossum(DATABASE_CONN, client, message, image)
            number = await opossum_bot_functions.number_opossums(DATABASE_CONN, client, message)
            await message.channel.send(f'{message.author.name} has added a new opossum to the database! :) \n the image is ' + str(number))
        else:
            await message.channel.send('You are not an admin! AAAAAAA!')
        return
    
    if message.content.startswith('!admins'):
        message_content = await opossum_bot_functions.return_admins(DATABASE_CONN, client, message)
        await message.channel.send(message_content)
        return
    
    if message.content.startswith('!add_admin'):
        if message.author.id == 181187505448681472:
            await opossum_bot_functions.add_admins(DATABASE_CONN, client, message)
            await message.channel.send(f'{message.author.name} has added a new admin to the database! :)')
        else:
            await message.channel.send('You are not an admin! AAAAAAA!')
            print("!add_admin command ignored")
        return
    
    if message.content.startswith('!number_opossums'):
        admins = await opossum_bot_functions.return_admins(DATABASE_CONN, client, message)
        if admins.__contains__(message.author.id):
            number = await opossum_bot_functions.number_opossums(DATABASE_CONN, client, message)
            await message.channel.send(f'Number of opossums in the database is {number}')
            return
        else:
            await message.channel.send('You are not an admin! AAAAAAA!')
            print("!number_opossums command ignored")
            return
        
    if message_content.startswith('!wheel'):
        await message.channel.send('https://cdn.discordapp.com/attachments/915671205938364477/1213542487239565332/video0_13.mp4')

# This needs to be the bottom of the file
TOKEN = open('run.token', encoding="utf-8").read()
client.run(TOKEN)
