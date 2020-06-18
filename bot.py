import telebot

API_TOKEN = '1015161255:AAEnNiql2HzZm3DNMU1ibUyHaK4gj8jYjlQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler()
def tag_spei(message) :
    bot.reply_to(message, '@IsepantaI')
    print(message)

bot.polling()