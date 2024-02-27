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
            self.__user_data.update({user_id: [None, None, None, -1, [], []]}) # status, lang, main_question, counter_of_sub_quests, answers
        return self.__user_data

    def clear_temp_data(self, user_id):
        if user_id in self.__user_data.keys():
            self.__user_data[user_id] = copy.deepcopy(self.__default)


class ChatGpt:
    def __init__(self):
        super(ChatGpt, self).__init__()
        self.__base_prompt = {'ru': {0: 'Составь наводящие вопросы помогающие составить бизнес план для ', 1: 'Составь бизнес план по ключевым особенностям '},
                                'en': {0: 'Make up leading questions to help you make a business plan for ', 1: 'Make a business plan based on key features '}}

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
        pdf.set_font('Arial', size=20)

        # Загружаем фотографию
        image_path = 'DesignPDF.png'

        # Функция для вставки изображения на каждую страницу
        def add_image_on_page(image_path):
            pdf.image(image_path, x=0, y=0, w=210, h=297)

        # Вставляем дизайн на каждую страницу
        for i in range(1, pdf.page_no() + 1):
            pdf.set_page(i)
            add_image_on_page(image_path)

        # Добавляем логотип
        pdf.image('logo.png', x=87, y=40, w=40, h=40)
        # Добавляем текст "Your Company Name"
        pdf.set_xy(0, 80)
        pdf.cell(210, 20, company_name, 0, 1, 'C')

        # Добавляем длинный текст

        # Разбиваем текст на строки, чтобы он не выходил за границы страницы
        lines = pdf.multi_cell(w=0, h=10, txt=text)

        # Сохраняем изменения в PDF файле
        pdf.output('plan.pdf')
