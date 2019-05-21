import sys
import threading
import discord
from discord import ChannelType
import translate as translate
import currency as currency
import reaction as reactspam
import delete as delete
import ipgrabber as ipgrabber


#dhav
print("\nWelcome to the discord script suite - Created by dhav")
print("\nPlease follow this link to retrieve your token: https://github.com/TheRacingLion/Discord-SelfBot/wiki/Discord-Token-Tutorial")
print("\nYou might have to refresh to see the token section show up - also you can do this in the desktop app, no need for browser")
SERVER_NAME = None
SERVER_OBJECT = None
TOKENDHAV = 'ENTER TOKEN HERE'
TOKEN = 'ENTER TOKEN HERE'
client = discord.Client()

@client.event
async def on_ready():
    print('\nLogged on as: ', client.user)
     
@client.event
async def on_message(message):
    print(message.author.id)
    if "?translate" in message.content:
        await translate.translate(message)
    if "?currency" in message.content:
        await currency.currency(message)
    if "?reactspam" in message.content:
        await reactspam.reaction(message,message.channel,client.user)
    if "?deletemessages" in message.content:
        await delete.delete(message,client)
    if "?ipgrabber" in message.content:
        await ipgrabber.ipgrabber(message)
client.run(TOKEN,bot=False)
