# main.py

import asyncio
from bots.discord_bot import run_discord_bot
from bots.telegram_bot import run_telegram_bot

async def run_bots():
    """
    Run both bots concurrently.
    """
    await asyncio.gather(
        asyncio.to_thread(run_discord_bot),  # Run Discord bot in a separate thread
        asyncio.to_thread(run_telegram_bot)  # Run Telegram bot in a separate thread
    )

if __name__ == "__main__":
    asyncio.run(run_bots())