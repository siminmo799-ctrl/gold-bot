import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.environ.get("8940690033:AAHpu5bUlNLE9-Qsk692ViEHQxCvgMcwT30")

if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN is missing")
    exit()

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200
