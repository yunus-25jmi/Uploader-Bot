from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
👋 Hᴇʏ {} ♡

I ᴀᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ

Usᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ

Pᴏᴡᴇʀᴇᴅ ʙʏ : [Tᴇʟʟʏʙᴏᴛs](https://telegram.me/TellyBots)
"""
    HELP_TEXT = """
ʟɪɴᴋ ᴛᴏ ᴍᴇᴅɪᴀ ᴏʀ ғɪʟᴇ

➠ sᴇɴᴅ ᴀ ʟɪɴᴋ ғᴏʀ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ.

sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴀs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ /delthumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ.

sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ /showthumb ᴛᴏ ᴠɪᴇᴡ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.

Pᴏᴡᴇʀᴇᴅ ʙʏ : [Tᴇʟʟʏʙᴏᴛs](https://telegram.me/TellyBots)
 
"""
    ABOUT_TEXT = """
**Mʏ ɴᴀᴍᴇ** : [ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ](http://t.me/TellyUploaderRobot)

**Cʜᴀɴɴᴇʟ** : [Tᴇʟʟʏʙᴏᴛs](https://t.me/TellyBots)

**Vᴇʀꜱɪᴏɴ** : [2.0 ʙᴇᴛᴀ](https://t.me/TellyUploaderRobot)

**Sᴏᴜʀᴄᴇ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/tellybots_digital)

**Sᴇʀᴠᴇʀ** : [ʜᴇʀᴏᴋᴜ](https://heroku.com/)

**Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 3.10.2](https://www.python.org/)

**Fʀᴀᴍᴇᴡᴏʀᴋ :** [ᴘʏʀᴏɢᴀᴍ 1.3.6](https://docs.pyrogram.org/)

**Dᴇᴠᴇʟᴏᴘᴇʀ :** [Tᴇʟʟʏʙᴏᴛs](https://t.me/tellybots)

**Pᴏᴡᴇʀᴇᴅ ʙʏ :** [NᴀʏsᴀBᴏᴛs](https://t.me/NaysaBots)

"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' ᴜᴘᴅᴀᴛᴇs', url='https://telegram.me/Tellybots'),
        InlineKeyboardButton(' sᴜᴘᴘᴏʀᴛ', url='https://telegram.me/Tellybots')
        ],[
        InlineKeyboardButton(' ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton(' ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton(' ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton(' ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton(' ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton(' ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton(' ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )


