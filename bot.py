import os
import traceback
import logging
from pyrogram import Client, filters
from configs import Config as C

from pyrogram.types import *
from database.broadcast import broadcast
from database.verifier import handle_user_status
from database.database import Database

LOG_CHANNEL = C.LOG_CHANNEL
AUTH_USERS = C.AUTH_USERS
DB_URL = C.DB_URL
DB_NAME = C.DB_NAME

db = Database(DB_URL, DB_NAME)

bot = Client('Feedback bot',
             api_id=C.API_ID,
             api_hash=C.API_HASH,
             bot_token=C.BOT_TOKEN)
async def start(self):
  app = web.AppRunner(await web_server())
  await app.setup()
  bind_address = "0.0.0.0"
  await web.TCPSite(app, bind_address, PORT).start()

from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Join Telegram Channal @GreyMatter_Bots") 


donate_link=C.DONATE_LINK
owner_id=C.OWNER_ID
LOG_TEXT = "ɪᴅ: <code>{}</code>\n ғɪʀsᴛ ɴᴀᴍᴇ: <a href='tg://user?id={}'>{}{}</a>\n ᴅᴄ ɪᴅ: <code>{}</code>"
IF_TEXT = "<b>ᴍᴇssᴀɢᴇ ғʀᴏᴍ:</b> {}\n<b>ɴᴀᴍᴇ:</b> {}\n\n{}"
IF_CONTENT = "<b>ᴍᴇssᴀɢᴇ ғʀᴏᴍ:</b> {} \n<b>ɴᴀᴍᴇ:</b> {}"


START_TXT = """
<b>ʜᴇʏ {first} 💞 ᴋɪsᴇ ʜᴏ 

<blockquote>ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇǫᴜᴇsᴛ ᴀ ᴍᴏᴠɪᴇ/sᴇʀɪᴇs/ᴋᴅʀᴀᴍᴀ ᴛʜᴀᴛ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴏᴜʀ ʙᴏᴛs ᴏʀ ᴄʜᴀɴɴᴇʟs ᴊᴜsᴛ ᴅʀᴏᴘ ᴛʜᴇ ɴᴀᴍᴇ ᴀɴᴅ ᴘᴏsᴛᴇʀs ᴛʜᴀᴛs ɪᴛ</blockquote></b>"""

HELP_TXT = """
<b>ʜᴇʏ {first} ⚡ ᴋɪsᴇ ʜᴏ 

<blockquote>ɪᴛs ʀᴇᴀʟʟʏ ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴊᴜsᴛ sᴇɴᴅ ᴀɴʏ ɴᴀᴍᴇ ᴡɪᴛʜ ᴘᴏsᴛᴇʀ sᴏ ɪᴛ ᴡɪʟʟ ᴇᴀsʏ ғᴏʀ ᴛᴏ sᴇᴀʀᴄʜ ᴡᴇ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ғᴏʀ sᴜʀᴇ sᴏ ᴅᴏɴᴛ sᴘᴀᴍ</blockquote></b>"""

DONATE_TXT = """
<b>ʜᴇʏ {first} 💞 ᴋɪsᴇ ʜᴏ 

<blockquote>ʏᴇᴀʜ ᴛʜᴀɴᴋs ғᴏʀ ᴄʟɪᴄᴋɪɴɢ ᴛʜɪs ɪɴ ᴛʜᴇ ғɪʀsᴛ ᴘʟᴀᴄᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴏʀ ᴊᴜsᴛ ᴘᴀʏ ᴡɪᴛʜ ᴛʜᴇ ᴜᴘɪ ʙᴇʟᴏᴡ ᴘᴀʏ ᴡɪᴛʜ ᴜᴘɪ ᴀɴᴅ ʜᴇʟᴘ ᴜs ɢʀᴏᴡ ᴇᴠᴇɴ ᴍᴏʀᴇ ⚡</blockquote>

ᴜᴘɪ ɪᴅ - <code>titanindia@ibl</code></b>"""

@bot.on_callback_query()
async def callback_handlers(bot: Client, cb: CallbackQuery):
    user_id = cb.from_user.id
    if "closeMeh" in cb.data:
        await cb.message.delete(True)
    elif "notifon" in cb.data:
        notif = await db.get_notif(cb.from_user.id)
        if notif is True:
            # 
            await db.set_notif(user_id, notif=False)
        else:
            # 
            await db.set_notif(user_id, notif=True)
        await cb.message.edit(
            f"`Here You Can Set Your Settings:`\n\nSuccessfully setted notifications to **{await db.get_notif(user_id)}**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            f"ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
                            callback_data="notifon",
                        )
                    ],
                    [InlineKeyboardButton("💫 ᴄʟᴏsᴇ", callback_data="closeMeh")],
                ]
            ),
        )
        await cb.answer(
            f"sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛᴛᴇᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴs ᴛᴏ {await db.get_notif(user_id)}"
        )
        
        
@bot.on_message((filters.private | filters.group))
async def _(bot, cmd):
    await handle_user_status(bot, cmd)

@bot.on_message(filters.command('start') & (filters.private | filters.group))
async def start(bot, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"#ɴᴇᴡᴜsᴇʀ: \n\n ɴᴇᴡ ᴜsᴇʀ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) sᴛᴀʀᴛᴇᴅ @{BOT_USERNAME} !!",
        )
        return
    
    ban_status = await db.get_ban_status(chat_id)   
    is_banned = ban_status.get('is_banned', False)
    if is_banned:
        ban_duration = ban_status.get('ban_duration', 'ᴜɴᴋɴᴏᴡɴ')
        ban_reason = ban_status.get('ban_reason', 'ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ')
        await message.reply_text(f"ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ 🚫 ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ **{ban_duration}** ᴅᴀʏ(s) ғᴏʀ ᴛʜᴇ ʀᴇᴀsᴏɴ __{ban_reason}__ \n\n**ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀᴅᴍɪɴ 🤠**")
        return
    
    await message.reply_text(
        text=START_TXT.format(first=message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup([
            [ 
              InlineKeyboardButton("ᴛɪᴛᴀɴ ᴄᴏᴍᴍᴜɴɪᴛʏ", url="https://t.me/Titan_Community_India")
            ]
        ])
    )
  
@bot.on_message(filters.command('help') & (filters.group | filters.private))
async def help(bot, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
        )
   
    ban_status = await db.get_ban_status(chat_id)    
    is_banned = ban_status.get('is_banned', False)
    if is_banned:
        ban_duration = ban_status.get('ban_duration', 'ᴜɴᴋɴᴏᴡɴ')
        ban_reason = ban_status.get('ban_reason', 'ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ')
        await message.reply_text(f"ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ 🚫 ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ **{ban_duration}** ᴅᴀʏ(s) ғᴏʀ ᴛʜᴇ ʀᴇᴀsᴏɴ __{ban_reason}__ \n\n**ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀᴅᴍɪɴ 🤠**")
        return
      
    await message.reply_text(
        text=HELP_TXT.format(first=message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup([
            [ 
              InlineKeyboardButton("ᴛɪᴛᴀɴ ᴄᴏᴍᴍᴜɴɪᴛʏ", url="https://t.me/Titan_Community_India")
            ]
        ])
    )
@bot.on_message(filters.command('donate') & (filters.group | filters.private))
async def donate(bot, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
        )
    
    ban_status = await db.get_ban_status(chat_id)
    
    is_banned = ban_status.get('is_banned', False)
    if is_banned:
        ban_duration = ban_status.get('ban_duration', 'ᴜɴᴋɴᴏᴡɴ')
        ban_reason = ban_status.get('ban_reason', 'ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ')
        await message.reply_text(f"ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ 🚫 ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ **{ban_duration}** ᴅᴀʏ(s) ғᴏʀ ᴛʜᴇ ʀᴇᴀsᴏɴ __{ban_reason}__ \n\n**ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀᴅᴍɪɴ 🤠**")
        return
      
    await message.reply_text(
        text=DONATE_TXT.format(first=message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup([
            [ 
              InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ", url="https://t.me/Titan_Community_India")
            ]
        ])
    )

@bot.on_message(filters.command("settings") & filters.private)
async def opensettings(bot, cmd):
    user_id = cmd.from_user.id
    # Adding to DB
    if not await db.is_user_exist(user_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(user_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"#NEWUSER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{BOT_USERNAME} !!",
        )
    try:
        await cmd.reply_text(
            text=f"⚙ `ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ sᴇᴛ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs:` ⚙\n\n sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛᴛᴇᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴs ᴛᴏ **{await db.get_notif(user_id)}**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text=f"ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",callback_data="notifon")],
                    [InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="closeMeh")],
                ]
            )
        )
    except Exception as e:
        await cmd.reply_text(e)


@bot.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
        return
    await broadcast(m, db)


@bot.on_message((filters.group | filters.private) & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**ᴛᴏᴛᴀʟ ᴜsᴇʀs ɪɴ ᴅᴀᴛᴀʙᴀsᴇ 📂:** `{await db.total_users_count()}`\n\n**ᴛᴏᴛᴀʟ ᴜsᴇʀs ᴡɪᴛʜ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ 🔔 :** `{await db.total_notif_users_count()}`",
        quote=True,
    )


@bot.on_message(filters.private & filters.command("ban_user"))
async def ban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban 🛑 any user from the bot 🤖.\n\nUsage:\n\n`/ban_user user_id ban_duration ban_reason`\n\nEg: `/ban_user 1234567 28 You misused me.`\n This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."
        
        if user_id == owner_id:
            await m.reply_text("**You can Ban The Owner Vro")
            return
        try:
            await c.send_message(
                user_id,
                f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**",
            )
            ban_log_text += "\n\nUser notified successfully!"
        except BaseException:
            traceback.print_exc()
            ban_log_text += (
                f"\n\n ⚠️ User notification failed! ⚠️ \n\n`{traceback.format_exc()}`"
            )
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True,
        )


@bot.on_message((filters.group | filters.private) & filters.command("unban_user"))
async def unban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban 😃 any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user 🤪 {user_id}"

        try:
            await c.send_message(user_id, f"Your ban was lifted!")
            unban_log_text += "\n\n✅ User notified successfully! ✅"
        except BaseException:
            traceback.print_exc()
            unban_log_text += (
                f"\n\n⚠️ User notification failed! ⚠️\n\n`{traceback.format_exc()}`"
            )
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"⚠️ Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True,
        )


@bot.on_message((filters.group | filters.private) & filters.command("banned_users"))
async def _banned_usrs(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_status = banned_user.get("ban_status", {})
        ban_duration = ban_status.get("ban_duration", "Unknown")
        banned_on = ban_status.get("banned_on", "Unknown")
        ban_reason = ban_status.get("ban_reason", "No reason provided")
        
        banned_usr_count += 1
        text += f"> **User_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, **Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"
    
    reply_text = f"Total banned user(s) 🤭: `{banned_usr_count}`\n\n{text}"    
    if len(reply_text) > 4096:
        with open("banned-users.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-users.txt", True)
        os.remove("banned-users.txt")
        return
      
    await m.reply_text(reply_text, True)

@bot.on_message((filters.group | filters.private) & filters.text)
async def pm_text(bot, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
        )
    
    ban_status = await db.get_ban_status(chat_id)
    
    is_banned = ban_status.get('is_banned', False)
    if is_banned:
        ban_duration = ban_status.get('ban_duration', 'unknown')
        ban_reason = ban_status.get('ban_reason', 'No reason provided')
        await message.reply_text(f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**")
        return
      
    if message.from_user.id == owner_id:
        await reply_text(bot, message)
        return
    
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=owner_id,
        text=IF_TEXT.format(reference_id, info.first_name, message.text),
    )

@bot.on_message((filters.group | filters.private) & filters.media_group)
async def pm_media_group(bot, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
        )
    
    ban_status = await db.get_ban_status(chat_id)
    
    is_banned = ban_status.get('is_banned', False)
    if is_banned:
        ban_duration = ban_status.get('ban_duration', 'unknown')
        ban_reason = ban_status.get('ban_reason', 'No reason provided')
        await message.reply_text(f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**")
        return
      
    if message.from_user.id == owner_id:
        await replay_media(bot, message)
        return
    
    reference_id = int(message.chat.id)
    await bot.copy_media_group(chat_id=owner_id, from_chat_id=reference_id, message_id=message.message_id)

@bot.on_message((filters.group | filters.private) & filters.media)
async def pm_media(_, message):
    try:
        chat_id = message.from_user.id
        
        if not await db.is_user_exist(chat_id):
            data = await bot.get_me()
            BOT_USERNAME = data.username
            await db.add_user(chat_id)
            await bot.send_message(
                LOG_CHANNEL,
                f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
            )
        
        ban_status = await db.get_ban_status(chat_id)
        
        is_banned = ban_status.get('is_banned', False)
        if is_banned:
            ban_duration = ban_status.get('ban_duration', 'unknown')
            ban_reason = ban_status.get('ban_reason', 'No reason provided')
            await message.reply_text(f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**")
            return
          
        if message.from_user.id == owner_id:
            await replay_media(bot, message)
            return
        
        info = await bot.get_users(user_ids=message.from_user.id)
        reference_id = int(message.chat.id)
        
        if message.media_group_id is not None:
            print(f"Handling media group with ID: {message.media_group_id}")
            media = []
            async for m in bot.iter_history(message.chat.id, message.media_group_id):
                if m.media:
                    media.append(m.media)
            await bot.send_media_group(chat_id=owner_id, media=media)
        else:
            await bot.copy_message(
                chat_id=owner_id,
                from_chat_id=message.chat.id,
                message_id=message.id,
                caption=IF_CONTENT.format(reference_id, info.first_name),
            )
    
    except Exception as e:
        print(f"Error in pm_media command: {e}")


@bot.on_message(filters.user(owner_id) & filters.text)
async def reply_text(bot, message):
    chat_id = message.from_user.id
    try:
        if not await db.is_user_exist(chat_id):
            data = await bot.get_me()
            BOT_USERNAME = data.username
            await db.add_user(chat_id)
            await bot.send_message(
                LOG_CHANNEL,
                f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
            )
        
        reference_id = None
        if message.reply_to_message:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
        
        if reference_id:
            await bot.send_message(
                chat_id=int(reference_id),
                text=message.text
            )
        else:
            await bot.send_message(
                chat_id=message.chat.id,
                text="No valid reference ID found."
            )
    
    except Exception as e:
        print(f"Error in reply_text command: {e}")

@bot.on_message(filters.user(owner_id) & filters.media)
async def replay_media(bot, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
        )
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        if message.media_group_id is not None:
            await bot.copy_message(
                chat_id=int(reference_id),
                from_chat_id=message.chat.id,
                message_id=message.id,
                caption=message.caption,
    
            )
        else:
            await bot.copy_message(
                chat_id=int(reference_id),
                from_chat_id=message.chat.id,
                message_id=message.id,
            )

if __name__ == "__main__":
    print("---------- ** Bot Started ** ----------")
    bot.run()
