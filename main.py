#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import os
import platform
from io import BytesIO

import telebot
import textwrap
from config_parser import ConfigParser
from backend import TempUserData, ChatGpt, PDFCreate
#####################################
config_name = 'secrets.json'
#####################################


def main():
    @bot.message_handler(commands=['start'])
    def send_question(message):
        user_id = message.chat.id
        bot.send_message(message.chat.id, "Hi! Enter a name for your business! I will help you with the development of a private business plan!")
        temp_user_data.clear_temp_data(user_id)

    @bot.message_handler(content_types=['text'])
    def text(message):
        user_input = message.text
        user_id = message.chat.id
        if temp_user_data.temp_data(user_id)[user_id][3] == -1:
            temp_user_data.temp_data(user_id)[user_id][1] = chat_gpt.detect_language(user_input)
            temp_user_data.temp_data(user_id)[user_id][2] = user_input
            temp_user_data.temp_data(user_id)[user_id][4].extend(
                chat_gpt.gpt_query(user_input, temp_user_data.temp_data(user_id)[user_id][1], 0))
            temp_user_data.temp_data(user_id)[user_id][3] = 0
            bot.send_message(message.chat.id, temp_user_data.temp_data(user_id)[user_id][4][0])
        else:
            if temp_user_data.temp_data(user_id)[user_id][3] != len(temp_user_data.temp_data(user_id)[user_id][4]) - 1:
                temp_user_data.temp_data(user_id)[user_id][5].append(user_input)
                temp_user_data.temp_data(user_id)[user_id][3] += 1
                index = temp_user_data.temp_data(user_id)[user_id][3]
                bot.send_message(message.chat.id, temp_user_data.temp_data(user_id)[user_id][4][index])
            else:
                bot.send_message(message.chat.id, "Мы подготавливаем для Вас персональный план...")
                answer = chat_gpt.gpt_query(
                    f"{','.join(temp_user_data.temp_data(user_id)[user_id][5])} for {temp_user_data.temp_data(user_id)[user_id][2]}",
                    temp_user_data.temp_data(user_id)[user_id][1], 1)
                pdf_creator.create_pdf(temp_user_data.temp_data(user_id)[user_id][2], '\n'.join(answer))
                with open("plan.pdf", "rb") as misc:
                    obj = BytesIO(misc.read())
                    obj.name = 'plan.pdf'
                bot.send_document(user_id, obj)
                os.remove('plan.pdf')
                temp_user_data.clear_temp_data(user_id)


    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    temp_user_data = TempUserData()
    chat_gpt = ChatGpt()
    pdf_creator = PDFCreate()
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()
