from sqlalchemy import Table, MetaData, Column, INTEGER, String, DATETIME, Text, VARCHAR
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

t_tg_users = Table(
    "tg_users",
    metadata,
    Column("id", INTEGER(), primary_key=True, autoincrement=True),
    Column("tg_id", BIGINT()),
    Column("tg_first_name", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_last_name", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_username", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_phone", String(255, "utf8mb4_unicode_520_ci")),
    Column("create_time", String(255, "utf8mb4_unicode_520_ci")),
    Column("update_time", String(255, "utf8mb4_unicode_520_ci")),
    Column("time_at", DATETIME()),
)


t_lumoz_tg_users = Table(
    "lumoz_tg_users",
    metadata,
    Column("id", INTEGER(), primary_key=True, autoincrement=True),
    Column("tg_id", INTEGER()),
    Column("user_id", INTEGER()),
    Column("tg_first_name", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_last_name", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_username", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_phone", String(255, "utf8mb4_unicode_520_ci")),
    Column("create_time", String(255, "utf8mb4_unicode_520_ci")),
    Column("update_time", String(255, "utf8mb4_unicode_520_ci")),
    Column("chain", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_code", INTEGER()),
    Column("time_at", DATETIME()),
)

t_lumoz_tg_users_info = Table(
    "lumoz_tg_users_info",
    metadata,
    Column("id", INTEGER(), primary_key=True, autoincrement=True),
    Column("tg_id", BIGINT()),
    Column("tg_first_name", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_last_name", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_username", String(255, "utf8mb4_unicode_520_ci")),
    Column("tg_phone", String(255, "utf8mb4_unicode_520_ci")),
    Column("create_time", String(255, "utf8mb4_unicode_520_ci")),
    Column("update_time", String(255, "utf8mb4_unicode_520_ci")),
    Column("time_at", DATETIME()),
)

t_users = Table(
    "users",
    metadata,
    Column("id", BIGINT(), primary_key=True),
    Column("username", Text(4, "utf8mb4_unicode_ci")),
    Column("avatar", Text(100, "utf8mb4_unicode_ci")),
    Column("create_time", BIGINT(20)),
    Column("discord_id", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("twitter_id", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("twitter_token", VARCHAR(512, "utf8mb4_unicode_ci")),
    Column("twitter_name", VARCHAR(512, "utf8mb4_unicode_ci")),
    Column("twitter_username", VARCHAR(512, "utf8mb4_unicode_ci")),
    Column("discord_name", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("country", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("email", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("verified", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("tg_id", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("tg_username", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("address", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("platform", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("selected_icon", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("chain", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("discord_code", VARCHAR(255, "utf8mb4_unicode_ci")),
    Column("tg_code", VARCHAR(255, "utf8mb4_unicode_ci")),
)