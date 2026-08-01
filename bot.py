import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Ivy est connectée en tant que {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith("ivy"):
        await message.channel.send(
            "Tu viens de m'appeler ? J'espère que tu as une bonne raison 😈"
        )

    await bot.process_commands(message)


keep_alive()
bot.run(TOKEN)
