import telebot
import os
import json

import env_var
import img_scrape

chat_id = os.environ["chat_id"]
chat_id_product = os.environ["chat_id_product"]
bot = telebot.TeleBot(os.environ["token"], parse_mode=None)


def send_photo():
    markup = telebot.types.InlineKeyboardMarkup()
    itembtn1 = telebot.types.InlineKeyboardButton('Post', callback_data='post')
    itembtn2 = telebot.types.InlineKeyboardButton('Dismiss', callback_data='dismiss')
    markup.add(itembtn1, itembtn2)
    img_path = img_scrape.get_new_img()
    bot.send_photo(chat_id, img_path, reply_markup=markup, caption=img_path)
    return bot

@bot.callback_query_handler(func=lambda call: True)
def message_reply(call):
    #bot.send_mesaage(chat_id, )
    bot.edit_message_media(message_id=call.message.message_id, chat_id=chat_id, media=telebot.types.InputMediaPhoto("https://img-9gag-fun.9cache.com/photo/aGzReY7_460s.jpg"))
    img_path = call.message.caption
    if call.data == "post":
        bot.send_photo(chat_id_product, img_path)

send_photo()

bot.infinity_polling()

#https://img-9gag-fun.9cache.com/photo/aGzReY7_460s.jpg
#img_scrape.get_new_img()
