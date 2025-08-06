import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

# Load token from .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Set up bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# On ready event
@bot.event
async def on_ready():
    print(f'✅ Meow~ Logged in as {bot.user.name} the Catbot!')

# Game invitation command
@bot.command()
async def game(ctx, game: str, time: str, *mentions: discord.Member):
    print(f"DEBUG: Called with game={game}, time={time}, mentions={mentions}")
    try:
        if not mentions:
            await ctx.send("😾 Oops! You forgot to mention your gaming pawtners. Try `!game valorant 8PM @friend`")
            return

        mention_text = ' '.join(member.mention for member in mentions)

        embed = discord.Embed(
            title="🎮 Game Time Meow!",
            description=f"**Game:** {game}\n**Time:** {time}\n\nLet's paw-ty together! 🐾",
            color=discord.Color.blurple()
        )
        embed.set_footer(text=f"Sent by {ctx.author.display_name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1864/1864514.png")

        await ctx.send(content=mention_text, embed=embed)
    except Exception as e:
        print("❌ Error in game command:", e)
        await ctx.send("🐱‍👤 Something went wrong...")

# Play music from YouTube
@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel if ctx.author.voice else None
    if not voice_channel:
        await ctx.send("😿 You need to be in a voice channel first, hooman!")
        return

    vc = await voice_channel.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'extract_flat': False,
        'outtmpl': 'song.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']

    vc.play(discord.FFmpegPCMAudio(audio_url), after=lambda e: print("✅ Done playing"))

    await ctx.send(f"🎵 Now playing: **{info['title']}** ~nya~")

# Stop music
@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⏹️ Meow~ I’ve left the voice channel. Bye bye humans~")
    else:
        await ctx.send("🙀 I’m not even in a voice channel yet, silly!")

# Keep alive and run bot
keep_alive()
bot.run(TOKEN)
