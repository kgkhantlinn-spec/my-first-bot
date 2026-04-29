import telebot
import google.generativeai as genai
import os

# Render Environment ထဲကနေ ဆွဲယူမယ်
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '8723355944:AAGiPXuNVdaWBKleTIkUSsSYgcOB4yuZFnI')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyCZAem5bj_ItU014WMfExUNLuZaazl4E-8')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! Bot ကတော့ ပွင့်နေပါပြီ။ စာတစ်ကြောင်းလောက် ပို့ကြည့်ပါဦးဗျ။")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        # ဘာလွဲနေလဲဆိုတာကို Bot က ကိုကောင်းကို တိုက်ရိုက်ပြောပြလိမ့်မယ်
        bot.reply_to(message, f"ပြဿနာကတော့ ဒါပါ ကိုကောင်း- \n\n {str(e)}")

bot.infinity_polling()
