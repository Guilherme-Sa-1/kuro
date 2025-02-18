def get_weather(city="desconhecido"):
    """
    Retorna uma previsão do tempo fictícia para testes.
    """
    return {"city": city, "temperature": "25°C", "condition": "Céu limpo"}

def format_weather(weather_data):
    """
    Formata a previsão do tempo para exibição.
    """
    return f"🌤️ O tempo em {weather_data['city']} está {weather_data['temperature']} com {weather_data['condition']}."
