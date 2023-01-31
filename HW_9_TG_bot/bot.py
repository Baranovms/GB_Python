import telebot
from telebot import types
from random import *

bot = telebot.TeleBot("6178029107:AAFwZSyV_KHLY-UTayqupZQaKr92h2LPjFA")

flag = None
user_sweets = 0
bot_sweets = 0
step_max = 28
sweets = 221

@bot.message_handler(commands=['start'])  # вызов функции по команде в списке
def start(message):
    global flag
    bot.send_message(message.chat.id, f"Выбери тип игры")  # отправка сообщения (кому отправляем, что отправляем(str))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создание клавиатуры
    but1 = types.KeyboardButton("Начать игру за пользователя")#создание кнопок
    but2 = types.KeyboardButton("Начать игру за бота")
    markup.add(but1)#добавление кнопок
    markup.add(but2)#добавление кнопок
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def first_step(message):
    global flag
    if message.text == "Начать игру за пользователя":
        flag = "user"
    else:
        flag = "bot"
    controller(message)

def controller(message):
    global flag
    if sweets > 0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Ваш ход. Введите кол-во конфет от 0 до {step_max}")
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Поздравляем! Победу одержал {flag}!")
        mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = telebot.types.KeyboardButton("Перезапуск")
        key2 = telebot.types.KeyboardButton("Выход")
        mrk.add(key1)
        mrk.add(key2)
        bot.send_message(message.chat.id,"Если хотите перезапусти", reply_markup=mrk)
        bot.register_next_step_handler(message, restart_game)
@bot.message_handler(content_types=["text"])
def restart_game(message):
    if message.text == "Перезапуск":
        restart()
        start(message)
    else:
        exit()

def user_input(message):
    global user_sweets, flag
    user_sweets = int(message.text)
    if (user_sweets > step_max) or (user_sweets > sweets):
        bot.send_message(message.chat.id, f'Столько брать нельзя. Попробуй снова.')
        controller(message)
    else:
        get_count(message)

def get_count(message):
    global sweets, flag
    sweets = sweets - user_sweets
    bot.send_message(message.chat.id, f"Конфет осталось: {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

def restart():
    global sweets
    sweets = 221

def bot_input(message):
    global bot_sweets, flag
    bot_sweets = randint(1, 28)
    bot.send_message(message.chat.id, f'Бот взял конфет: {bot_sweets}')
    get_bot_count(message)

def get_bot_count(message):
    global sweets, flag
    sweets = sweets - bot_sweets
    bot.send_message(message.chat.id, f'Осталось конфет: {sweets}')
    flag = "user" if flag == "bot" else "bot"
    controller(message)

bot.infinity_polling()
