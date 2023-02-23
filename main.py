
import telebot
import random

# Загружаем список интересных фактов о бобрах
f = open('bobr.txt', 'r', encoding='UTF-8')
bobr = f.read().split('\n')
f.close()
# Загружаем список фактов о лосях
f = open('los.txt', 'r', encoding='UTF-8')
los = f.read().split('\n')
f.close()
# Загружаем картинки
bobr_img = []
for i in range(10):
    image = open(f'b{i}.jpg', 'rb')
    bobr_img.append(image.read())
    image.close()
# Создаем бота
bot = telebot.TeleBot('5879572173:AAGMaueWeOlBKw46K7UvspfaXbwQK29RDuM')


# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    #  item1 = telebot.types.KeyboardButton("Факт о Лосе")
    #  item2 = telebot.types.KeyboardButton("Факт о Бобре")
    item3 = telebot.types.KeyboardButton("Фото Бобра")
    #  markup.add(item1)
    #  markup.add(item2)
    markup.add(item3)
    markup.row('Факт о Лосе', 'Факт о Бобре')
    bot.send_message(m.chat.id, 'Про какого животного хочешь узнать? Нажми: \nЛОСЬ, чтобы узнать факт о лосе'
                                   '\nБОБР, чтобы узнать факт о бобре', reply_markup=markup)

@bot.message_handler(content_types=["image"])
def handle_image(message):
    bot.send_message(message.chat.id, 'Классное фото!')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт о Лосе':
        answer = random.choice(los)
        bot.send_message(message.chat.id, answer)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Факт о Бобре':
        answer = random.choice(bobr)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'Фото Бобра':
        bot.send_photo(message.chat.id, random.choice(bobr_img))

    # Отсылаем юзеру сообщение в его чат


#
# Запускаем бота
bot.polling(none_stop=True, interval=0)

