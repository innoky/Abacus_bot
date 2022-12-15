#---------------------------------------------------------------------------

import time
import random
import os
import subprocess
import sys
import os.path
import numpy as np


import telebot

from telebot import types



#---------------------------------------------------------------------------


go = "hi"
bot = telebot.TeleBot('5654797665:AAGHtXeh2hew8L8bZvvfXNyiOBiF9bIikog')

@bot.message_handler(commands=['start'])



#---------------------------------------------------------------------------



def welcome(message):


    # keyboard (Создание кнопок и приветствие)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Помощь")
    item2 = types.KeyboardButton("Сообщить об ошибке")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, телеграмм бот от HS university! Мой функционал основывается на технологиях wolfram research, но в будущем мы собираемся перейти на свой язык программирования. Нажми «Помощь» чтобы узнать больше о моих возможностях.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])



#---------------------------------------------------------------------------



def lalala(message):
    if message.chat.type == 'private':
        if "x" in message.text:
            global get_message
            get_message = message.text
 			# keyboard (Создание кнопок под текстом)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Посчитать интеграл", callback_data='1')
            item2 = types.InlineKeyboardButton("Нарисовать график", callback_data='2')
            item3 = types.InlineKeyboardButton("Найти корни", callback_data='3')
            item4 = types.InlineKeyboardButton("Найти производную", callback_data='4')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, get_message, reply_markup=markup)

        # elif message.text == ' '
        elif message.text == "Посчитать интеграл":
            bot.send_message(message.chat.id, "i")


        else:
            bot.send_message(message.chat.id, "ушел в else")
#---------------------------------------------------------------------------
#отрисовка графика
#нижний предел интеграла
def lower_lim(message, plus_low):
    plus_high = plus_low + " " + message.text

    msg = bot.send_message(message.chat.id, "Введите верхний предел интегрирования")
    bot.register_next_step_handler(msg, upp_lim, plus_high)

#верхний предел интеграла
def upp_lim(message, plus_high):
    final_int = plus_high + " " + message.text

    clear_func = final_int.replace("^", "**")
    with open("int_get.txt", "w") as file:
        file.write(clear_func)

    os.system('python3 integral.py')
    time.sleep(2)
    with open("int_out.txt", "r") as file:
        for line in file:
            text1 = str(line)
    bot.send_message(message.chat.id, "Ваш интеграл равен:")
    bot.send_message(message.chat.id, text1)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
        	# keyboard (Работа с кнопками под текстом)
            if call.data == '1':
                msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите нижний предел интегрирования",
                    reply_markup=None)
                plus_low = get_message
                bot.register_next_step_handler(msg, lower_lim, plus_low)

            elif call.data == '2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Подождите... Считаем точки",
                    reply_markup=None)
                time.sleep(1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Рисуем график...",
                    reply_markup=None)
                time.sleep(1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отправляем график...",
                    reply_markup=None)
                get_sub = get_message
                clear_graph1 = get_sub.replace("^", "**")
                with open("graphdraw.py", "w") as file:
                    file.write(
'''
from numpy import sqrt, sin, cos, pi
import matplotlib.pyplot as plt
import os.path
import numpy as np
x = np.linspace(-5,5,100)
'''
+ clear_graph1 +
'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.savefig('/home/innoky/Documents/hsbot/HSBOT 2.0/graphs/graphdraw.png')
''')
                os.system("python3 graphdraw.py")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="График вашей функции:",
                    reply_markup=None)
                bot.send_photo(call.message.chat.id, open('/home/innoky/Documents/hsbot/HSBOT 2.0/graphs/graphdraw.png', 'rb'));

            elif call.data == '3':
                bot.send_message(call.message.chat.id, '')
            elif call.data == '4':
                bot.send_message(call.message.chat.id, '')

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Пишите, всегда поможем!")

    except Exception as e:
        print(repr(e))



#---------------------------------------------------------------------------


# Старт
bot.polling(none_stop=True)



#---------------------------------------------------------------------------
