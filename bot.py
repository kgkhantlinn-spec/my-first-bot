import telebot
import google.generativeai as genai

# ၁။ ကိုကောင်းရဲ့ Token အသစ်
TELEGRAM_TOKEN = '8723355944:AAGiPXuNVdaWBKleTIkUSsSYgcOB4yuZFnI'

# ၂။ ကိုကောင်း အခုပေးတဲ့ API Key အသစ်
GEMINI_API_KEY = 'AIzaSyDm7v2l1e4zP8v2wIfCSsc5NfS7nkSkN-I'

# Gemini AI ကို Setup လုပ်ခြင်း
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! အခု ကျွန်တော် လုံးဝ အဆင်သင့် ဖြစ်သွားပါပြီဗျ။ စကားပြောလို့ ရပါပြီ!")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        # Gemini ဆီက အဖြေတောင်းတာပါ
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        # Error တက်ရင် ဘာလို့တက်လဲဆိုတာ ကိုကောင်းကို တိုက်ရိုက်ပြောပြမယ်
        bot.reply_to(message, f"Error တက်နေပါတယ် ကိုကောင်း- \n\n {str(e)}")

bot.infinity_polling()
