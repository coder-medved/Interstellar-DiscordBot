import json
import requests
import discord
from discord import Intents
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(
        f'Hello, {author.mention}!')


@bot.command()
async def img(ctx, content: str):
    print(content)
    response = requests.get(f'https://some-random-api.ml/img/{str(content)}')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title=f'{str(content)}')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

@bot.event('Где моя нашя неко-тян?')
async def on_message(ctx):
    if ctx.author != bot.user:
        if str(ctx.author) == "1_-NauRy-_1#2298":
            await ctx.reply("Ваша милая неко-тян здесь, Хозяин!")
            await ctx.reply(file=discord.File('img.png'))
        else:
            await ctx.reply("Я не твоя неко-тян -.-")


@bot.command()
async def echo(ctx, *, content: str):
    await ctx.send(content)


bot.run('MTA3MTQ0ODk4OTIwNTAxMjQ4MA.GV6UBL.ae-fqjCXkY2FLD9ngK68HgTQxDmElTZBDKwBBs')

