#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import os
import platform
from io import BytesIO
from deep_translator import GoogleTranslator
import telebot
from backend import TempUserData, ChatGpt, PDFCreate
from config_parser import ConfigParser

#####################################
config_name = 'secrets.json'


#####################################


def main():
    @bot.message_handler(commands=['start'])
    def send_question(message):
        user_id = message.chat.id
        if message.from_user.language_code == 'ru':
            bot.send_message(message.chat.id,
                             "Привет! Введите название для вашего бизнеса! Я Помогу Вам с развитием частного "
                               "бизнес-плана!")
        elif message.from_user.language_code == 'en':
            bot.send_message(message.chat.id,
                             "Hi! Enter a name for your business! I will help you with the development of a private "
                             "business plan!")
        temp_user_data.clear_temp_data(user_id)

    @bot.message_handler(content_types=['text'])
    def text(message):
        user_input = message.text
        user_id = message.chat.id
        if temp_user_data.temp_data(user_id)[user_id][3] == -1:
            temp_user_data.temp_data(user_id)[user_id][1] = message.from_user.language_code
            temp_user_data.temp_data(user_id)[user_id][2] = GoogleTranslator(source='auto', target='en').translate(text=user_input)
            questions = chat_gpt.gpt_query(user_input, 0)
            if message.from_user.language_code == 'ru':
                for i in questions:
                    try:
                        temp_user_data.temp_data(user_id)[user_id][4].append(GoogleTranslator(source='en', target='ru').translate(text=i))
                    except:
                        pass
            else:
                temp_user_data.temp_data(user_id)[user_id][4].extend(questions)
            temp_user_data.temp_data(user_id)[user_id][3] = 0
            print(temp_user_data.temp_data(user_id)[user_id][4][0])
            bot.send_message(message.chat.id, temp_user_data.temp_data(user_id)[user_id][4][0]) # ошибка была
        else:
            if temp_user_data.temp_data(user_id)[user_id][3] != len(temp_user_data.temp_data(user_id)[user_id][4]) - 1:
                temp_user_data.temp_data(user_id)[user_id][5].append(user_input)
                temp_user_data.temp_data(user_id)[user_id][3] += 1
                index = temp_user_data.temp_data(user_id)[user_id][3]
                bot.send_message(message.chat.id, temp_user_data.temp_data(user_id)[user_id][4][index])
            else:
                if message.from_user.language_code == 'ru':
                    bot.send_message(message.chat.id, "Мы уже подготавливаем вам персональный план!")
                elif message.from_user.language_code == 'en':
                    bot.send_message(message.chat.id, "We already prepared your personal plan!")
                try:
                    quests = GoogleTranslator(source='auto', target='en').translate(
                        text=','.join(temp_user_data.temp_data(user_id)[user_id][4]))
                    answers = GoogleTranslator(source='auto', target='en').translate(
                        text=','.join(temp_user_data.temp_data(user_id)[user_id][5]))
                    answer = chat_gpt.gpt_query([quests, answers, temp_user_data.temp_data(user_id)[user_id][2]], 1)
                    if message.from_user.language_code == 'ru':
                        pdf_creator.create_pdf(temp_user_data.temp_data(user_id)[user_id][2], GoogleTranslator(source='auto', target='ru').translate(text='\n'.join(answer)))
                    else:
                        pdf_creator.create_pdf(temp_user_data.temp_data(user_id)[user_id][2], '\n'.join(answer))
                    with open("plan.pdf", "rb") as misc:
                        obj = BytesIO(misc.read())
                        obj.name = 'plan.pdf'
                    bot.send_document(user_id, obj)
                    os.remove('plan.pdf')
                except Exception as e:
                    print(e)
                    bot.send_message(user_id, 'Произошла ошибка. Попробуйте ещё раз')
                temp_user_data.clear_temp_data(user_id)
                print(temp_user_data.temp_data(user_id)[user_id])

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
