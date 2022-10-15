from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ ʙᴏᴛ sᴛᴀᴛᴜs ✨", url="https://t.me/MYRAOFFICIAL")],
        [
            InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ ⌨️", callback_data="help"), 
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")      
        ], 
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs ☢️", url="https://t.me/TEACH_TEAMOP")],
    ]

    START = """
Hᴇʏ {}

Tʜɪs ɪs {} ❣,
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Sᴏᴜʀᴄᴇ :[ɢɪᴛʜᴜʙ](https://github.com/loveness/stringbot) 
Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ :[𝗦𝗧∆𝗥 𝗪𝗢𝗥𝗟𝗗](https://t.me/TG_STARWORLD) !
    """

    HELP = """
✨ **Available Commands** ✨

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ 
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ 
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/generate - ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss 
/restart - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    ABOUT = """
**𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭** 
ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @TEACH_TEAMOP

sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com)

ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](https://www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/TG_STARWORLD) 
    """
