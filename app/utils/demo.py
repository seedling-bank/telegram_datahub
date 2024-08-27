import asyncio

import loguru
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty

api_id = 20464789  # 你的 api_id
api_hash = '87c3a2090b3c3fd98ea22da5e4d39a44'  # 你的 api_hash

client = TelegramClient('aaaaaaaaa', api_id, api_hash)

# import asyncio
# from telethon import TelegramClient
from loguru import logger

# 你需要替换下面的值为你的实际API id和hash，以及Bot Token或用户session名称
# api_id = 'YOUR_API_ID'
# api_hash = 'YOUR_API_HASH'
# # session_name = 'YOUR_SESSION_NAME_OR_BOT_TOKEN'
#
# client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()

    me = await client.get_me()
    logger.info(me.stringify())

    username = me.username
    logger.info(username)
    logger.info(me.phone)

    async for dialog in client.iter_dialogs():
        logger.info(dialog)
        try:
            logger.debug(f"{dialog.name} {dialog.id} {dialog.message.peer_id.channel_id} {dialog.pinned}")
        except Exception as e:
            print(e)

    await client.disconnect()

# 运行异步主函数
loop = asyncio.get_event_loop()
loop.run_until_complete(main())



"""Dialog(name='lumoz&deagent', date=datetime.datetime(2024, 8, 27, 3, 29, 13, tzinfo=datetime.timezone.utc), 
draft=<telethon.tl.custom.draft.Draft object at 0x1033ffe20>, message=Message(id=15576, peer_id=PeerChat(
chat_id=4273021899), date=datetime.datetime(2024, 8, 27, 3, 29, 13, tzinfo=datetime.timezone.utc), message='ok', 
out=True, mentioned=False, media_unread=False, silent=False, post=False, from_scheduled=False, legacy=False, 
edit_hide=False, pinned=False, noforwards=False, invert_media=False, offline=False, from_id=PeerUser(
user_id=6968848547), from_boosts_applied=None, saved_peer_id=None, fwd_from=None, via_bot_id=None, 
via_business_bot_id=None, reply_to=None, media=None, reply_markup=None, entities=[], views=None, forwards=None, 
replies=None, edit_date=None, post_author=None, grouped_id=None, reactions=None, restriction_reason=[], 
ttl_period=None, quick_reply_shortcut_id=None, effect=None, factcheck=None), entity=Chat(id=4273021899, 
title='lumoz&deagent', photo=ChatPhotoEmpty(), participants_count=12, date=datetime.datetime(2024, 8, 13, 16, 19, 23, 
tzinfo=datetime.timezone.utc), version=12, creator=False, left=False, deactivated=False, call_active=False, 
call_not_empty=False, noforwards=False, migrated_to=None, admin_rights=None, default_banned_rights=ChatBannedRights(
until_date=datetime.datetime(2038, 1, 19, 3, 14, 7, tzinfo=datetime.timezone.utc), view_messages=False, 
send_messages=False, send_media=False, send_stickers=False, send_gifs=False, send_games=False, send_inline=False, 
embed_links=False, send_polls=False, change_info=False, invite_users=False, pin_messages=False, manage_topics=False, 
send_photos=False, send_videos=False, send_roundvideos=False, send_audios=False, send_voices=False, send_docs=False, 
send_plain=False)))


Dialog(name='madras', date=datetime.datetime(2024, 8, 26, 9, 49, 45, tzinfo=datetime.timezone.utc), 
draft=<telethon.tl.custom.draft.Draft object at 0x10340d210>, message=MessageService(id=15536, peer_id=PeerChat(
chat_id=4534839336), date=datetime.datetime(2024, 8, 26, 9, 49, 45, tzinfo=datetime.timezone.utc), 
action=MessageActionChatCreate(title='madras', users=[6968848547]), out=True, mentioned=False, media_unread=False, 
silent=False, post=False, legacy=False, from_id=PeerUser(user_id=6968848547), reply_to=None, ttl_period=None), 
entity=Chat(id=4534839336, title='madras', photo=ChatPhotoEmpty(), participants_count=1, date=datetime.datetime(2024, 
8, 26, 9, 49, 45, tzinfo=datetime.timezone.utc), version=1, creator=True, left=False, deactivated=False, 
call_active=False, call_not_empty=False, noforwards=False, migrated_to=None, admin_rights=None, 
default_banned_rights=ChatBannedRights(until_date=datetime.datetime(2038, 1, 19, 3, 14, 7, 
tzinfo=datetime.timezone.utc), view_messages=False, send_messages=False, send_media=False, send_stickers=False, 
send_gifs=False, send_games=False, send_inline=False, embed_links=False, send_polls=False, change_info=False, 
invite_users=False, pin_messages=False, manage_topics=False, send_photos=False, send_videos=False, 
send_roundvideos=False, send_audios=False, send_voices=False, send_docs=False, send_plain=False)))


Dialog(name='Lumoz Official', date=datetime.datetime(2024, 8, 27, 3, 36, 58, tzinfo=datetime.timezone.utc), 
draft=<telethon.tl.custom.draft.Draft object at 0x1058ca950>, message=Message(id=3, peer_id=PeerChannel(
channel_id=2210488432), date=datetime.datetime(2024, 8, 27, 3, 36, 58, tzinfo=datetime.timezone.utc), message="🏆 
Lumoz Quidditch Match: Ready to Fly? 🏆 \n\nAttention Lumoz Wizards and Witches! 🧙\u200d♂️✨\n\n🧹The Lumoz Quidditch 
Match is taking off faster than a Firebolt on game day!  It’s time to grab your brooms, put on your best robes, 
and dive into the action!\n\n🎯 Warm-up details: 
https://mirror.xyz/lumozorg.eth/SBZooo8YTruooogaEJ84Kudprsz96LOl0Pl_GVYRoCw\n\n🔥 Don't forget to join Lumoz's 
official Telegram channel to learn more: https://t.me/Lumozannouncement\n\n🚨 You may find the entrance to the Lumoz 
Quidditch Bot, but please note that the event will officially start on August 27, at 4:00 PM UTC+8, and the data 
before the official start will be cleared~ However, understanding the bot in advance will help you win the Lumoz 
Quidditch Match!\n\nLet the games begin! ⚡️", out=False, mentioned=False, media_unread=False, silent=False, 
post=True, from_scheduled=False, legacy=False, edit_hide=False, pinned=False, noforwards=False, invert_media=False, 
offline=False, from_id=None, from_boosts_applied=None, saved_peer_id=None, fwd_from=None, via_bot_id=None, 
via_business_bot_id=None, reply_to=None, media=MessageMediaPhoto(spoiler=False, photo=Photo(id=6226559048908653805, 
access_hash=-1305599879710995762, file_reference=b'\x05\x00\x00\x00\x00\x83\xc1`p\x00\x00\x00\x03f\xcde\xf4a\xf3
\x9397S\x7f\xdfV\x85\xb1\x01\x8e%%\xb3', date=datetime.datetime(2024, 8, 27, 3, 36, 58, 
tzinfo=datetime.timezone.utc), sizes=[PhotoStrippedSize(type='i', bytes=b"\x01\x17(\xaa\x9f(
\xe3\xa7qR\x90\x08$d\xfbS!\x90\x01\x82\x07=\xf1V7\x0c\x8cm\xfc\x87\xf8\xd6m\x94\x88ve\xb0\xa0\xd4\xa2\xd0\x95'\xa6zQ
\xe6\xa1\x90\r\xbc\x93\xdb\x8cU\xfc\xab(\xe7\xe9S)43\x16\xe2\x12\x9d\xb8\xed\xefEX\xd4\x08\xcf\xaf\xbeh\xaaM\xb4'b
\x9a7\xcbN\xf3;d\xfa\xd1E6\x01\xe6u\xebO\xfb[\x80@8\xa2\x8a,\x04\x12\xc8]\x894QE4\x07"), PhotoSize(type='m', w=320, 
h=180, size=15971), PhotoSize(type='x', w=800, h=450, size=66967), PhotoSizeProgressive(type='y', w=1280, h=720, 
sizes=[13508, 34818, 50414, 76446, 125590])], dc_id=5, has_stickers=False, video_sizes=[]), ttl_seconds=None), 
reply_markup=None, entities=[MessageEntityBold(offset=0, length=43), MessageEntityUrl(offset=271, length=75), 
MessageEntityUrl(offset=421, length=30), MessageEntityBold(offset=739, length=23)], views=17, forwards=0, 
replies=None, edit_date=datetime.datetime(2024, 8, 27, 5, 8, 17, tzinfo=datetime.timezone.utc), post_author=None, 
grouped_id=None, reactions=None, restriction_reason=[], ttl_period=None, quick_reply_shortcut_id=None, effect=None, 
factcheck=None), entity=Channel(id=2210488432, title='Lumoz Official', photo=ChatPhoto(photo_id=5904508592734717071, 
dc_id=4, has_video=False, stripped_thumb=b'\x01\x08\x08\xcd\x8aD\x893\x83\xbe\x8a(\xa5\xca\x85c'), 
date=datetime.datetime(2024, 8, 27, 5, 29, 54, tzinfo=datetime.timezone.utc), creator=False, left=False, 
broadcast=True, verified=False, megagroup=False, restricted=False, signatures=False, min=False, scam=False, 
has_link=False, has_geo=False, slowmode_enabled=False, call_active=False, call_not_empty=False, fake=False, 
gigagroup=False, noforwards=True, join_to_send=False, join_request=False, forum=False, stories_hidden=False, 
stories_hidden_min=False, stories_unavailable=True, access_hash=-2784474769857460999, username='Lumozannouncement', 
restriction_reason=[], admin_rights=None, banned_rights=None, default_banned_rights=None, participants_count=19, 
usernames=[], stories_max_id=None, color=None, profile_color=None, emoji_status=None, level=None))

"""