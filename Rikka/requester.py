from telethon.tl.types import ChannelParticipantsAdmins
from telethon.utils import get_display_name
from telethon import *
from . import API_ID, API_HASH, BOT_TOKEN, tbot, OWNER
from Rikka.events import register
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

IN_GRP = -1001657611433
bot = asst = tbot
REQ_GO =  -1001694591350
on = tbot.on
auth = OWNER


@tbot.on(events.NewMessage(chats=IN_GRP))
async def filter_requests(event):
    if event.fwd_from:
        return
    if "#request" in event.text:
      #  await asst.send_message(IN_GRP,
        #                    f"**We are not taking any requests for some days.\n\nSorry for inconvenience 😶**",
        #                    buttons=[
        #                        [Button.url("❗️MAIN CHANNEL", url="https://t.me/AnimeXWrld")]])
        if (event.reply_to_msg_id):
            msg = (await event.get_reply_message()).message
        else:
            msg = event.text
        try:
            global user
            sender = event.sender
            if sender.bot:
                return
            if not sender.username:
                user = f"[{get_display_name(sender)}](tg://user?id={event.sender_id})"
            else:
                user = "@" + str(sender.username)
        except BaseException:
            user = f"[User](tg://user?id={event.sender_id})"
        chat_id = (str(event.chat_id)).replace("-100", "")
        username = ((await bot.get_entity(REQ_GO)).username)
        hel_ = "#request"
        if hel_ in msg:
            global anim
            anim = msg.replace(hel_, "")
        x = await asst.send_message(REQ_GO,
                                f"**Request By {user}**\n\n{msg}",
                                buttons=[
                                    [Button.url("Requested Message", url=f"https://t.me/c/{chat_id}/{event.message.id}")],
                                    [Button.inline("🚫 Reject", data="reqdelete"),
                                    Button.inline("Done ✅", data="isdone")],
                                    [Button.inline("⚠️ UNAVAILABLE ⚠️", data="unavl")]])
        btns = [
            [Button.url("⏳ REQUEST STATUS ⏳", url=f"https://t.me/{username}/{x.id}")],
            [Button.url("❗️MAIN CHANNEL", url="https://t.me/AnimeXWrld"),
            [Button.url("INDEX📚", url="https://t.me/AnimeXWrld_Index")]]
        await event.reply(f"**👋 Hello {user} !!**\n\n🚀 Your Request for {anim} has been sended to the admins.\n\n**• Check Whether the Requested Anime is uploaded in Main Channel or Not**", buttons=btns)
        if not auth:
            async for x in bot.iter_participants("@AnimeXWrld", filter=ChannelParticipantsAdmins):
                auth.append(x.id)

@tbot.on(events.callbackquery.CallbackQuery(data="reqdelete"))
async def delete_message(event):
    if not auth:
        async for x in bot.iter_participants("@AnimeXWrld_Chat", filter=ChannelParticipantsAdmins):
             auth.append(x.id)
    if event.sender_id in auth:
        x = await bot.get_messages(event.chat_id, ids=event.message_id)
        xx = x.raw_text
        btns = [
            [Button.url("❗️MAIN CHANNEL", url="https://t.me/AnimeXWrld"),
            [Button.url("INDEX📚", url="https://t.me/AnimeXWrld_Index")]]
       
        await event.edit(f"**REJECTED**\n\n~~{xx}~~", buttons=[Button.inline("Request Rejected 🚫", data="ndone")])
        await tbot.send_message(-1001657611433, f"**⚠️ Request Rejected By An Admin !!**\n\n~~{xx}~~", buttons=btns)
    else:
        await event.answer("Only admins can access these", alert=True, cache_time=0)
        
@tbot.on(events.callbackquery.CallbackQuery(data="unavl"))
async def delete_message(event):
    if not auth:
        async for x in bot.iter_participants("@AnimeXWrld_Chat", filter=ChannelParticipantsAdmins):
             auth.append(x.id)
    if event.sender_id in auth:
        x = await bot.get_messages(event.chat_id, ids=event.message_id)
        xx = x.raw_text
        btns = [
            [Button.url("❗️MAIN CHANNEL", url="https://t.me/AnimeXWrld"),
            [Button.url("INDEX📚", url="https://t.me/AnimeXWrld_Index")]]
       
        await event.edit(f"**UNAVAILABLE**\n\n~~{xx}~~", buttons=[Button.inline("❗ Unavailable ❗", data="navl")])
        await tbot.send_message(-1001657611433, f"**⚠️ Request Unavailable ⚠️**\n\n~~{xx}~~", buttons=btns)
    else:
        await event.answer("Who TF are you? This is for admins only..", alert=True, cache_time=0)
        
        
@tbot.on(events.callbackquery.CallbackQuery(data="isdone"))
async def isdone(e):
    if not auth:
        async for x in bot.iter_participants("@AnimexWrld_Chat", filter=ChannelParticipantsAdmins):
             auth.append(x.id)
    if e.sender_id in auth:
        x = await bot.get_messages(e.chat_id, ids=e.message_id)
        xx = x.raw_text
        btns = [
            [Button.url("❗️MAIN CHANNEL", url="https://t.me/AnimeXWrld"),
            [Button.url("INDEX📚", url="https://t.me/AnimeXWrld_Index")]]
       
        await e.edit(f"**COMPLETED**\n\n~~{xx}~~", buttons=[Button.inline("Request Completed ✅", data="donne")])
        await tbot.send_message(-1001657611433, f"**Request Completed**\n\n~~{xx}~~", buttons=btns)
    else:
        await e.answer("Only admin can access these", alert=True, cache_time=0)
        
    
@tbot.on(events.callbackquery.CallbackQuery(data="donne"))
async def ans(e):
    await e.answer("Request has been completed ", alert=True, cache_time=0)
        
@tbot.on(events.callbackquery.CallbackQuery(data="navl"))
async def ans(e):
    await e.answer("This Request Is Marked Unavailable By Admins", alert=True, cache_time=0)
        
        
@tbot.on(events.callbackquery.CallbackQuery(data="ndone"))
async def ans(e):
    await e.answer("Unavailable Request", alert=True, cache_time=0)
