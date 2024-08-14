from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty

# 填入你的 Telegram API credentials
api_id = 20464789
api_hash = "87c3a2090b3c3fd98ea22da5e4d39a44"

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        pass


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())