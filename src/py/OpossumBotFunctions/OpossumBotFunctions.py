import psycopg2

async def ping(client, message):
    await message.channel.send('This is a test message!')
    return
