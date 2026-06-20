import telebot

BOT_TOKEN = "8940690033:AAExD0hcXejHxURX7aoz-WCXFIOxjy2WM7M"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ربات آنلاین شد ✅")

print("BOT RUNNING")

bot.infinity_polling()
