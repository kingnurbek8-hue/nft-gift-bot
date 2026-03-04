import telebot
from telebot import types

TOKEN = '8743861596:AAFN5YiHbRscPHxTwd_c2r0C6CzyM1gwzCw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # Web App manzilingizni to'g'ri yozing
    web_app = types.WebAppInfo("https://SAYTINGIZ_MANZILI.onrender.com")
    markup.add(types.InlineKeyboardButton("🚀 ENTER GAME", web_app=web_app))
    
    bot.send_message(message.chat.id, 
        "<b>Welcome to the Premium Pepe Case!</b>\n\n"
        "Click the button below to enter the game and claim your rewards.", 
        parse_mode="HTML", reply_markup=markup)

bot.polling(none_stop=True)
