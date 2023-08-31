import discord
from discord.ext import commands
import random
import os
import time

print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Merhaba, ben {bot.user}! Ben bir botum!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Görüşürüz, {bot.user} senin için her zaman burada!')

@bot.command()
async def kendinyap(ctx):
    await ctx.send(f"İnternette evde basit malzemelerle yapabileceğiniz 'Kendin Yap' projeleri bulabilirsiniz!")
    with open(r"M1L2\M1L3\bot2\kendinyapimages\img1.jpg", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send(f"https://www.youtube.com/watch?app=desktop&v=adCxkgrOJaw")

@bot.command()
async def neyapabilirim(ctx):
   await ctx.send(f"Evde ürettiğiniz atıkları azaltmak için aşağıdaki adımları düşünebilirsiniz:")
   time.sleep(4)
   await ctx.send(f"- 1. *Geri Dönüşüm*: Kağıt, plastik, cam ve metal gibi malzemeleri geri dönüşüm kutularına ayırarak atıklarınızı geri dönüşüme kazandırabilirsiniz.")
   await ctx.send(f"https://efa-tr.com/images/5473011365a.jpg")
   time.sleep(4)
   await ctx.send(f"- 2. *Azaltma Alışkanlığı*: Ürünleri satın alırken gereksiz ambalajları olanları tercih etmeyerek veya toptan alışveriş yaparak atık miktarını azaltabilirsiniz.")
   await ctx.send(f"https://www.alpgeridonusum.com.tr/uploads/images/geri-donusum-nedir.jpg")
   time.sleep(4)
   await ctx.send(f"- 3. *Kullan-At Alışkanlığını Azaltın*: Tek kullanımlık ürünleri mümkünse yerine tekrar kullanılabilir alternatifleri tercih ederek atık üretimini azaltabilirsiniz.")
   await ctx.send(f"https://www.sarcina.com.tr/wp-content/uploads/2023/04/plastik-ambalaj-geri-donusumu-edited-1030x5791-1.jpg")
   time.sleep(4)
   await ctx.send(f"- 5. *Alışveriş Çantası ve Şişe Kullanımı*: Alışveriş yaparken kanvas çanta gibi tekrar kullanılabilir çantalar ve su şişeleri kullanarak plastik kullanımını azaltabilirsiniz.")
   await ctx.send(f"https://d35fbhjemrkr2a.cloudfront.net/Images/Shop/53/Product/5493/Thumb/159-2.jpg")

bot.run("MTEzODk5NTI2OTMzNDIyMDkyMQ.GIoGT8.lilc_q4ItcN6PrO27MMjvp_unr5TD4U3E2I7IM")