import asyncio
import json
import traceback
from datetime import datetime, timezone

import loguru
import pytz
import redis
from sqlalchemy import insert, event, select, update
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from redis import asyncio as aioredis

from telethon import TelegramClient, events

from app.models.users_models import t_tg_users, t_lumoz_tg_users_info, t_lumoz_tg_users, t_users, t_B2_user,  B2_tg_info
from app.utils.send_lark_message import send_a_message

api_id = 20464789  # 你的 api_id
api_hash = '87c3a2090b3c3fd98ea22da5e4d39a44'  # 你的 api_hash

client = TelegramClient('session', api_id, api_hash)
# client = TelegramClient('abcd', api_id, api_hash)

# with client:
#     client.start()  # 启动客户端
#     loguru.logger.info("Telegram客户端连接成功！")  # 添加连接成功的日志消息
#     client.run_until_disconnected()  # 运行客户端直到断开连接

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


# LUMOZ telegram
@client.on(events.ChatAction(chats=1002210488432))
async def handler(event):
    try:
        # REDIS_URL = "redis://10.244.4.140:6379"
        # REDIS_URL = "redis://10.244.4.58:6379"
        # pool = aioredis.ConnectionPool.from_url(REDIS_URL, max_connections=10000)
        # redis_client = aioredis.Redis(connection_pool=pool)

        utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
        formatted_utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp = int(utc_time.timestamp() * 1000)

        if event.user_joined or event.user_added:
            user = await event.get_user()

            if user:
                loguru.logger.info(
                    f'新成员加入LUMOZ: {user.id} - {user.first_name} {user.last_name if user.last_name else ""} ')

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

                        user_data = {
                            "tg_code": 1
                        }
                        query1 = (
                            update(t_lumoz_tg_users)
                            .where(t_lumoz_tg_users.c.tg_id == int(user.id))
                            .values(**user_data)
                        )
                        await session.execute(query1)
                        await session.commit()

                        query = insert(t_lumoz_tg_users_info).prefix_with("IGNORE").values(information)
                        await session.execute(query)
                        await session.commit()
                except Exception as e:
                    loguru.logger.error(traceback.format_exc())
                    send_a_message(traceback.format_exc())
    except Exception as e:
        loguru.logger.error(traceback.format_exc())
        send_a_message(traceback.format_exc())


# DA telegram
@client.on(events.ChatAction(chats=1002080008623))
async def handler(event):
    try:
        # REDIS_URL = "redis://10.244.4.140:6379"
        # REDIS_URL = "redis://10.244.4.58:6379"
        # pool = aioredis.ConnectionPool.from_url(REDIS_URL, max_connections=10000)
        # redis_client = aioredis.Redis(connection_pool=pool)

        utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
        formatted_utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp = int(utc_time.timestamp() * 1000)

        if event.user_joined or event.user_added:
            user = await event.get_user()
            if user:
                loguru.logger.info(
                    f'新成员加入DA: {user.id} - {user.first_name} {user.last_name if user.last_name else ""}')

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

                        user_data = {
                            "tg_code": 1
                        }
                        query1 = (
                            update(t_users)
                            .where(t_users.c.tg_id == str(user.id))
                            .values(**user_data)
                        )
                        await session.execute(query1)
                        await session.commit()

                        query = insert(t_tg_users).prefix_with("IGNORE").values(information)
                        await session.execute(query)
                        await session.commit()

                except Exception as e:
                    loguru.logger.error(traceback.format_exc())
                    send_a_message(traceback.format_exc())
    except Exception as e:
        loguru.logger.error(traceback.format_exc())
        send_a_message(traceback.format_exc())


# B2 telegram
@client.on(events.ChatAction(chats=1001926465799))
async def handler(event):
    try:

        utc_time = datetime.now(timezone.utc)
        formatted_utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp = int(utc_time.timestamp() * 1000)

        if event.user_joined or event.user_added:
            user = await event.get_user()
            if user:
                loguru.logger.info(
                    f'新成员加入B2: {user.id} - {user.first_name} {user.last_name if user.last_name else ""}')

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

                        user_data = {
                            "tg_code": 1
                        }
                        query1 = (
                            update(t_B2_user)
                            .where(t_B2_user.c.tg_id == str(user.id))
                            .values(**user_data)
                        )
                        await session.execute(query1)
                        await session.commit()

                        query = insert(B2_tg_info).prefix_with("IGNORE").values(information)
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
