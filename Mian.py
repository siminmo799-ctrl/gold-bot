import telebot

BOT_TOKEN = "8981002593:AAHPZvZmoMZSk2g0qD1-nmANtSV8JXGehzc"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ربات آنلاین شد ✅")

print("BOT RUNNING")

bot.infinity_polling()
