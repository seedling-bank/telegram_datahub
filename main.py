import asyncio
import traceback
from datetime import datetime

import loguru
import pytz

from sqlalchemy import insert, event
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from telethon import TelegramClient, events

from app.models.users_models import t_alphax_tg_user
from app.utils.send_lark_message import send_a_message

api_id = 20464789  # 你的 api_id
api_hash = '87c3a2090b3c3fd98ea22da5e4d39a44'  # 你的 api_hash

client = TelegramClient('session', api_id, api_hash)

engine = create_async_engine(
    "mysql+aiomysql://deagent:deagentai123@cb-rds.cw5tnk9dgstt.us-west-2.rds.amazonaws.com/alphax_test?charset=utf8mb4",
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


# Alpha X telegram
@client.on(events.ChatAction(chats=1002228316303))
async def handler(event):
    try:
        utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
        formatted_utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')

        if event.user_joined or event.user_added:
            user = await event.get_user()
            if user:
                loguru.logger.info(
                    f'新成员加入 Alpha x: {user.id}')

                information = {
                    "tg_id": user.id,
                    "tg_username": user.username,
                    "create_at": formatted_utc_time,
                    "update_at": formatted_utc_time,
                }

                try:
                    async with async_session() as session:
                        query = insert(t_alphax_tg_user).prefix_with("IGNORE").values(information)
                        await session.execute(query)
                        await session.commit()

                except Exception as e:
                    loguru.logger.error(traceback.format_exc())
                    send_a_message(traceback.format_exc())
    except Exception as e:
        loguru.logger.error(traceback.format_exc())
        send_a_message(traceback.format_exc())


async def main():
    async with client:
        await client.start()
        await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
