import telebot
import google.generativeai as genai

# ၁။ Telegram Token
TELEGRAM_TOKEN = '8123355944:AAGuD9T_hXoZq5T-O3K03P_NfP0U5J8m6x8'

# ၂။ Gemini API Key
GEMINI_API_KEY = 'AIzaSyARprm7Eom2nGOBFiTBQGZRwm5fzftgUj0'

# Gemini Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! အခု ကျွန်တော့်မှာ Gemini AI ဦးနှောက် ရှိသွားပါပြီ။ ဘာမေးချင်လဲ မေးလို့ရပါပြီဗျ!")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(e)
        bot.reply_to(message, "အဆင်မပြေမှုလေး ဖြစ်သွားလို့ ခဏနေမှ ပြန်မေးပေးပါဦး ကိုကောင်း။")

# ⚠️ ဒီနေရာက အရေးကြီးဆုံးပါ - တခြား Flask code တွေ မပါရပါဘူး
bot.infinity_polling()
