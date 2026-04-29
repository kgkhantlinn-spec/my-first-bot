import telebot
import google.generativeai as genai
import os

# Render Environment ထဲကနေ Token တွေကို လုံခြုံစွာ ဆွဲယူမယ်
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! အခု ကျွန်တော် လုံးဝ အဆင်သင့် ဖြစ်သွားပါပြီဗျ။")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခေတ္တစောင့်ဆိုင်းပေးပါ ကိုကောင်း။")

bot.infinity_polling()
