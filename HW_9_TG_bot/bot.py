import telebot
from telebot import types
from random import *

bot = telebot.TeleBot("6178029107:AAFwZSyV_KHLY-UTayqupZQaKr92h2LPjFA")

user_sweets = 0
sweets = 221

@bot.message_handler(commands=['start'])  # вызов функции по команде в списке
def start(message):
    bot.send_message(message.chat.id, f"/game")  # отправка сообщения (кому отправляем, что отправляем(str))


@bot.message_handler(commands=["game"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание клавиатуры
    but1 = types.KeyboardButton("Начать игру")  # создание кнопок
    markup.add(but1)  # добавление кнопок
    bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=markup)

def user_input(message):
    global user_sweets
    user_sweets = int(message.text)
    if user_sweets > 28 or user_sweets > sweets:
        bot.send_message(message.chat.id, f'Столько брать нельзя, начни сначала')
        start(message)
    else:
        get_count(message)

def get_count(message):
    global sweets
    sweets = sweets - user_sweets
    bot.send_message(message.chat.id, f"Осталось конфет: {sweets}")
    controller(message)

def bot_input(message):
    global bot_sweets
    bot_sweets = randint(1, 29)
    get_bot_count(message)

def get_bot_count(message):
    global sweets
    bot.send_message(message.chat.id, f'Бот взял конфет: {bot_sweets}')
    sweets = sweets - bot_sweets
    bot.send_message(message.chat.id, f"Осталось конфет: {sweets}")
    controller(message)

@bot.message_handler(content_types=["text"])
def controller(message):
    global sweets
    while sweets >= 0:
        bot.send_message(message.chat.id, f'Сколько конфет возьмешь? ')
        bot.register_next_step_handler(message, user_input)
        if sweets == 0:
            bot.send_message(message.chat.id, f'Поздравляю! Вы выиграли!')
            start(message)
        if sweets >= 28:
            bot.register_next_step_handler(message, bot_input)
        if sweets <= 28:
            bot.register_next_step_handler(message, bot_input)

bot.infinity_polling()
