import discord
import re
from whitelist import *
from forex_python.converter import CurrencyRates
CurrencyRates = CurrencyRates()
async def currency(message):
    if ("?currency" in message.content and message.author.id in WHITELIST):
        amount = re.findall(r'\d+', message.content)
        currencies = message.content.replace(amount[0], '')
        currencyID = [word for word in currencies.split() if len(word) == 3]
        print(int(amount[0]))
        print(currencyID)   
        if len(currencyID) == 2:
            convertednumber = CurrencyRates.convert(currencyID[0], currencyID[1], int(amount[0]))
            await message.channel.send((amount[0]) + " " + str(currencyID[0]) + " is " + str(convertednumber) + " " + str(currencyID[1]))
      
           

        