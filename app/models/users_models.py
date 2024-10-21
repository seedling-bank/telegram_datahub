from sqlalchemy import Table, MetaData, Column, INTEGER, String, DATETIME, Text, VARCHAR
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

t_alphax_tg_user = Table(
    "alphax_tg_user",
    metadata,
    Column("id", INTEGER(), primary_key=True, autoincrement=True),
    Column("tg_id", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_name", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_phone", String(255, "utf8mb4_unicode_520_ci")),
    Column("create_at", DATETIME()),
    Column("update_at", DATETIME())
)