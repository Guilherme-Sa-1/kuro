import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro')
        self.chats = {}

    def get_chat(self, user_id):
        if user_id not in self.chats:
            self.chats[user_id] = self.model.start_chat(history=[])
        return self.chats[user_id]

    async def generate_response(self, user_id, prompt):
        try:
            chat = self.get_chat(user_id)
            response = await chat.send_message_async(prompt)
            return response.text
        except Exception as e:
            return f"❌ Erro ao gerar resposta: {str(e)}"