import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Configurar a API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_gemini(prompt):
    """
    Envia um prompt para o Google Gemini e retorna a resposta.
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Erro ao acessar a IA: {e}"
