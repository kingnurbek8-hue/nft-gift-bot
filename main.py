import telebot
from telebot import types

# O'z tokeningizni ehtiyotkorlik bilan qo'ying
TOKEN = '8743861596:AAFN5YiHbRscPHxTwd_c2r0C6CzyM1gwzCw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Diqqat! Bu yerga o'zingizning Render saytingiz manzilini yozing
    # Masalan: https://nft-gift-bot.onrender.com
    web_app_url = "https://kingnurbek8-hue.github.io/nft-gift-bot/"

    markup = types.InlineKeyboardMarkup()
    # Chat ichidagi asosiy tugma
    markup.add(types.InlineKeyboardButton("🚀 ENTER GAME", web_app=types.WebAppInfo(web_app_url)))
    
    # Pastdagi menyu tugmasini "Play" ga aylantirish
    try:
        bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp("Play", types.WebAppInfo(web_app_url)))
    except:
        pass

    bot.send_message(message.chat.id, 
        "<b>Welcome to Premium Pepe Case!</b>\n\nClick the button below to start the game.", 
        parse_mode="HTML", reply_markup=markup)

bot.polling(none_stop=True)
