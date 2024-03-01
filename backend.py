#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import copy
from freeGPT import Client
from langdetect import detect
from fpdf import FPDF
from PIL import Image


#####################################


class TempUserData:
    def __init__(self):
        super(TempUserData, self).__init__()
        self.__user_data = {}
        self.__default = [None, None, None, -1, [], []]

    def temp_data(self, user_id):
        if user_id not in self.__user_data.keys():
            self.__user_data.update({user_id: [None, None, None, -1, [],
                                               []]})  # status, lang, main_question, counter_of_sub_quests, answers
        return self.__user_data

    def clear_temp_data(self, user_id):
        if user_id in self.__user_data.keys():
            self.__user_data[user_id] = copy.deepcopy(self.__default)


class ChatGpt:
    def __init__(self):
        super(ChatGpt, self).__init__()
        self.__base_prompt = {'ru': {0: 'Составь наводящие вопросы помогающие составить бизнес план для ',
                                     1: 'Напиши очень подробный бизнес-план для моего бизнеса отвечающего требованиям по вопросам и ответам на них в соответственном порядке'},
                              'en': {0: 'Make up leading questions to help you make a business plan for ',
                                     1: 'Write a very detailed business plan for my business that meets the requirements for questions and answers in the appropriate order'}}

    def detect_language(self, text):
        return detect(text)

    def gpt_query(self, prompt, lang, index):
        if lang != 'ru':
            lang = 'en'
        answer = ''
        try:
            answer = Client.create_completion("gpt3", f'{self.__base_prompt[lang][index]}{prompt}')
        except:
            pass
        return answer.split('\n')


class PDFCreate:
    def __init__(self):
        super(PDFCreate, self).__init__()

    def create_pdf(self, company_name, text):
        # Создаем PDF файл с дизайном
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Добавляем первую страницу в PDF файл
        pdf.image('FirstPage.png', x=0, y=0, w=210, h=297)

        # Добавляем вторую страницу с дизайном в PDF файл
        pdf.add_page()
        pdf.image('PageNo2.png', x=0, y=0, w=210, h=297)


        # Добавляем вторую страницу в PDF файл
        pdf.add_page()
        pdf.image('SecondPage.png', x=0, y=0, w=210, h=297)
        pdf.set_xy(0, 100)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('Arial', size=28, style='B')
        pdf.cell(220, -125, company_name, 0, 1, 'C')
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', size=15)
        # Добавляем ответы бота на 10 вопросов
        pdf.set_xy(0, 100)
        pdf.multi_cell(w=0, h=10, txt=text)


        # # Добавляем последнюю страницу в PDF файл
        # pdf.add_page()
        # pdf.image('LastPage.png', x=0, y=0, w=210, h=297)

        # Сохраняем изменения в PDF файле
        pdf.output('plan.pdf')
