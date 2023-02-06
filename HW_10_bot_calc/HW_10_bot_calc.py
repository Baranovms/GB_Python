import telebot
from telebot import types
import logger


bot = telebot.TeleBot("5888524320:AAF2-z58ndxfwxzBC87f8Alrw-nAMCtAyKo")

a = 0
b = 0
res = 0
sign = None
complex_sign = None

@bot.message_handler(commands=['start'])  # вызов функции по команде в списке
def start(message):
    global flag
    bot.send_message(message.chat.id, f"Выбери тип калькулятора")  # отправка сообщения (кому отправляем, что отправляем(str))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создание клавиатуры
    but1 = types.KeyboardButton("Классический калькулятор")#создание кнопок
    but2 = types.KeyboardButton("Калькулятор комплексных чисел")
    markup.add(but1)#добавление кнопок
    markup.add(but2)#добавление кнопок
    bot.send_message(message.chat.id, "Выберите ниже", reply_markup=markup)

@bot.message_handler(commands=["log"])
def getlog(message):
    doc = open('log.csv', 'rb')
    bot.send_document(message.from_user.id, doc)


@bot.message_handler(content_types=["text"])
def controller(message):
    if message.text == "Классический калькулятор":
        bot.send_message(message.chat.id, "Введите знак для действительных чисел (+,-,/,*,//,%) ")
        bot.register_next_step_handler(message, get_sign)
    if message.text == 'Калькулятор комплексных чисел':
        bot.send_message(message.chat.id, "Введите знак для действительных чисел (+,-,/,*) ")
        bot.register_next_step_handler(message, get_complex)

def get_sign(message):
    global sign
    sign = message.text
    bot.send_message(message.chat.id, "Введите 1-е число ")
    bot.register_next_step_handler(message, input_calc1)

def input_calc1(message):
    global a
    a = message.text
    if not a.isdigit():
        bot.send_message(message.chat.id, 'Enter only digits!')
        bot.register_next_step_handler(message, input_calc1)
    bot.send_message(message.chat.id, "Введите 2-е число ")
    bot.register_next_step_handler(message, input_calc2)

def input_calc2(message):
    global b
    b = message.text
    if not b.isdigit():
        bot.send_message(message.chat.id, 'Enter only digits!')
        bot.register_next_step_handler(message, input_calc2)
    bot.send_message(message.chat.id, "Результат")
    int_calc(message)

def int_calc(message):
    global res, sign
    if sign == "+":
        res = int(a) + int(b)
        log_str = f'{a} + {b} = {res}'
        bot.send_message(message.chat.id, (f'{a} + {b} = {res}'))
    if sign == "-":
        res = int(a) - int(b)
        log_str = f'{a} - {b} = {res}'
        bot.send_message(message.chat.id, (f'{a} - {b} = {res}'))
    if sign == "*":
        res = int(a) * int(b)
        log_str = f'{a} * {b} = {res}'
        bot.send_message(message.chat.id, (f'{a} * {b} = {res}'))
    if sign == "/":
        if b != 0:
            res = int(a) / int(b)
            log_str = f'{a} / {b} = {res}'
            bot.send_message(message.chat.id, (f'{a}/ {b} = {res}'))
        else:
            bot.send_message(message.chat.id, (f'Деление на ноль. Попробуйте еще раз.'))
            input_calc1(message)
    if sign == "//":
        if b != 0:
            res = int(a) // int(b)
            log_str = f'{a} // {b} = {res}'
            bot.send_message(message.chat.id, (f'{a} // {b} = {res}'))
        else:
            bot.send_message(message.chat.id, (f'Деление на ноль. Попробуйте еще раз.'))
            input_calc1(message)
    if sign == "%":
        if b != 0:
            res = int(a) % int(b)
            log_str = f'{a} % {b} = {res}'
            bot.send_message(message.chat.id, (f'{a} % {b} = {res}'))
        else:
            bot.send_message(message.chat.id, (f'Деление на ноль. Попробуйте еще раз.'))
            input_calc1(message)
    logger.log_operation(log_str)



def get_complex(message):
    global complex_sign
    complex_sign = message.text
    bot.send_message(message.chat.id, "Введите 1-е комплексое число ")
    bot.register_next_step_handler(message, input_comlex1)

def input_comlex1(message):
    global a
    a = complex(message.text)
    bot.send_message(message.chat.id, "Введите 2-е комплексное число ")
    bot.register_next_step_handler(message, input_comlex2)

def input_comlex2(message):
    global b
    b = complex(message.text)
    bot.send_message(message.chat.id, "Результат")
    complex_calc(message)

def complex_calc(message):
    global res, complex_sign
    if complex_sign == "+":
        res = a + b
        log_str = f'{a} + {b} = {res}'
        bot.send_message(message.chat.id, (f'{a} + {b} = {res}'))
    if complex_sign == "-":
        res = a - b
        log_str = f'{a} - {b} = {res}'
        bot.send_message(message.chat.id, (f'{a} - {b} = {res}'))
    if complex_sign == "*":
        res = a * b
        log_str =  f'{a} * {b} = {res}'
        bot.send_message(message.chat.id, (f'{a} * {b} = {res}'))
    if complex_sign == "/":
        if b != 0:
            res = a / b
            log_str = f'{a} / {b} = {res}'
            bot.send_message(message.chat.id, (f'{a}/ {b} = {res}'))
        else:
            bot.send_message(message.chat.id, (f'Деление на ноль. Попробуйте еще раз.'))
    if complex_sign == "//":
        bot.send_message(message.chat.id, (f'Неверный выбор функции. Попробуйте еще раз'))
    if complex_sign == "%":
        bot.send_message(message.chat.id, (f'Неверный выбор функции. Попробуйте еще раз'))
    logger.log_operation(log_str)

print("Start Server")
bot.infinity_polling()