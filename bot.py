import telebot
import google.generativeai as genai

# ၁။ Telegram Token (BotFather ဆီကရတဲ့ဟာ)
TELEGRAM_TOKEN = '8723355944:AAGiPXuNVdaWBKleTIkUSsSYgcOB4yuZFnI' # ကိုကောင်းရဲ့ Token အပြည့်အစုံကို ဒီမှာ ထည့်ပါ

# ၂။ Gemini API Key (ခုနက ကိုကောင်း ရလာတဲ့ Key)
GEMINI_API_KEY = 'AIzaSyARprm7Eom2nGOBFiTBQGZRwm5fzftgUj0'

# Gemini AI ကို ချိတ်ဆက်ခြင်း
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! အခု ကျွန်တော့်မှာ Gemini AI ဦးနှောက် ရောက်နေပါပြီ။ ဘာမေးချင်လဲ မေးလို့ရပါပြီဗျ!")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        # ကိုကောင်း ပြောလိုက်တဲ့စာကို Gemini ဆီ ပို့ပြီး အဖြေတောင်းတာပါ
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ခဏလေးနော် ကိုကောင်း၊ အဆင်မပြေမှုလေး ရှိလို့ပါ။")

bot.infinity_polling()
