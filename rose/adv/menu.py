from rose import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

supunma = """
👨‍🔧 **Advanced Menu**

✘ Advanced commands will help you to secure your groups 
from attackers and do many stuff in group from a single bot
You can choose an option below, by clicking a button.
Also you can ask anything in [Support Group](https://t.me/DevilAngelSupport).

Click buttons to get help ?
"""

mbuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton
                (
                    "ᴄᴀᴘᴛᴄʜᴀ 🧠", callback_data="_cap"
                ),            
            InlineKeyboardButton
                (
                    "ʟᴏɢᴏ ᴛᴏᴏʟs 🧰", callback_data="_logo"
                )
        ],
        [
            InlineKeyboardButton
                (
                    "🔊 ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ", callback_data="_vc"
                ),            
            InlineKeyboardButton
                (
                    "sᴛʀɪɴɢ ɢᴇɴ💈", callback_data="_telegram"
                ),  
        ],       
        [
            InlineKeyboardButton
                (
                    "🔙 ʙᴀᴄᴋ", callback_data="bot_commands"
                )
        ]
    ]
)
    

@app.on_callback_query(filters.regex("adv_menu"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunma,
        reply_markup=mbuttons,
        disable_web_page_preview=True,    
    )
    await CallbackQuery.message.delete()
