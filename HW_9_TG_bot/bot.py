import telebot
from telebot import types
from random import *

bot = telebot.TeleBot("6178029107:AAFwZSyV_KHLY-UTayqupZQaKr92h2LPjFA")

user_sweets = 0
step_max = 28
sweets = 221
bot_sweets = 0
first_step = 'first'

@bot.message_handler(commands=['start'])  # вызов функции по команде в списке
def start(message):
    bot.send_message(message.chat.id, f"Выбери тип игры, /controller")  # отправка сообщения (кому отправляем, что отправляем(str))

def get_count(message):
    global sweets
    sweets = sweets - user_sweets
    bot.send_message(message.chat.id, f"Конфет осталось: {sweets}")
    controller(message)

def user_input(message):
    global user_sweets
    user_sweets = int(message.text)
    if (user_sweets > step_max) or (user_sweets > sweets):
        bot.send_message(message.chat.id, f'Столько брать нельзя. Попробуй снова.')
        controller(message)
    else:
        get_count(message)

def bot_input(message):
    global bot_sweets
    bot_sweets = randint(1, 28)
    bot.send_message(message.chat.id, f'Бот взял конфет: {bot_sweets}')
    get_bot_count(message)

def get_bot_count(message):
    global sweets
    sweets = sweets - bot_sweets
    bot.send_message(message.chat.id, f'Осталось конфет: {sweets}')
    controller(message)

@bot.message_handler(commands=["controller"])
def controller(message):
    global sweets
    if message.text == 'Начать игру за пользователя':
        bot.send_message(message.chat.id, f"Начата игра за пользователя")
        bot.send_message(message.chat.id, f"Введите количество не больше 28") # отправка сообщения (кому отправляем, что отправляем(str))
        bot.register_next_step_handler(message, user_input)
    if message.text == 'Начать игру за бота':
        bot.send_message(message.chat.id, f"Начата игра за бота")
        bot.register_next_step_handler(message, bot_input)


@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создание клавиатуры
    but1 = types.KeyboardButton("Начать игру за пользователя")#создание кнопок
    but2 = types.KeyboardButton("Начать игру за бота")
    markup.add(but1)#добавление кнопок
    markup.add(but2)#добавление кнопок
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)

bot.infinity_polling()
