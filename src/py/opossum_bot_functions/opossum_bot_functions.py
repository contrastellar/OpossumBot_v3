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

async def return_opossum(conn: psycopg2.connect, client: discord.Client, message: any, ID: int) -> Image:
    """
    Function that returns the specified opossum from the
    database
    """
    # At invokation for this funtion, the `conn` parameter is
    # a working psycopg2 connection.
    cur = conn.cursor()
    # Dummy execution
    cur.execute("SELECT img FROM opossumbot WHERE ID="+str(ID))
    print(cur.fetchall())
    #image = discord.File(cur.fetchall())
    #message.channel.send(image)
    return
