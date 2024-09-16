import asyncio

import loguru
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty

api_id = 20464789  # 你的 api_id
api_hash = '87c3a2090b3c3fd98ea22da5e4d39a44'  # 你的 api_hash

client = TelegramClient('abcdefg', api_id, api_hash)

# import asyncio
# from telethon import TelegramClient
from loguru import logger

# 你需要替换下面的值为你的实际API id和hash，以及Bot Token或用户session名称
# api_id = 'YOUR_API_ID'
# api_hash = 'YOUR_API_HASH'
# # session_name = 'YOUR_SESSION_NAME_OR_BOT_TOKEN'
#
# client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()

    me = await client.get_me()
    logger.info(me.stringify())

    username = me.username
    logger.info(username)
    logger.info(me.phone)

    async for dialog in client.iter_dialogs():
        logger.info(dialog)
        try:
            logger.debug(f"{dialog.name} {dialog.id} {dialog.message.peer_id.channel_id} {dialog.pinned}")
        except Exception as e:
            print(e)

    await client.disconnect()

# 运行异步主函数
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

"""

"""