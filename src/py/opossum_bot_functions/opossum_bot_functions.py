import psycopg2
import discord

async def ping(client: discord.Client, message: any):
    await message.channel.send('This is a test message!')
    return
