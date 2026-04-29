import telebot
import google.generativeai as genai

# ၁။ ကိုကောင်းရဲ့ Token အသစ်စက်စက်
TELEGRAM_TOKEN = '8723355944:AAH12_ss1uY1nX5GQ08AZ26ZzuxQrUPrJ1E'

# ၂။ ကိုကောင်းရဲ့ Gemini API Key
GEMINI_API_KEY = 'AIzaSyDm7v2l1e4zP8v2wIfCSsc5NfS7nkSkN-I'

# Gemini Setup - model name ကို 'models/gemini-1.5-flash' အစား 'gemini-1.5-flash' လို့ပဲ သုံးကြည့်ပါမယ်
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! အခုတော့ အားလုံး အိုကေပြီ ထင်တယ်ဗျ။ စမ်းကြည့်ပါဦး!")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        # Model နာမည် မှားခဲ့ရင်တောင် ဒီနေရာမှာ ပြန်စစ်ပေးမယ်
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        # Error တက်ရင် ဘာလို့တက်လဲဆိုတာ အသေးစိတ်ပြမယ်
        print(f"Log: {e}")
        bot.reply_to(message, f"Error Message: {str(e)}")

bot.infinity_polling()
