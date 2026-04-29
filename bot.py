import telebot
import google.generativeai as genai

# ၁။ ကိုကောင်း အခုပေးတဲ့ Token အသစ် (အစက်လေးတွေ၊ စာလုံးလေးတွေ သေချာစစ်ပြီး ထည့်ထားပါတယ်)
TELEGRAM_TOKEN = '8723355944:AAGiPXuNVdaWBKleTIkUSsSYgcOB4yuZFnI'

# ၂။ ကိုကောင်းရဲ့ Gemini API Key အသစ်
GEMINI_API_KEY = 'AIzaSyCZAem5bj_ItU014WMfExUNLuZaazl4E-8'

# Gemini Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! အခုတော့ လုံးဝ အဆင်ပြေသွားပါပြီ။ ကျွန်တော် Alpha Gemini အသင့်ရှိနေပါပြီဗျ!")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခေတ္တစောင့်ဆိုင်းပေးပါ ကိုကောင်း။")

bot.infinity_polling()
