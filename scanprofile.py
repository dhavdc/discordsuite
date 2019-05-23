import discord
import re

from whitelist import *


async def scanprofile(message, client):
    if "?scanprofile" in message.content:
        userid = message.content.replace('?scanprofile', '')
        userid = re.sub('[^0-9,.]', '', userid)
        profile = await client.fetch_user_profile(userid)
        profilelist = []

        for stuff in profile:
            profilelist.append(stuff)
        await message.channel.send("Name: " +  str(profilelist[1]))
        await message.channel.send("Bot Status: " + str(profilelist[1].bot))
        
        #print(profilelist.connected_accounts)
        # print("Name: ", profile.name)
        # print("User ID: ", profile.user)
        # print("Bot Status: ", profile.bot)
        # print("Connected Accounts: ", profile.connect_accounts)


        #await message.channel.send("Scanned: " + profile )