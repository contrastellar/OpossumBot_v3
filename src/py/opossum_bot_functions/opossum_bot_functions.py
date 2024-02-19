"""
The functions module of OpossumBot, all the backend handling of 
"""
import psycopg2
import discord

async def ping(client: discord.Client, message: any):
    """
    Ping function to serve as a placeholder for
    actually sending opossum pictures.
    """
    await message.channel.send('This is a test message!')
    return
