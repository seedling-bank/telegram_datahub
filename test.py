import asyncio
import ssl

import traceback
from datetime import datetime, timedelta

import loguru
import pytz
from databases import Database
from fastapi import APIRouter, Depends
import aiohttp
from starlette.responses import JSONResponse

from app.core.depends import get_db
from app.dao.login import UserQuestion
from app.models.user import t_discord_users, t_discord_sign_in, t_tg_users, t_users

router = APIRouter()


@router.post("/verify_user")
async def verify_user(user_question: UserQuestion, db: Database = Depends(get_db)):
    try:

        for index, user_info in enumerate(user_question):
            print(user_info)

        url = f"http://192.168.50.3:8001/api/v1/task/complete_task"

        query = t_discord_users.select().where(t_discord_users.c.discord_id == discord_id)
        results = await db.fetch_all(query)
        list_of_dicts = list()
        for result in results:
            dict_result = dict(result)
            if 'time_at' in dict_result:
                dict_result['time_at'] = dict_result['time_at'].isoformat()
            list_of_dicts.append(dict_result)
            break

        user_info_query = t_users.select().where(t_users.c.discord_id == discord_id)
        results = await db.fetch_all(user_info_query)
        for result in results:
            dict_result = dict(result)
            user_id = dict_result.get("id")

            data = {
                "user_id": user_id,
                "task_id": 7,
                "task_type": "newbie"
            }

            ssl_context = ssl.SSLContext()
            ssl_context.verify_mode = ssl.CERT_NONE
            async with aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(ssl=ssl_context)
            ) as session:
                async with session.post(url=url, json=data) as response:
                    result = await response.text()
                    loguru.logger.info(result)

        if len(list_of_dicts) == 0:
            return JSONResponse(content=dict(code=200, message="success", data=[]))
        else:
            return JSONResponse(content=dict(code=200, message="success", data=list_of_dicts))
    except Exception as e:
        loguru.logger.error(e)
        loguru.logger.error(traceback.format_exc())


@router.get("/verify_discord_sign")
async def verify_discord_sign(discord_id: int, db: Database = Depends(get_db)):
    try:
        url = f"http://192.168.50.3:8001/api/v1/task/complete_task"

        utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
        start_of_today_utc = utc_time.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_today_utc = start_of_today_utc + timedelta(days=1, microseconds=-1)
        start_timestamp = int(start_of_today_utc.timestamp() * 1000)
        end_timestamp = int(end_of_today_utc.timestamp() * 1000)

        query = (t_discord_sign_in.select()
                 .where(t_discord_sign_in.c.discord_id == discord_id)
                 .where(t_discord_sign_in.c.create_time >= start_timestamp)
                 .where(t_discord_sign_in.c.create_time <= end_timestamp)
                 )
        results = await db.fetch_all(query)
        list_of_dicts = list()
        for result in results:
            dict_result = dict(result)
            if 'time_at' in dict_result:
                dict_result['time_at'] = dict_result['time_at'].isoformat()
            list_of_dicts.append(dict_result)

        user_info_query = t_users.select().where(t_users.c.discord_id == discord_id)
        results = await db.fetch_all(user_info_query)
        for result in results:
            dict_result = dict(result)
            user_id = dict_result.get("id")

            data = {
                "user_id": user_id,
                "task_id": 10,
                "task_type": "daily"
            }

            ssl_context = ssl.SSLContext()
            ssl_context.verify_mode = ssl.CERT_NONE
            async with aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(ssl=ssl_context)
            ) as session:
                async with session.post(url=url, json=data) as response:
                    result = await response.text()
                    loguru.logger.info(result)

        if len(list_of_dicts) == 0:
            return JSONResponse(content=dict(code=200, message="success", data=[]))
        else:
            return JSONResponse(content=dict(code=200, message="success", data=list_of_dicts))
    except Exception as e:
        loguru.logger.error(e)
        loguru.logger.error(traceback.format_exc())


@router.get("/verify_tg_user")
async def verify_tg_users(tg_id: int, db: Database = Depends(get_db)):
    try:
        url = f"http://192.168.50.3:8001/api/v1/task/complete_task"

        query = t_tg_users.select().where(t_tg_users.c.tg_id == tg_id)
        results = await db.fetch_all(query)
        list_of_dicts = list()
        for result in results:
            dict_result = dict(result)
            if 'time_at' in dict_result:
                dict_result['time_at'] = dict_result['time_at'].isoformat()
            list_of_dicts.append(dict_result)
            break

        user_info_query = t_users.select().where(t_users.c.tg_id == tg_id)
        results = await db.fetch_all(user_info_query)
        for result in results:
            dict_result = dict(result)
            user_id = dict_result.get("id")

            data = {
                "user_id": user_id,
                "task_id": 9,
                "task_type": "newbie"
            }

            ssl_context = ssl.SSLContext()
            ssl_context.verify_mode = ssl.CERT_NONE
            async with aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(ssl=ssl_context)
            ) as session:
                async with session.post(url=url, json=data) as response:
                    result = await response.text()
                    loguru.logger.info(result)

        if len(list_of_dicts) == 0:
            return JSONResponse(content=dict(code=200, message="success", data=[]))
        else:
            return JSONResponse(content=dict(code=200, message="success", data=list_of_dicts))
    except Exception as e:
        loguru.logger.error(e)
        loguru.logger.error(traceback.format_exc())


if __name__ == '__main__':
    # asyncio.run(verify_discord_group_users())
    asyncio.run(verify_tg_users())
