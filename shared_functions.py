from features.news import get_news, format_news
from features.weather import get_weather, format_weather

def greet_user(username):
    """
    A shared function to greet the user.
    """
    return f"Hello, {username}! Welcome to Kuro."
