"""
The functions module of OpossumBot, all the backend handling of 
"""
import io
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

async def return_opossum(conn: psycopg2.connect, client: discord.Client, message: any, id: int) -> discord.File:
    """
    Function that returns the specified opossum from the
    database
    """
    # At invokation for this funtion, the `conn` parameter is
    # a working psycopg2 connection.
    cur = conn.cursor()
    # Dummy execution
    cur.execute("SELECT img FROM opossumbot WHERE ID="+str(id))
    # Pull the raw memory bytes from the result set
    memory_item = cur.fetchall().pop(0)[0]
    # Convert the memory item to bytes
    image_bytes = memory_item.tobytes()
    # Convert the bytes to an image
    image = discord.File(io.BytesIO(image_bytes), filename='opossum.png')
    return image

async def add_opossum(conn: psycopg2.connect, client: discord.Client, message: any, image: bytes) -> None:
    """
    Function that adds a new opossum to the database
    The image is handled in this function.
    """
    cur = conn.cursor()

    cur.execute("INSERT INTO opossumbot VALUES (0, %s)", (image,))

    # It's important that the bot is aware of who it is that is sending the image
    # So that must be handled in the bot, rather than in this function.
    return


async def return_admins(conn: psycopg2.connect, client: discord.Client, message: any) -> None:
    """
    Function that returns the list of admins from the bot
    """
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM admins")
    admins = cur.fetchall()

    return admins