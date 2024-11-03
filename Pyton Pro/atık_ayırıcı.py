import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def Merhaba(ctx):
    await ctx.send(f'Merhaba! Hangi atığın sınıfı merak ediyorsun?')

@bot.command()
async def Pet_şişe(ctx):
    await ctx.send(f'Pet_şişe plastik grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Teneke_kutu(ctx):
    await ctx.send(f'Teneke_kutu metal grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır).')

@bot.command()
async def Karton(ctx):
    await ctx.send(f'Karton kağıt grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Gazoz_şişesi(ctx):
    await ctx.send(f'Gazoz_şişesi cam grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Lityum_pil(ctx):
    await ctx.send(f'Lityum_pil pil grubuna giriyor.Sakın pilleri çöp veya geri dönüşüm dışında bir yere atma doğaya çok zarar veriyor!!Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Muz_kabuğu(ctx):
    await ctx.send(f'Muz_kabuğu evsel grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Plastik_bardak(ctx):
    await ctx.send(f'Plastik_bardak plastik grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Gazoz_kapağı(ctx):
    await ctx.send(f'Gazoz_kapağı metal grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır).')

@bot.command()
async def Zarf(ctx):
    await ctx.send(f'Zarf kağıt grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Ayna(ctx):
    await ctx.send(f'Ayna cam grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Telefon_bataryası(ctx):
    await ctx.send(f'Telefon_bataryası pil grubuna giriyor.Sakın pilleri çöp veya geri dönüşüm dışında bir yere atma doğaya çok zarar veriyor!!Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Yemek_artığı(ctx):
    await ctx.send(f'Yemek_artığı evsel grubuna giriyor.Başka bir atığın sınfını merak ediyor musun?(Evet/Hayır)')

@bot.command()
async def Evet(ctx):
    await ctx.send(f'Tamam.Atığının adını yaz.')

@bot.command()
async def Hayır(ctx):
    await ctx.send(f'Tamam.Yardımcı olabildiysem rica ederim.Merak ettiğin bir atık olursa bekliyor olucam.')

bot.run('MTI5MjU0MTU4MjUwMjkyNDQ0MQ.GfUrwS.fBIeF6XlVjHspYUiFcDKnsmRRgSBRBOStB2pvI')













