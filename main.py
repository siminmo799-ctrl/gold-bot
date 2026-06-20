import telebot
import os
from flask import Flask, request
from threading import Thread

# TOKEN از Environment Variable گرفته می‌شود (نه داخل کد!)
BOT_TOKEN = os.environ.get("8940690033:AAHpu5bUlNLE9-Qsk692ViEHQxCvgMcwT30")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# صفحه تست وب
@app.route('/')
def home():
    return "Bot is running!"

# webhook route
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# اجرای Flask
def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# استارت برنامه
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://gold-bot-gtun.onrender.com/{BOT_TOKEN}")

    print("BOT AND WEB SERVER RUNNING")

    Thread(target=run_web).start()
