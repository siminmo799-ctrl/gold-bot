import telebot

# توکن خود را در اینجا قرار دهید
BOT_TOKEN = "8940690033:AAExD0hcXejHxURX7aoz-WCXFIOxjy2WM7M" 

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ربات آنلاین شد ✅")

# این بخش برای جلوگیری از خطاهای تداخلی و اجرای پایدار است
if __name__ == "__main__":
    print("BOT RUNNING")
    bot.polling(none_stop=True, interval=0)

