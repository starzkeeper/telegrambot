import telebot as tb
import vk_api
from urlextract import URLExtract

bot = tb.TeleBot('5690482127:AAFVEmVE0sMoPSmYZmqxVltQF1BV2oW4gO0')

session = vk_api.VkApi(token='vk1.a.bD6PnYGQLQhj5eTR4x_eMuqnwH1YV_YFTakJJb9GjTr6YzkT8BmOkC11lvtkVNqWNOtI9'
                             '-QXGn7gZa2YLAvZ2UyKlbkjLvz8uwka2Iu1Ywe_2vHEVOJoyELn_ZtsjK16xqqN4ydtWAO5Z9Svg45qoeoIx1gCXuJLva5GlnYTbfnSOrM-aAWfNEIxCJimea2gV7zhvhASim0zxLU3SzQRow')

vk = session.get_api()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>audiostarz vk: https://vk.com/ascult</b>', parse_mode='html')


@bot.message_handler(commands=['last_post'])
def last_track(message):
    post = get_post()
    bot.send_message(message.chat.id, post['items'][0]['text'])


@bot.message_handler(commands=['all_tracks'])
def all_tracks(message):
    post = get_post()
    extractor = URLExtract()
    for i in range(len(post['items'])):
        if len(extractor.find_urls(post['items'][i]['text'])) != 0:
            bot.send_message(message.chat.id, post['items'][i]['text'])


def get_post():
    post = session.method("wall.get", {"owner_id": -208680305})
    return post


bot.polling(none_stop=True)
