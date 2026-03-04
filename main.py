import telebot
from telebot import types

TOKEN = '8743861596:AAFN5YiHbRscPHxTwd_c2r0C6CzyM1gwzCw'
bot = telebot.TeleBot(TOKEN)

# DIQQAT: Linkni oxiridagi / bilan birga yozing
WEB_URL = "https://kingnurbek8-hue.github.io/nft-gift-bot/"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # WebApp tugmasi
    markup.add(types.InlineKeyboardButton("🚀 Play Epic Gift", web_app=types.WebAppInfo(WEB_URL)))
    
    # Pastdagi Menu tugmasini ham Play qilib qo'yamiz
    bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp("Play", types.WebAppInfo(WEB_URL)))
    
    bot.send_message(message.chat.id, 
        "<b>Welcome to Epic Gift Clone!</b>\n\nClick the button below to start.", 
        parse_mode="HTML", reply_markup=markup)

bot.polling(none_stop=True)
