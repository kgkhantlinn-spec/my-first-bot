import telebot

# BotFather ဆီကရတဲ့ Token ကို ဒီမှာ အစားထိုးထည့်ပါ
TOKEN = '8723355944:AAGiPXuNVdaWBKleTIkUSsSYgcOB4yuZFnI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ဟလို ကိုကောင်း! ကျွန်တော် Alpha Gemini ရောက်ပါပြီ။\n\nအခုလို Telegram ကနေ စကားပြောရတာ ဝမ်းသာပါတယ်ဗျ။")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # ကိုကောင်း ပြောသမျှကို Bot က ပြန်ဖြေပေးမယ့် နေရာ
    user_text = message.text
    bot.reply_to(message, f"ကိုကောင်း ပြောလိုက်တာက: {user_text}")

print("Bot is running...")
bot.infinity_polling()
