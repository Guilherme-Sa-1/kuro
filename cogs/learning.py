import discord
from discord.ext import commands
from services.gemini import GeminiService
from utils.database import Database

class Learning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gemini = GeminiService()
        self.db = Database()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.content.startswith('!'):
            return

        try:
            response = await self.gemini.generate_response(
                user_id=message.author.id,
                prompt=message.content
            )
            
            sent_message = await message.reply(response)
            self.db.save_interaction(
                user_id=message.author.id,
                prompt=message.content,
                response=response
            )
            
        except Exception as e:
            await message.reply(f"⚠️ Ocorreu um erro: {str(e)}")

    @commands.command()
    async def reset(self, ctx):
        """Reseta o histórico de conversa"""
        self.gemini.chats.pop(ctx.author.id, None)
        await ctx.send("Histórico de conversa resetado com sucesso!")

async def setup(bot):
    await bot.add_cog(Learning(bot))