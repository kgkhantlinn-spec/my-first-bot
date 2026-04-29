import telebot
import google.generativeai as genai
import os
from flask import Flask
import threading

# Render ရဲ့ Port Error ကို ကျော်ဖို့ Flask Setup လုပ်တာပါ
app = Flask(__name__)

@app.route('/')
def home():
    return "Alpha Gemini Bot is running!"

# ၁။ Telegram Token (ကိုကောင်း အခုပေးတဲ့ဟာ ထည့်ထားပေးပါတယ်)
TELEGRAM_TOKEN = '8723355944:AAGiPXuNVdaWBKleTIkUSsSYgcOB4yuZFnI'

# ၂။ Gemini API Key (ကိုကောင်း စောစောက ရထားတဲ့ဟာ)
GEMINI_API_KEY = 'AIzaSyARprm7Eom2nGOBFiTBQGZRwm5fzftgUj0'

# Gemini AI ဦးနှောက်ကို ချိတ်ဆက်တာပါ
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! ကျွန်တော် Alpha Gemini (AI) အသင့်ရှိနေပါပြီ။ ဘာမေးချင်လဲ မေးလို့ရပါပြီဗျ!")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        # ကိုကောင်း မေးလိုက်တဲ့စာကို Gemini ဆီ ပို့လိုက်တာပါ
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခဏလေးနော် ကိုကောင်း၊ တစ်ခုခု လွဲနေလို့ပါ။")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Bot ကို သီးသန့် Thread တစ်ခုနဲ့ Run တာပါ
    threading.Thread(target=run_bot, daemon=True).start()
    # Render အတွက် Port တစ်ခု ဖွင့်ပေးတာပါ
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
