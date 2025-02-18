import re

def parse_command(message):
    """
    Analisa uma mensagem humanizada e retorna um comando correspondente.
    """
    message = message.lower()

    # Detecta pedido de alerta
    alert_match = re.search(r"alerta.*?(\d{1,2}:\d{2}).*?(\d{1,2}/\d{1,2}/\d{4}|hoje|amanhã)", message)
    if alert_match:
        return {"action": "alert", "time": alert_match.group(1), "date": alert_match.group(2)}

    # Detecta pedido de previsão do tempo
    weather_match = re.search(r"(tempo|clima) (em|para) (.+)", message)
    if weather_match:
        return {"action": "weather", "city": weather_match.group(3)}

    # Detecta pedido de notícias
    news_match = re.search(r"(notícias|news) sobre (.+)", message)
    if news_match:
        return {"action": "news", "topic": news_match.group(2)}

    # Detecta cálculos matemáticos simples
    calc_match = re.search(r"quanto é (\d+)[\s]*([\+\-\*/])[\s]*(\d+)", message)
    if calc_match:
        return {"action": "calculate", "num1": int(calc_match.group(1)), "operator": calc_match.group(2), "num2": int(calc_match.group(3))}

    return {"action": "unknown"}
