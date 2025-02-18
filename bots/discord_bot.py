import discord
from discord.ext import commands
from shared_functions import greet_user, calculate_something, get_news, format_news, get_weather, format_weather

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

@bot.command()
async def hello(ctx):
    """
    Comando: Responde a !hello.
    """
    greeting = greet_user(ctx.author.name)
    await ctx.send(greeting)

@bot.command()
async def calculate(ctx, a: int, b: int):
    """
    Comando: Responde a !calculate <a> <b>.
    """
    result = calculate_something(a, b)
    await ctx.send(f"O resultado é: {result}")

@bot.command()
async def news(ctx, query="technology"):
    """
    Comando: Responde a !news <query>.
    """
    articles = get_news(query)
    formatted_news = format_news(articles)
    await ctx.send(formatted_news)

@bot.command()
async def weather(ctx, city_name):
    """
    Comando: Responde a !weather <city_name>.
    """
    weather_data = get_weather(city_name)
    formatted_weather = format_weather(weather_data)
    await ctx.send(formatted_weather)

# Executar o bot (chamado por main.py)
def run_discord_bot():
    bot.run('Token-discord')
