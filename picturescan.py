import discord
import re
from whitelist import *
import requests, json
url = "http://localhost:5000/search"


async def picturescan(message, channel):
    if "?picturescan" in message.content:
            async for lastmessage in channel.history(limit=int(5)):
                if lastmessage.attachments:
                    print(lastmessage.attachments)
                    for attachment in lastmessage.attachments:
                        print(attachment.url)
                        data = {
                            "image_url":attachment.url,
                            "resized_images":False, # Or True
                            "cloud_api":True
                        }
                        headers = {'Content-type': 'application/json'}
                        r = requests.post(url, headers=headers, data=json.dumps(data))
                        print(r.json())

                

                    