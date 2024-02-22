"""
The functions module of OpossumBot, all the backend handling of 
"""
import discord
import psycopg2
from PIL import Image

async def ping(client: discord.Client, message: any):
    """
    Ping function to serve as a placeholder for
    actually sending opossum pictures.
    """
    await message.channel.send('This is a test message!')
    return

def return_opossum(client: discord.Client, message: any, ID: int) -> Image:
    """
    Function that returns the specified opossum from the
    database
    """
    return