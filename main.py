import asyncio
import json
import traceback
from datetime import datetime

import loguru
import pytz
import redis
from sqlalchemy import insert, event
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from redis import asyncio as aioredis


from telethon import TelegramClient, events

from app.models.users_models import t_tg_users
from app.utils.send_lark_message import send_a_message

api_id = 20464789  # 你的 api_id
api_hash = '87c3a2090b3c3fd98ea22da5e4d39a44'  # 你的 api_hash
# chat_id = 1002080008623  # 群组ID
chat_id = 4140777618  # 群组ID

client = TelegramClient('session', api_id, api_hash)

engine = create_async_engine(
    "mysql+aiomysql://cb:cryptoBricks123@34.218.139.166:3306/da_test?charset=utf8mb4",
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


@client.on(events.ChatAction)
async def handler(event):
    try:
        REDIS_URL = "redis://localhost:6379"
        pool = aioredis.ConnectionPool.from_url(REDIS_URL, max_connections=10)
        redis_client = aioredis.Redis(connection_pool=pool)

        utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
        formatted_utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp = int(utc_time.timestamp() * 1000)

        if event.user_joined or event.user_added:
            user = await event.get_user()
            loguru.logger.info(f'新成员加入: {user.id} - {user.first_name} {user.last_name if user.last_name else ""}')

            information = {
                "tg_id": user.id,
                "tg_first_name": user.first_name,
                "tg_last_name": user.last_name,
                "tg_username": user.username,
                "tg_phone": user.phone,
                "create_time": timestamp,
                "update_time": timestamp,
                "time_at": formatted_utc_time
            }
            try:
                async with async_session() as session:
                    query = insert(t_tg_users).values(information)
                    await session.execute(query)
                    await session.commit()

                message = json.dumps(information)
                result = await redis_client.publish('update_tg_user', message)
                print(result)
            except Exception as e:
                loguru.logger.error(traceback.format_exc())
                send_a_message(traceback.format_exc())
    except Exception as e:
        loguru.logger.error(traceback.format_exc())
        send_a_message(traceback.format_exc())


with client:
    client.run_until_disconnected()
