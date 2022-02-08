from rose import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

supunma = """
**👮‍♀️Basic Menu**

✘ Base commands are the basic tools of DevilAngel Bot which help you to manage 
your group easily and effectivelyYou can choose an option below, 
by clicking a button.Also you can ask anything in [Support Group](https://t.me/DevilAngelSupport).

Click buttons to get help ?
"""

mbuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton
                (
                    "ᴀᴅᴍɪɴ", callback_data="_admin"
                ),            
            InlineKeyboardButton
                (
                    "ᴀɴᴛɪ-ᴄʜᴀɴɴᴇʟ", callback_data="_antichannel"
                ),
            InlineKeyboardButton
                (
                    "ᴀɴᴛɪ-ʟᴀɴɢs", callback_data="_antilangs"
                )   
        ],
        [
            InlineKeyboardButton
                (
                    "ᴀɴᴛɪ-sᴇʀᴠɪᴄᴇ", callback_data="_antiservice"
                ),            
            InlineKeyboardButton
                (
                    "ᴅɪsᴀʙʟɪɴɢ", callback_data="_disabling"
                ),
            InlineKeyboardButton
                (
                    "ꜰɪʟᴛᴇʀs", callback_data="_filters"
                )   
        ],       
        [
            InlineKeyboardButton
                (
                    "ꜰʟᴏᴏᴅ", callback_data="_flood"
                ),            
            InlineKeyboardButton
                (
                    "ɢʀᴇᴇᴛɪɴɢs", callback_data="_Greetings"
                ),
            InlineKeyboardButton
                (
                    "ᴜʀʟ-ʟᴏᴄᴋ", callback_data="_groups"
                )   
        ],
        [
            InlineKeyboardButton
                (
                    "ʟᴏᴄᴋs", callback_data="_locks"
                ),            
            InlineKeyboardButton
                (
                    "ɴᴏᴛᴇs", callback_data="_notes"
                ),
            InlineKeyboardButton
                (
                    "ᴘᴏʀɴ-ᴅᴇᴛᴇᴄᴛ", callback_data="_porn"
                )   
        ],
        [
            InlineKeyboardButton
                (
                    "ʀᴇᴘᴏʀᴛ", callback_data="_report"
                ),            
            InlineKeyboardButton
                (
                    "ʀᴜʟᴇs", callback_data="_rules"
                ),
            InlineKeyboardButton
                (
                    "sᴘᴀᴍ-ᴅᴇᴛᴇᴄᴛ", callback_data="_spam"
                )   
        ],
        [
            InlineKeyboardButton
                (
                    "🔻ʙᴀᴄᴋ🔻", callback_data="bot_commands"
                )
        ]
    ]
)
    


        
@app.on_callback_query(filters.regex("basic_menu"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunma,
        reply_markup=mbuttons,
        disable_web_page_preview=True,    
    )
    await CallbackQuery.message.delete()
