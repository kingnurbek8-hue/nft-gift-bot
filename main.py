import telebot
from telebot import types

TOKEN = '8743861596:AAFN5YiHbRscPHxTwd_c2r0C6CzyM1gwzCw'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    
    web_app_url = "https://https://t.me/OnyxCratebot"
    

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🚀 START GAME", web_app=types.WebAppInfo(web_app_url)))
    
    
    bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp("Play", types.WebAppInfo(web_app_url)))
    
    bot.send_message(message.chat.id, "<b>Welcome!</b>\nPress the button below to start.", parse_mode="HTML", reply_markup=markup)

bot.polling(none_stop=True)
