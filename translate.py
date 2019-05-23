import discord
from yandex_translate import YandexTranslate
from googletrans import Translator
from whitelist import *

translatorYandex = YandexTranslate('trnsl.1.1.20190520T002820Z.4e3db21495664c2e.993b41d7a965db8e67b458230d18464fa316da87')
translatorGoogle = Translator()



async def translate(message):
    if ("?translate" in message.content and message.author.id in WHITELIST):
        if "google" in message.content:
                
            strippedmessage = message.content.replace('?translate', '')
            strippedmessage = strippedmessage.replace('google', '')
            if "portugese" in message.content:
                strippedmessage = strippedmessage.replace('portugese', '')
                translatedmessage = translatorGoogle.translate(strippedmessage, dest='pt')
                await message.channel.send(translatedmessage.text)
                return
            translatedmessage = translatorGoogle.translate(strippedmessage, dest='en')
            if translatedmessage.src == "ru":
                await message.channel.send(translatedmessage.text)
            else:
                translatedmessage = translatorGoogle.translate(strippedmessage, dest='ru')
                await message.channel.send(translatedmessage.text)
        if "yandex" in message.content:
            strippedmessage = message.content.replace('?translate', '')
            strippedmessage = strippedmessage.replace('yandex', '')
            sourcelanguage = translatorYandex.detect(strippedmessage)
            if sourcelanguage == "ru":
                translatedmessage = translatorYandex.translate(strippedmessage, sourcelanguage + "-en") 
                await message.channel.send(translatedmessage.get("text", '')[0])
            else:
                translatedmessage = translatorYandex.translate(strippedmessage, sourcelanguage + "-ru") 
                await message.channel.send(translatedmessage.get("text",'')[0])
