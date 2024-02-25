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
        subscribe = types.InlineKeyboardButton('➕Подписаться', url='https://t.me/AdviceOTZIVI')
        self.__markup.add(subscribe)
        return self.__markup

    def main_chat_btns(self):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            replenish = types.KeyboardButton(text="💰Пополнить")
            withdrawal = types.KeyboardButton(text="📨Вывод")
            reviews = types.KeyboardButton(text="😄Отзывы")
            course = types.KeyboardButton(text="📉Курс")
            calculator = types.KeyboardButton(text="🔢Калькулятор")
            support = types.KeyboardButton(text="👨‍💻Поддержка")
            profile = types.KeyboardButton(text="🤖Профиль")
            keyboard.add(replenish, withdrawal, reviews, course, calculator, support, profile)
            return keyboard