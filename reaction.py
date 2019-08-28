import discord
import re
from whitelist import *
async def reaction(message, channel, client):
    if "?reactspam" in message.content:
        LIMIT = re.findall(r'\d+', message.content)
        emoji = message.content.replace('?reactspam','')
        if LIMIT:
            emoji = emoji.replace(LIMIT[0], '')
        emoji = emoji.encode('unicode-escape').decode('unicode-escape')
        if "delete" in message.content:
            emoji = emoji.replace('delete', '')
            async for messages in channel.history(limit=int(100)):
                await messages.remove_reaction(emoji.strip().upper().replace("\\", ""), client)
        else:
            print(emoji.strip().upper())
            print(type('\U0001F3D3'))
            async for messages in channel.history(limit=int(LIMIT[0])):
                await messages.add_reaction(emoji.strip().upper().replace("\\", ""))