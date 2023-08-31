import discord
from discord.ext import commands
import random
import os

print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def joke(ctx):
    await ctx.send(f'Adamın biri bir gün sigara bırakma hattını aramış. Demiş ki; "Benim eve de sigara bırakır mısın gardaş"')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open(r'C:\Users\W10\Desktop\Kodland\M1L2\M1L3\images\mem1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def randommem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'M1L2\M1L3\images\{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

#Meme gönderme komutunu ekle*

bot.run("MTEzODk5NTI2OTMzNDIyMDkyMQ.GIoGT8.lilc_q4ItcN6PrO27MMjvp_unr5TD4U3E2I7IM")