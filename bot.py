import sys
import threading
import discord
from discord import ChannelType
import translate as translate
import currency as currency
import reaction as reactspam
import delete as delete
import picturescan as picturescan
import scanprofile as scanprofile
from secret_keys import *


#dhav
print("\nWelcome to the discord script suite - Created by dhav")
print("\nPlease follow this link to retrieve your token: https://github.com/TheRacingLion/Discord-SelfBot/wiki/Discord-Token-Tutorial")
print("\nYou might have to refresh to see the token section show up - also you can do this in the desktop app, no need for browser")
SERVER_NAME = None
SERVER_OBJECT = None
TOKENDHAV = "MjQ5NzMwNzAxOTE2NzY2MjA4.XQrmnQ.uNY3hEp9wKryRVVYRQ9aCsyk7pU"
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
    if "?picturescan" in message.content:
        await picturescan.picturescan(message, message.channel)
    if "?scanprofile" in message.content:
        await scanprofile.scanprofile(message, client)
client.run(TOKEN, bot=False)
