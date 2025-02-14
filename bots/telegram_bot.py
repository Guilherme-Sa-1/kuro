# telegram_bot.py

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from shared_functions import greet_user, calculate_something, get_news, format_news, get_weather, format_weather




# telegram_bot.py

async def kuro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Command: Respond to humanized commands.
    """
    command = " ".join(context.args)
    action = understand_command(command)
    if action == "weather":
        await update.message.reply_text("Please specify a city for the weather.")
    elif action == "news":
        articles = get_news()
        formatted_news = format_news(articles)
        await update.message.reply_text(formatted_news)
    elif action == "greeting":
        greeting = greet_user(update.message.from_user.first_name)
        await update.message.reply_text(greeting)
    else:
        await update.message.reply_text("Sorry, I didn't understand that.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Command: Respond to /start.
    """
    greeting = greet_user(update.message.from_user.first_name)
    await update.message.reply_text(greeting)

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Command: Respond to /calculate <a> <b>.
    """
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = calculate_something(a, b)
        await update.message.reply_text(f"The result is: {result}")
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /calculate <number> <number>")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Command: Respond to /news <query>.
    """
    query = " ".join(context.args) if context.args else "technology"
    articles = get_news(query)
    formatted_news = format_news(articles)
    await update.message.reply_text(formatted_news)

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Command: Respond to /weather <city_name>.
    """
    if not context.args:
        await update.message.reply_text("Usage: /weather <city_name>")
        return
    
    city_name = " ".join(context.args)
    weather_data = get_weather(city_name)
    formatted_weather = format_weather(weather_data)
    await update.message.reply_text(formatted_weather)

def run_telegram_bot():
    """
    Start the Telegram bot.
    """
    application = Application.builder().token("token-discord").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("calculate", calculate))
    application.add_handler(CommandHandler("news", news))
    application.add_handler(CommandHandler("weather", weather))
    application.run_polling()