import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from shared_functions import greet_user, get_news, format_news, get_weather, format_weather
from features.command_parser import parse_command
from features.gemini import chat_with_gemini

# Carregar variáveis do .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Inicializar o bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """
    Evento: Quando o bot está pronto.
    """
    print(f'Kuro (Discord) está pronto! Logado como {bot.user.name}')

@bot.event
async def on_message(message):
    """
    Evento: Responde automaticamente a mensagens humanizadas.
    """
    if message.author == bot.user:
        return  # Evita que o bot responda a si mesmo

    if bot.user.mentioned_in(message) or not message.content.startswith("!"):
        parsed = parse_command(message.content)

        if parsed["action"] == "alert":
            await message.channel.send(f"⏰ Alerta criado para {parsed['time']} no dia {parsed['date']}.")

        elif parsed["action"] == "weather":
            weather_data = get_weather(parsed["city"])
            formatted_weather = format_weather(weather_data)
            await message.channel.send(formatted_weather)

        elif parsed["action"] == "news":
            articles = get_news(parsed["topic"])
            formatted_news = format_news(articles)
            await message.channel.send(formatted_news)

        elif parsed["action"] == "calculate":
            result = eval(f"{parsed['num1']} {parsed['operator']} {parsed['num2']}")
            await message.channel.send(f"🧮 O resultado é: {result}")

        else:
            resposta = chat_with_gemini(message.content)
            await message.channel.send(f"🤖 {resposta}")

    await bot.process_commands(message)  # Permite que comandos tradicionais continuem funcionando

@bot.command()
async def hello(ctx):
    """
    Comando: Responde a !hello.
    """
    greeting = greet_user(ctx.author.name)
    await ctx.send(greeting)

# Executar o bot (chamado por main.py)
def run_discord_bot():
    bot.run(DISCORD_TOKEN)
