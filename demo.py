import asyncio

from sqlalchemy import select, event
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.ext.asyncio import async_session, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.models.users_models import t_users

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
async def a():
    user_id = "5204123039"
    query = select(t_users.c.id).where(t_users.c.tg_id == user_id)
    try:
        async with async_session() as session:
            result = await session.execute(query)
            user = result.scalars().first()
            print(user)
            print(type(user))
    except Exception as e:
        pass


if __name__ == '__main__':
    asyncio.run(a())