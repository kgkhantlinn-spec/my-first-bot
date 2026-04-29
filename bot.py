import telebot
import google.generativeai as genai
import os
from flask import Flask
import threading

# ၁။ Bot Setup
TELEGRAM_TOKEN = '8723355944:AAH12_ss1uY1nX5GQ08AZ26ZzuxQrUPrJ1E'
GEMINI_API_KEY = 'AIzaSyDm7v2l1e4zP8v2wIfCSsc5NfS7nkSkN-I'

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# ၂။ Render ရဲ့ Port Scan Error ကို ကျော်ဖို့ Flask သုံးမယ်
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is alive!", 200

def run_flask():
    # Render က ပေးတဲ့ Port ကို သုံးမယ်၊ မရှိရင် 10000 ကို သုံးမယ်
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# ၃။ Bot Logic
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! US Server ကနေ အဆင်သင့် ဖြစ်ပါပြီဗျ။")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

if __name__ == "__main__":
    # Flask ကို Thread နဲ့ Background မှာ run မယ်
    threading.Thread(target=run_flask, daemon=True).start()
    # ပြီးရင် Bot ကို run မယ်
    print("Bot is starting...")
    bot.infinity_polling()
