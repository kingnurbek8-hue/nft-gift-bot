import telebot
from telebot import types

TOKEN = '8743861596:AAFN5YiHbRscPHxTwd_c2r0C6CzyM1gwzCw'
CHANNEL_ID = '@https://t.me/+Pm19j-nmUzUzZmNl' # Majburiy obuna uchun kanal
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Foydalanuvchi birinchi marta kirganda balans 0
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo("https://SAYTINGIZ_MANZILI.onrender.com")
    markup.add(types.InlineKeyboardButton("🎮 Play Epic Gift", web_app=web_app))
    
    bot.send_message(message.chat.id, 
        "🚀 Welcome to Epic Gift!\n\n"
        "💰 Your balance: 0.00 TON\n"
        "🎁 Open cases and win unique rewards!", 
        reply_markup=markup)

# WebApp'dan keladigan ma'lumotlarni tutish
@bot.message_handler(content_types=['web_app_data'])
def web_app(message):
    if message.web_app_data.data == "check_subscription_and_open_pepe":
        user_id = message.from_user.id
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        
        if status in ['member', 'administrator', 'creator']:
            bot.send_message(user_id, "✅ You are a member! Pepe Case is opening...")
        else:
            bot.send_message(user_id, f"❌ Please join {CHANNEL_ID} to open the free case!")

bot.polling(none_stop=True)
