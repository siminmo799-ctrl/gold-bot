import telebot
import os
from flask import Flask
from threading import Thread

# تنظیمات ربات
BOT_TOKEN = "8940690033:AAExD0hcXejHxURX7aoz-WCXFIOxjy2WM7M"
bot = telebot.TeleBot(BOT_TOKEN)

# بخش وب‌سرور برای راضی کردن Render
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# اجرای همزمان ربات و وب‌سرور
if __name__ == "__main__":
    t = Thread(target=run_web)
    t.start()
    print("BOT AND WEB SERVER RUNNING")
    bot.polling(none_stop=True, interval=0)
