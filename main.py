#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import os
import platform
import telebot
from config_parser import ConfigParser
from backend import TempUserData
#####################################
config_name = 'secrets.json'
questions = ['What is your favorite color?', 'What is your favorite animal?', 'What is your favorite food?']
#####################################

def main():
    @bot.message_handler(commands=['start'])
    def send_question(message):
        bot.send_message(message.chat.id, "Hi! Enter a name for your business! I will help you with the development of a private business plan!")
        temp_user_data.temp_data(message.chat.id)[message.chat.id][0] = 1

    @bot.message_handler(content_types=['text'])
    def text(message):
        user_input = message.text
        user_id = message.chat.id
        current_index = temp_user_data.temp_data(user_id)[user_id][2]
        user_current_action = temp_user_data.temp_data(user_id)[user_id][0]
        if user_current_action == 1:
            temp_user_data.temp_data(user_id)[user_id][1] = user_input
            # отправка в бэкенд
            temp_user_data.temp_data(user_id)[user_id][0] = 2
        elif user_current_action == 2:
            if current_index is None:
                temp_user_data.temp_data(user_id)[user_id][2] = []
                current_index = 0
            temp_user_data.temp_data(user_id)[user_id][2].append(message.text)
            current_index += 1
            if current_index < len(questions):
                bot.send_message(message.chat.id, questions[current_index])
            else:
                bot.send_message(message.chat.id, "Вопросы закончились")
                temp_user_data.temp_data(user_id)[user_id][2] = None

    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    temp_user_data = TempUserData()
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()
