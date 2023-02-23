import json
import requests
import discord
from discord import Intents
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=Intents.all())


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(
        f'Hello, {author.mention}!')


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='Random Fox')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)


@bot.command()
async def echo(ctx, *, content: str):
    await ctx.send(content)


bot.run(
    'TOKEN')
