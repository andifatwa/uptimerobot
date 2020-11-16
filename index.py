import discord
import random
from discord.ext import commands, tasks
from random import choice
from itertools import cycle
from python_utils import *

andi = commands.Bot(command_prefix = "?")
status = cycle(['Genshin Impact', 'Metal Gear Solid 5: The Phantom Pain', 'Watch Dogs Legion', 'Call of Duty', 'Watch Dogs 2', 'GTA V', 'VALORANT', 'Counter Strike', "Assassin's Creed Valhalla", 'Cyberpunk 2077', 'The Witcher 3', 'Undertale'])

@andi.event
async def on_ready():
    change_status.start()
    print("Bot is ready")

@tasks.loop(seconds=120)
async def change_status():
    await andi.change_presence(activity=discord.Game(next(status)))

@andi.command(aliases=["tes","test"])
async def _test(ctx):
    await ctx.send("I'm right here master")

@andi.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
    await ctx.send(fmt.format(member, len(member.roles)))


@andi.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')

@andi.command()
async def ping(ctx):
    ping = round(andi.latency * 1000)
    await ctx.send(f"Pong! {ping}ms")
    if ping >= 150:
        await ctx.send("Wow pasti sangad ngeleg")
    elif ping >= 50:
        await ctx.send("wow sangat kencang")

@andi.command(aliases=['tanya'])
async def _8ball(ctx, *, question):
    responses = [
        'Oh tentu saja',
        'Gatau',
        'Ga lah yakali',
        'bruh',
        'mungkin',
        'ragu2 sih',
        'Y',
        'G',
        'yeet',
        'Ga mau jawab, kamu jelek']
    if question == "kamu siapa?":
        await ctx.send("Useless bot made by useless person")
    else:
        await ctx.send(f'{random.choice(responses)}')
    

@andi.command(aliases=['jawab'])
async def _9ball(ctx, *, question):
    responses_jawab = [
        'yeet',
        'bruh',
        'cringe',
        '...']
    await ctx.send(f'{random.choice(responses_jawab)}')

@andi.command()
async def funfact(ctx):
    funfact = [
        "Dinosaur adalah hewan reptil.",
        "Otot terkuat berdasarkan beratnya adalah masseter.",
        "Susu kuda nil berwarna merah muda cerah.",
        "Warna rumput muda adalah hijau.",
        "Andi Fatwa ganteng.",
        "Ojan alam idaman para wanita.",
        "Pada 12 April 1961, kosmonot Rusia Yuri Gagarin menjadi manusia pertama di luar angkasa ketika dia mengorbit Bumi sekali selama 108 menit penerbangan.",
        "Saya bot gagal",
        "Sarabi adalah ibu Simba, istri Mufasa dan nenek Kiara. Namanya berarti 'fatamorgana' dalam bahasa Swahili.",
        "Rajo Devi menjadi wanita tertua dalam sejarah yang pernah melahirkan pada 28 November, ketika wanita berusia 70 tahun itu melahirkan bayi perempuan di India.",
        "Semua planet, kecuali Bumi, dinamai menurut nama dewa dan dewi Yunani dan Romawi. Nama Bumi adalah nama Inggris / Jerman yang berarti tanah.",
        "Bayi baru lahir tidak bisa bernapas melalui mulut dalam beberapa bulan pertama kehidupan. Karena bayi memiliki saluran hidung yang kecil, mereka akan terdengar pengap saat bernapas.",
        "Konsep SMS dikembangkan atas kerjasama GSM Perancis-Jerman pada tahun 1984 oleh Friedhelm Hillebrand dan Bernard Ghillebaert",
        "Sebagian besar wanita hamil mengetahui jenis kelamin bayi mereka (jika mereka memilih untuk mengetahui) selama USG pertengahan kehamilan, biasanya antara 16 dan 20 minggu.",
        "Alat instrumen kazoo ditemukan pada abad ke-19 oleh seorang Afrika Amerika bernama Alabama Vest di Macon, Georgia, Amerika Serikat.",
        "CD musik populer pertama yang diproduksi di pabrik baru adalah The Pengunjung (1981) oleh ABBA.",
        "Istanbul, kota terbesar di Turki, adalah kota yang masuk kedalam dua kontinen yaitu Asia dan Eropa.",
        "Tornado terbesar dalam sejarah yang tercatat adalah tornado EF-5 hari Jumat tanggal 31 Mei 2013 di El Reno, Oklahoma.",
        "Manusia, simpanse, gorila, orangutan dan nenek moyang mereka yang telah punah membentuk keluarga organisme yang dikenal sebagai Hominidae, sebagai hewan yang paling mirip dengan Manusia."
    ]
    await ctx.send(f'{random.choice(funfact)}')

@andi.command()
async def permohonan(ctx):
    permohonan = [
        "Aku ingin pahala yang gede banget",
        "Nikah ama Cheaslea Islan",
        "Pengen pinter",
        "Pengen pc spek dewa :(",
        "Keluar dari jalur sesat",
        "Dosaku dihapuskan",
        "Ibadahku diterima oleh-Nya"
    ]
    await ctx.send(f'{random.choice(permohonan)}')

@andi.command()
async def yeet(ctx):
    await ctx.send(f'yeet')
    await ctx.send(f'yeet')
    await ctx.send(f'yeet')
    await ctx.send(f'yeet')
    await ctx.send(f'yeet')

@andi.command()
async def andifatwa(ctx):
    await ctx.send("Ikemen")
    await ctx.send("Idaman para wanita")
    await ctx.send("Ganteng sampe cewe2 mimisan")
    await ctx.send("Sholeh dan tidak pernah coli")
    await ctx.send("Rajin beribadah")
    await ctx.send("Calon penghuni surga")
    await ctx.send("Tensai")
    await ctx.send("Never rejected")

@andi.command()
async def payrespect(ctx):
    await ctx.send("F")
    await ctx.send("F")
    await ctx.send("F")
    await ctx.send("F")
    await ctx.send("F")

      
@andi.command()
async def kick(ctx, member : discord.Member, *, reason):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await member.kick(reason=reason)
@clear.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')

andi.run('NzcwMjQ5MDcyMTE5NTEzMDg5.X5a0WQ.W_HnheuE_GM2_Md60WasUvA9cz8')
