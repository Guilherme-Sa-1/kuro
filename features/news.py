def get_news(topic="geral"):
    """
    Retorna notícias fictícias para testes.
    """
    return [{"title": f"Notícia sobre {topic}", "link": "https://example.com"}]

def format_news(news_list):
    """
    Formata a lista de notícias para exibição.
    """
    return "\n".join([f"{news['title']} - {news['link']}" for news in news_list])
