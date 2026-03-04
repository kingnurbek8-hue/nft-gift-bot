import telebot
from telebot import types

TOKEN = '8743861596:AAFN5YiHbRscPHxTwd_c2r0C6CzyM1gwzCw'
bot = telebot.TeleBot(TOKEN)
WEB_URL = "https://kingnurbek8-hue.github.io/nft-gift-bot/"
@bot.message_handler(commands=['start'])
def start(message):
    bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp("Play", types.WebAppInfo(WEB_URL)))
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🚀 OPEN GAME", web_app=types.WebAppInfo(WEB_URL)))
    
    text = (
        "<b>Welcome to OnyxCrate!</b>\n\n"
        "🎁 Open Free24 Box every day\n"
        "🚀 Play Rocket and win rewards\n"
        "👇 Start playing right now!"
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)

bot.polling(none_stop=True)
