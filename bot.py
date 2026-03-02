import discord
from discord.ext import commands
import random
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

dicio = {
    "plástico" : "vc pode fazer mtas coisas mas podemos reciclar fazendo potinhos com garrafas PET",
    "metal" : "vc pode fazer mtas coisas mas podemos reciclar fazendo vazos de plantas com latas",
    "papel" : "vc pode fazer mtas coisas mas podemos reciclar usando o outro lado da sua folha",
    'papelão' : "vc pode fazer mtas coisas mas podemos reciclar fazendo uma prateleira temporária com sua caixa de papelão"
}

def meme_gen():
    lista = os.listdir('images')
    imagem_gerada = random.choice(lista)
    return imagem_gerada

def skzoo_gen():
    lista = os.listdir('skzoo images')
    imagem_gerada = random.choice(lista)
    return imagem_gerada
@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

class MyClient(discord.Client):


    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True



@bot.command()
async def meme(ctx):
    with open(f'images/{meme_gen()}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)


@bot.command()
async def skzoo(ctx):
    with open(f'skzoo images/{skzoo_gen()}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

@bot.command()
async def reciclar(ctx, material):
    await ctx.send(dicio [material])

intents = discord.Intents.default()
intents.message_content = True
bot.run("MTQ2Nzk3MzY4MjU1ODQwMjgzNA.GWGW4j.ktmyV-VsRraFFHNDDBEHhWsIpgjBFMLfDhKFX0")
