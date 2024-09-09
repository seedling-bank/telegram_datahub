import asyncio
import traceback
from datetime import datetime

import loguru
import pytz
from sqlalchemy import insert, event
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty

from app.models.users_models import t_tg_users, t_lumoz_tg_users_info
from app.utils.send_lark_message import send_a_message

# 填入你的 Telegram API credentials
api_id = 20464789
api_hash = "87c3a2090b3c3fd98ea22da5e4d39a44"

#
# async def main():
#     async with TelegramClient('session', api_id, api_hash) as client:
#         # 获取所有 chat
#         async for dialog in client.iter_dialogs():
#             # print(f'Chat ID: {dialog.id}, Chat Name: {dialog.name}')
#             try:
#                 print(dialog)
#                 print(dialog.entiry.id)
#             except Exception as e:
#                 print(e)
#
#
# if __name__ == '__main__':
#     import asyncio
#
#     asyncio.run(main())


from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat

# 填入你的 Telegram API credentials
api_id = 20464789
api_hash = "87c3a2090b3c3fd98ea22da5e4d39a44"

# chat_id = 4140777618
# async def get_group_members_tgid(chat_id):
#     async with TelegramClient('aaaaaa', api_id, api_hash) as client:
#         # 获取群组成员列表
#         participants = await client.get_participants(chat_id)
#
#         # 提取成员的 Telegram ID
#         member_ids = [participant.id for participant in participants]
#
#         return member_ids

#


engine = create_async_engine(
    "mysql+aiomysql://cb:cryptoBricks123@cb-rds.cw5tnk9dgstt.us-west-2.rds.amazonaws.com/da_test?charset=utf8mb4",
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=10,
)


def checkout_listener(dbapi_connection, connection_record, connection_proxy):
    try:
        dbapi_connection.ping(reconnect=True)
    except dbapi_connection.OperationalError as exc:
        raise DisconnectionError() from exc


# 添加监听事件，在每次从池中获取连接时执行
event.listen(engine.sync_engine, "checkout", checkout_listener)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def main():

    utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
    formatted_utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')
    timestamp = int(utc_time.timestamp() * 1000)

    # chat_id = 4140777618
    chat_id = 2210488432
    client = TelegramClient("aaaaaa", api_id, api_hash)
    await client.connect()
    # 获取群组成员的 Telegram ID

    res = await client.get_entity(chat_id)

    try:

        all_participants = []
        async for participant in client.iter_participants(chat_id, aggressive=True):
            all_participants.append(participant)
            print(f"已获取 {len(all_participants)} 名成员")
        # offset_user = 0
        # while True:
        #     member_ids = await client.get_participants(res, limit=200, offset=offset_user)
        #     if not member_ids:
        #         break
        #     print(len(member_ids))
        #     # print(member_ids)
        #     offset_user += len(member_ids)
        # async with async_session() as session:
        #     for member in member_ids:
        #         information = {
        #             "tg_id": member.id,
        #             "tg_first_name": member.first_name,
        #             "tg_last_name": member.last_name,
        #             "tg_username": member.username,
        #             "tg_phone": member.phone,
        #             "create_time": timestamp,
        #             "update_time": timestamp,
        #             "time_at": formatted_utc_time
        #         }
        #         loguru.logger.info(information)
        #
        #         query = insert(t_lumoz_tg_users_info).prefix_with("IGNORE").values(information)
        #         await session.execute(query)
        #         await session.commit()

    except Exception as e:
        loguru.logger.error(traceback.format_exc())
        send_a_message(traceback.format_exc())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
