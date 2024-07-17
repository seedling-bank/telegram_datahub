# from telethon.sync import TelegramClient
# from telethon.tl.types import InputPeerEmpty
#
# # 填入你的 Telegram API credentials
# api_id = 20464789
# api_hash = "87c3a2090b3c3fd98ea22da5e4d39a44"
#
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



# from telethon.sync import TelegramClient
# from telethon.tl.types import InputPeerChat
#
# # 填入你的 Telegram API credentials
# api_id = 20464789
# api_hash = "87c3a2090b3c3fd98ea22da5e4d39a44"
#
#
# async def get_group_members_tgid(chat_id):
#     async with TelegramClient('session_name', api_id, api_hash) as client:
#         # 获取群组成员列表
#         participants = await client.get_participants(chat_id)
#
#         # 提取成员的 Telegram ID
#         member_ids = [participant.id for participant in participants]
#
#         return member_ids
#
#
# async def main():
#     # 假设你的群组的 chat_id 是 -1001234567890 （负号表示是一个群组）
#     # chat_id = 1002080008623
#     chat_id = 4140777618
#     client = TelegramClient("session", api_id, api_hash)
#     await client.connect()
#     # 获取群组成员的 Telegram ID
#
#     res = await client.get_entity(chat_id)
#
#     member_ids = await client.get_participants(res)
#     for member in member_ids:
#         print(member.id)
#         print(member.first_name)
#         print(member.last_name)
#         print(member.username)
#         print(member.phone)
#         print(member)
#
#
# if __name__ == '__main__':
#     import asyncio
#
#     asyncio.run(main())