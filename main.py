import telebot
import random as r

neutral_response = ['хм, даже не знаю как реагировать', 'хммм', 'сомневаюсь что мне есть что добавить',
                    'посмотрим что остальные скажут', '🤔🤔🤔', 'продолжай', 'помедленнее, я записываю']

sad_response = ['%(', '😭😭', '😥😥', 'моя печаль неизмерима(', 'бле(', '(((', 'Грущу вместе с тобой(']
positive_response = ['Слова не мальчика, но мужа!)', 'Подписываюсь под каждым словом!)',
                     'Пускай я бездушная машина, но то что пишет этот парень ☝ - истина!', 'Полностью согласен!)',
                     'Да уж!)', 'Лучше и не скажешь!)', 'С языка снял!)', 'Все верно говорит!', '+1',
                     'Братан, когда прав тогда прав!']
link_response = ['Как говорил мой прадед - "Если ссылка то только такая!" ☝', 'Щас глянем, кэп!',
                 '☝️Топ контент от братишки!', '☝️Всем смотреть срочно!',
                 '☝️Вау!', 'Спасибо за ссылку! Мне очень понравилось!', '☝️Кто не глянул тот лох! Я глянул)', '👍👍👍']
question_response = ['☝ Рубрика "ЗАГАДКИ ВСЕЛЕННОЙ"', 'Реально важные вопросы подъехали!',
                     '☝ Вот это действительно интересно было бы узнать!',
                     'Неразрешенная загадка человечества 🤷',
                     'Ах если бы я мог ответить(', '@all а ну ка мозговой штурм!! и ответим братику на вопросик!💪']
poor_language = ['лол', 'кек', 'ахах']
poor_language_response = ['😂😂😂', 'лол кек чебурек', 'ОЛОЛОЛО', ')))))1)1адинадинадин',
                          'воистину невообразимо смешно!']

bot = telebot.TeleBot('5477098400:AAGt0TR__hxURKOo99iwtxr7gho0ZsIkV6M')
poo_emoji = u'\U0001F4A9'
abc = list('ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщщзхъфывапролджэячсмитьбю'
           'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasddfghjklzxcvbnm,.!()?=-+@#$%^&*/" 123456789')





def find_emoji(message):
    message = message[::-1]
    flag = 0
    for i in list(message):
        if i not in abc:
            flag +=1
    if flag != 0:

        return True


def emoji_response(message):
    message = message[::-1]
    emolist = []
    for i in list(message):
        if i not in abc:
            emolist.append(i)
    return ''.join(emolist[::-1])

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_usertext(message):
    userlist = [] #имя пользователя из участников чата, на сообщения которого бот будет реагировать 
    
    if message.from_user.username in userlist:  # ПОЛЬЗОВАТЕЛЬ
        if message.text == 'Hello':

            bot.send_message(message.chat.id, poo_emoji, parse_mode='html')
        elif message.text == 'id':
            bot.send_message(message.chat.id, message.from_user.id, parse_mode='html')
        elif message.text == 'message':
            bot.send_message(message.chat.id, message, parse_mode='html')
        elif 'http' in message.text:  # ссылка от пользователя
            bot.send_message(message.chat.id, f'{r.choice(link_response)}', parse_mode='html')
        elif message.text[-1] == '?' or '?)' in message.text  or '?(' in message.text :  # вопросительное предложение
            bot.send_message(message.chat.id, f'{r.choice(question_response)}', parse_mode='html')

        # elif len(find_emoji(message.text)) == 1:  # дублируем последний эмоджи в сообщении версия 1
        #     bot.send_message(message.chat.id, f'{r.choice(positive_response)} {find_emoji(message.text) * 3}',
        #                      parse_mode='html')
        elif find_emoji(message.text) == True: # дублируем последний эмоджи в сообщении версия 2
            if message.text == emoji_response(message.text):
                bot.send_message(message.chat.id, f'{emoji_response(message.text) * r.randint(2,4)}',
                             parse_mode='html')
            else:
                bot.send_message(message.chat.id, f'{r.choice(positive_response)} {emoji_response(message.text) * r.randint(2,4)}',
                             parse_mode='html')
        elif message.text.lower() in poor_language or 'азаз' in message.text.lower():  # отвечаем на лолкек паразитов
            bot.send_message(message.chat.id, f'{r.choice(poor_language_response)}', parse_mode='html')
        elif message.text[-1] == '(':  # отвечаем на грустную скобку
            bot.send_message(message.chat.id, f'{r.choice(sad_response)}', parse_mode='html')
        elif message.text[-1] == ')'and '(' not in message.text:  # отвечаем на веселую скобку
            bot.send_message(message.chat.id, f'{r.choice(positive_response)}', parse_mode='html')
        else:
            a = r.randint(1, 4)

            if a == 1:
                bot.send_message(message.chat.id, f'{r.choice(neutral_response)}', parse_mode='html')


bot.polling(none_stop=True)


