import re
import requests
from bs4 import BeautifulSoup
from http import client
import random
import discord
from discord.ext import commands
from Node import Node
client = discord.Client()
# Faire le bot
client = commands.Bot(command_prefix='-')


def kwa(sentence):
    term = re.findall("[a-zA-Z]+", sentence)[-1]
    soup = BeautifulSoup(requests.get(
        f"https://fr.wiktionary.org/wiki/{term}").text, features="html.parser")
    el = soup.select_one('span[title="Prononciation API"]')
    if el is None:
        return False
    else:
        return el.contents[0].endswith("kwa\\")


first_node = Node("Comment puis je vous aider ?","help",
[Node("Sur quel sujet ?","cours",[]),Node("Sur quel domaine?","fichier",[])])


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong ! {round(client.latency * 1000)}ms')

# @client.command()
# async def aide(ctx):
#     await ctx.send(first_node)

@client.command()
async def nerd(ctx, arg):
    await ctx.send(arg, file=discord.File(r'assets/Video/cringos.mp4'))


@client.command()
async def ratio(ctx, user):
    await ctx.send(user, file=discord.File(r'assets/Video/L+ratio.mp4'))


@client.command()
async def reu(ctx):
    await ctx.send(file=discord.File(r'assets/Video/rompish.mp4'))


@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")


@client.command(pass_context=True)
async def leave(ctx):
    if(ctx.author.voice):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("i am not in a voice channel")


@client.command()
async def cry(ctx, user):
    await ctx.send(user, file=discord.File(r'assets/Video/cry.mp4'))


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_message(message):
    await client.process_commands(message)
    message.content = message.content.lower()

    if message.author == client.user:
        return

    match message.author.id:
        case 263324664275795968:
            ale = random.randint(0, 20)
            if ale == 10:
                await message.channel.send("Youta parle quand t'aura des cheveux...")

        case 257186882365030400:
            await message.add_reaction("😐")
        
        case 246701574506676224:
            await message.add_reaction("🥶")
        
        case 263324664275795968, 501018096723558412:
            ale = random.randint(0, 5)
            if ale == 1:
                await message.add_reaction("💩")

    if first_node.keyword in message.content:
        await message.channel.send(first_node.question)

    if kwa(message.content):
        await message.channel.send(file=discord.File(r'assets/Video/FEUR_intro_3D.mp4'))
        await message.add_reaction("🇫")
        await message.add_reaction("🇪")
        await message.add_reaction("🇺")
        await message.add_reaction("🇷")

    # if message.content == "del":
    #     await message.channel.purge(limit=3)

client.run('OTc4MjI5MjYzNjI0OTk0ODM2.GcraNv.g5Wq-osWlt0pH4Via0-SqrRQlYNDvib61OtygI')
