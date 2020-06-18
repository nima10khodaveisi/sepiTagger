from asyncore import dispatcher

import telebot

API_TOKEN = '1104495525:AAGshNjPqxeMmZ7IAOy675YSnPrHEOJ6TMQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler()
def tag_spei(message) :
    bot.send_animation(message.chat.id, open('IMG_2923.MP4','rb'), reply_to_message_id=message.message_id)
    print(message)


bot.polling()