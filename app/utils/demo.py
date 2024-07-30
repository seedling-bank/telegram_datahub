from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty

# 填入你的 Telegram API credentials
api_id = 20464789
api_hash = "87c3a2090b3c3fd98ea22da5e4d39a44"

async def main():
    async with TelegramClient('abc', api_id, api_hash) as client:
        # 获取所有 chat
        async for dialog in client.iter_dialogs():
            # print(f'Chat ID: {dialog.id}, Chat Name: {dialog.name}')
            try:
                print(dialog)
                print(dialog.entiry.id)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())