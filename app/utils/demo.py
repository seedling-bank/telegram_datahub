@router.get("/tg_me")
async def tg_me(tg_code: int, user_id, db: Database = Depends(get_db), tg_name: Optional[str] = None):
    try:
        information = {
            "tg_id": tg_code,
            "tg_username": tg_name
        }
        query = t_users.update().where(t_users.c.id == user_id).values(information)

        try:
            await db.execute(query)
        except Exception as e:
            loguru.logger.info(e)
            loguru.logger.error(traceback.format_exc())

        select_user = t_users.select().where(t_users.c.id == user_id)
        user_data = dict(await db.fetch_one(query=select_user))
        return JSONResponse(
            content=dict(
                code=200,
                message="successful",
                data=dict(user_data),
            )
        )
    except Exception as e:
        logger.error(traceback.format_exc())
        return JSONResponse({"error": "error"})
    # user_info = await tus.fetch_user_info(token.get("access_token"))
    # logger.info(user_info)
    # logger.info(token)