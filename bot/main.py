import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

load_dotenv()

token = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == 'test':
        await message.channel.send(f'Hello {message.author.display_name}!')
        
client.run(token=token)