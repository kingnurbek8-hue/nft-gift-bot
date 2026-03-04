import telebot
from telebot import types

# BotFather'dan olgan tokenni shu yerga qo'ying
TOKEN = '8743861596:AAFN5YiHbRscPHxTwd_c2r0C6CzyM1gwzCw' 
bot = telebot.TeleBot(TOKEN)

# Tillardagi matnlar
strings = {
    'uz': {'welcome': "Xush kelibsiz!", 'open': "🎁 Case ochish"},
    'ru': {'welcome': "Добро пожаловать!", 'open': "🎁 Открыть кейс"},
    'en': {'welcome': "Welcome!", 'open': "🎁 Open Case"}
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🇺🇿 UZ", callback_data='l_uz'),
               types.InlineKeyboardButton("🇷🇺 RU", callback_data='l_ru'),
               types.InlineKeyboardButton("🇺🇸 EN", callback_data='l_en'))
    bot.send_message(message.chat.id, "Tilni tanlang / Select language:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('l_'))
def set_lang(call):
    lang = call.data.split('_')[1]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Bu linkni keyinroq GitHub Pages'dan olganingizda almashtirasiz
    web_app = types.WebAppInfo("https://kingnurbek8-hue.github.io/nft-gift-bot/") 
    markup.add(types.KeyboardButton(text=strings[lang]['open'], web_app=web_app))
    bot.send_message(call.message.chat.id, strings[lang]['welcome'], reply_markup=markup)

bot.polling()
