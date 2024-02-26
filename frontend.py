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

    # def start_btns(self):
    #     subscribe = types.InlineKeyboardButton('➕Подписаться', url='https://t.me/AdviceOTZIVI')
    #     self.__markup.add(subscribe)
    #     return self.__markup
