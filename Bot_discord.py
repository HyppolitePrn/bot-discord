import os
from Node import Node
from discord.ext import commands
import discord
import random
from http import client
from bs4 import BeautifulSoup
import youtube_dl
import requests
import re
import time
import asyncio
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
# Faire le bot
client = commands.Bot(command_prefix='-')

token = os.getenv('TOKEN')


def kwa(sentence):
    term = re.findall("[a-zA-Z]+", sentence)[-1]
    soup = BeautifulSoup(requests.get(
        f"https://fr.wiktionary.org/wiki/{term}").text, features="html.parser")
    el = soup.select_one('span[title="Prononciation API"]')
    if el is None:
        return False
    else:
        return el.contents[0].endswith("kwa\\")


first_node = Node("Comment puis je vous aider ?", "help",
                  [Node("Sur quel sujet ?", "cours", []), Node("Sur quel domaine?", "fichier", [])])


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong ! {round(client.latency * 1000)}ms')

# @client.command()
# async def aide(ctx):
#     await ctx.send(first_node)


@client.command()
async def nerd(ctx):
    ref = ctx.message.reference
    if ref is None:
        return await ctx.reply("Tu n'a répondu a personne")
    await ctx.message.delete()
    await ref.resolved.reply(file=discord.File(r'assets/Video/cringos.mp4'))


@client.command()
async def depression(ctx):
    ref = ctx.message.reference
    if ref is None:
        return await ctx.reply("Tu n'a répondu a personne")
    await ctx.message.delete()
    await ref.resolved.reply(file=discord.File(r'assets/Video/fuckkkk.mp4'))


@client.command()
async def ratio(ctx):
    ref = ctx.message.reference
    if ref is None:
        return await ctx.reply("Tu n'a répondu a personne")
    await ctx.message.delete()
    await ref.resolved.reply(file=discord.File(r'assets/Video/L+ratio.mp4'))


@client.command()
async def reu(ctx):
    ref = ctx.message.reference
    if ref is None:
        return await ctx.reply("Tu n'a répondu a personne")
    await ctx.message.delete()
    await ref.resolved.reply(file=discord.File(r'assets/Video/rompish.mp4'))


@client.command(pass_context=True)
async def join(ctx):
    predefUrl = 'https://www.youtube.com/watch?v=Qu84tcGExSQ'
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        player = ctx.voice_client
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(predefUrl, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            player.play(source)
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
async def cry(ctx):
    ref = ctx.message.reference
    if ref is None:
        return await ctx.reply("Tu n'a répondu a personne")
    await ctx.message.delete()
    await ref.resolved.reply(file=discord.File(r'assets/Video/cry.mp4'))


@client.command()
async def bully(ctx):
    ref = ctx.message.reference
    if ref is None:
        return await ctx.reply("Tu n'a répondu a personne")
    await ctx.message.delete()
    await ref.resolved.reply(file=discord.File(r'assets/Video/Allo_Mc_Fly_online-video-cutter.com.mp4'))


@client.command()
async def laught(ctx):
    ref = ctx.message.reference
    if ref is None:
        return await ctx.reply("Tu n'a répondu a personne")
    await ctx.message.delete()
    await ref.resolved.reply(file=discord.File(r'assets/Video/ahahahaha.mov'))


@client.command()
async def monkey(ctx):
    em = discord.Embed(
        name=f'MONKEY')
    em.set_image(
        url='https://c.tenor.com/d8Nj1CVSRbQAAAAd/monki-flips-dies.gif')
    await ctx.send(embed=em)


@client.command()
async def waitwhat(ctx):
    em = discord.Embed(
        name=f'WAIT WHAT ?')
    em.set_image(
        url='https://c.tenor.com/k_63-OnPklsAAAAC/didsomeonesaycock-didsomeonesay.gif')
    await ctx.send(embed=em)


@client.command()
async def puceau(ctx):
    ref = ctx.message.reference
    if ref is None:
        return await ctx.reply("Tu n'a répondu a personne")
    await ctx.message.delete()
    await ref.resolved.reply(file=discord.File(r'assets/Video/Ferme_la_puceau_de_merde.mp4'))


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

        case 296334984195735554:
            await message.add_reaction("😐")

        case 246701574506676224:
            await message.add_reaction("🥶")

        case 263324664275795968, 501018096723558412:
            ale = random.randint(0, 5)
            if ale == 1:
                await message.add_reaction("💩")

        # case 336588203417010176:
        #     await message.add_reaction("🇹")
        #     await message.add_reaction("🇬")
        #     await message.add_reaction("💩")

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


snipe_message_author = {}
snipe_message_content = {}


@client.event
async def on_message_delete(message):
    snipe_message_content[message.channel.id,
                          message.author.id] = message.content
    snipe_message_author[message.channel.id,
                         message.author.id] = message.author
    await asyncio.sleep(60)
    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]


@client.command(name='snipe')
async def snipe(ctx, user: discord.User):
    channel = ctx.channel

    try:
        em = discord.Embed(
            title=f'dernier message supp dans {channel.name}', description=snipe_message_content[channel.id, user.id])
        em.set_footer(
            text=f"This message was sent by {snipe_message_author[channel.id, user.id]}")
        await ctx.send(embed=em)

    except KeyError:
        await ctx.send(f'oh pelo ya pas de message récement sup dans ce channel **{channel.name}**')

client.run(token)
