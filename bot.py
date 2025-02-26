import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class KuroBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            command_prefix='!',
            intents=intents,
            case_insensitive=True
        )
    
    async def setup_hook(self):
        await self.load_extension('cogs.learning')
        await self.tree.sync()

bot = KuroBot()

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')


#Iniciar o bot
if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))