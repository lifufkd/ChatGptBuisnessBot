#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import telebot
from telebot import types
#####################################

class Bot_inline_btns:
    def __init__(self):
        super(Bot_inline_btns, self).__init__()
        self.__markup = types.InlineKeyboardMarkup(row_width=1)

    def start_btns(self):
        subscribe1 = types.InlineKeyboardButton('Изменить промт для создания вопросов')
        subscribe2 = types.InlineKeyboardButton('Изменить промт для анализа ответов')
        self.__markup.add(subscribe1, subscribe2)
        return self.__markup


