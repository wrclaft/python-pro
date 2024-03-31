import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents=intents)   

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def atik(ctx):
    atik = random.randint(1, 5)
    if atik == 1:
        with open('images/atik.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send(f'Merhaba! Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen gençler \n Gıda Atıklarını Azaltın: Yiyecekleri çöpe atmadan önce \n mutlaka değerlendirin. Artan yemekleri başka bir öğünde tüketebilir veya dondurarak saklayabilirsiniz.Atık Pil ve Elektronikleri Doğru Bir Şekilde Bertaraf Edin: Atık pilleri ve elektronik cihazları sadece belirlenmiş geridönüşüm noktalarına teslim edin. Bu, çevreye ve sağlığa zararlı olabilecek atıkların doğru şekilde bertaraf edilmesini sağlar.')
    if atik == 2:
        with open('images/atik2.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send(f'Merhaba! Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen gençler \n Atık kağıtlar, kağıt geri dönüşüm kutularında toplanır ve diğer kağıt geri dönüşüm kutularından alınan kağıtlarla birlikte büyük bir geri dönüşüm konteynerine konur. Geri kazanılan veya toplanan tüm kağıt atıklar daha sonra bir toplama aracı veya kamyonla kağıt geri dönüşüm tesisine taşınır.')
    if atik == 3:
        with open('images/atik3.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send(f'Merhaba! Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen gençler \n Daha Az Kağıt Kullanın: Not almak için kağıt yerine dijital ortamları tercih edebilirsiniz. E-kitaplar ve dijital dergiler gibi dijital medya seçeneklerini değerlendirerek kağıt tüketimini azaltabilirsiniz.')
    if atik == 4:
        with open('images/atik4.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send(f'Merhaba! Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen gençler \n Fazla Enerji Tüketimini Azaltın: Lambaları kapatmayı unutmayın, gereksiz yere elektronik cihazları açık bırakmayın ve enerji tasarruflu cihazlar kullanmaya özen gösterin.Atık miktarını azaltmak, çevreye ve gelecek nesillere karşı sorumluluk sahibi olmanın önemli bir yoludur. Yukarıda verilen pratik adımları uygulayarak siz de çevreye duyarlı bir yaşam tarzı benimseyebilirsiniz.')
    if atik == 5:
        with open('images/atik5.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send(f'Merhaba! Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen gençler \n Tekrar Kullanılabilir Ürünler Kullanın: Plastik poşetler yerine bez torbalar, tek kullanımlık su şişeleri yerine tekrar doldurulabilir su şişeleri kullanarak atık miktarını azaltabilirsiniz.')



bot.run("bot tokeni")
