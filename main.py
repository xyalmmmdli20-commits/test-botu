import os
from threading import Thread
from flask import Flask
import telebot
from telebot import types

# Server üçün Flask xidməti
app = Flask("")


@app.route("/")
def home():
    return "Bot aktivdir!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


# TELEGRAM BOT KODLARI
# Telegram-dan aldığınız tokeni dırnaq arasına yazın
API_TOKEN = "8916781102:AAExxL4BbVEl_XK3khj-eofaQVI1fHRN5Qw"
bot = telebot.TeleBot(API_TOKEN)

QUESTIONS = [
    {
        "question": "1. Azərbaycanın paytaxtı hansı şəhərdir?",
        "options": ["A) Gəncə", "B) Bakı", "C) Sumqayıt", "D) Şəki"],
        "correct": "B) Bakı",
    },
    {
        "question": "2. Azərbaycan Respublikası neçənci ildə müstəqillik əldə edib?",
        "options": ["A) 1918", "B) 1995", "C) 1991", "D) 2000"],
        "correct": "C) 1991",
    },
]

user_data = {}


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("📝 Testə Başla")
    btn2 = types.KeyboardButton("📊 Nəticələrim")
    keyboard.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        "Azərbaycan Test Mərkəzinə xoş gəlmisiniz!",
        reply_markup=keyboard,
    )


@bot.message_handler(content_types=["text"])
def handle_text(message):
    chat_id = message.chat.id
    if message.text == "📝 Testə Başla":
        user_data[chat_id] = {"current_q": 0, "score": 0}
        send_question(chat_id)
    elif message.text == "📊 Nəticələrim":
        score = user_data.get(chat_id, {}).get("score", 0)
        bot.send_message(
            chat_id, f"📊 Son test üzrə nəticəniz: {score} doğru cavab."
        )


def send_question(chat_id):
    q_idx = user_data[chat_id]["current_q"]
    if q_idx >= len(QUESTIONS):
        score = user_data[chat_id]["score"]
        bot.send_message(
            chat_id,
            f"🎉 **İmtahan bitdi!**\nNəticəniz: {len(QUESTIONS)} sualdan {score} doğru!",
            parse_mode="Markdown",
        )
        return

    q = QUESTIONS[q_idx]
    markup = types.InlineKeyboardMarkup(row_width=1)
    for opt in q["options"]:
        markup.add(types.InlineKeyboardButton(text=opt, callback_data=opt))
    bot.send_message(chat_id, q["question"], reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call):
    chat_id = call.message.chat.id
    if chat_id not in user_data:
        return
    q_idx = user_data[chat_id]["current_q"]
    if call.data == QUESTIONS[q_idx]["correct"]:
        user_data[chat_id]["score"] += 1
        bot.answer_callback_query(call.id, "✅ Doğru!")
    else:
        bot.answer_callback_query(call.id, "❌ Səhv!")

    user_data[chat_id]["current_q"] += 1
    bot.delete_message(chat_id, call.message.message_id)
    send_question(chat_id)


if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
