from http import client
import discord 

client = discord.Client()

# Faire le bot

# @client.command()
# async def coucou(ctx):
#     await ctx.send("COUCOU !!")

from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests
import re

def kwa(sentence):
  term = re.findall("[a-zA-Z]+", sentence)[-1]
  soup = BeautifulSoup(requests.get(f"https://fr.wiktionary.org/wiki/{term}").text)
  el = soup.select_one('span[title="Prononciation API"]')
  if el is None:
    return False
  else:
    return el.contents[0].endswith("kwa\\")

@client.event
async def on_message(message):
    message.content = message.content.lower()
    
    if message.author == client.user:
        return 
    if message.author.id == 978040870706249728:
        await message.add_reaction("😐")

    if message.author.id == 263324664275795968 or message.author.id == 501018096723558412:
        await message.add_reaction("💩")

    
    if kwa(message.content):
        await message.add_reaction("🇫")
        await message.add_reaction("🇪")
        await message.add_reaction("🇺")
        await message.add_reaction("🇷")

    if message.content == "del":
        await message.channel.purge(limit=3)

client.run('OTc4MjI5MjYzNjI0OTk0ODM2.GcraNv.g5Wq-osWlt0pH4Via0-SqrRQlYNDvib61OtygI')