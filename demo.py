import redis
import json

# 连接到 Redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 创建要发布的数据
data = {
    'tg_id': 6172193408,
    'tg_first_name': 'Dave',
    'tg_last_name': 'Lee',
    'tg_username': 'davelee32334',
    'tg_phone': '+18697435965',
    'create_time': 1721649336,
    'update_time': 1721649336,
    'time_at': '2024-07-22 11:55:36'
}

# 将数据序列化为 JSON 字符串
json_data = json.dumps(data)
print(json_data)
# 发布消息
r.publish('update_tg_user', json_data)
