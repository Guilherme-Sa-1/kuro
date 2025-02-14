# shared_functions.py

from features.news import get_news, format_news
from features.weather import get_weather, format_weather
from features.ai import understand_command

def greet_user(username):
    """
    A shared function to greet the user.
    """
    return f"Hello, {username}! Welcome to Kuro."

def calculate_something(a, b):
    """
    Example of a shared function that performs a calculation.
    """
    return a + b