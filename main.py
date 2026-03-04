import telebot
from telebot import types

TOKEN = 'BOT_TOKENINGIZ'
bot = telebot.TeleBot(TOKEN)

# Botni ochganda pastda katta tugma turishi uchun
@bot.message_handler(commands=['start'])
def start(message):
    # Web App manzilingiz
    web_app_url = "https://SAYTINGIZ_MANZILI.onrender.com"
    
    # 1. Chat ichidagi tugma
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🚀 START GAME", web_app=types.WebAppInfo(web_app_url)))
    
    # 2. Pastki Menu tugmasini o'zgartirish (Siz xohlagan narsa)
    bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp("Play", types.WebAppInfo(web_app_url)))
    
    bot.send_message(message.chat.id, "<b>Welcome!</b>\nPress the button below to start.", parse_mode="HTML", reply_markup=markup)

bot.polling(none_stop=True)
