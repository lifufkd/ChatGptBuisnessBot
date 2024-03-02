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
from googletrans import Translator


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

    def detect_language(self, text):
        return detect(text)

    def gpt_query(self, prompt, index):
        answer = ''
        if index == 0:
            base_prompt = f"You are a business consultant. Understand the client's needs, learn more about their business," \
                          f" {prompt}, understand their goals, problems and expectations, ask questions to deepen your " \
                          f"understanding of the situation and business needs. Your questions should be easy to understand " \
                          f"for the client, don't go into complex terminology or go off topic about the client's business. " \
                          f"The questions should be logical, connected questions so that you have a clear understanding of " \
                          f"the client's business. "
        else:
            base_prompt = f"based on the {prompt[1]} provided to the {prompt[0]}, assess the company's current strategies, " \
                          f"processes and resources. After the assessment, analyze the data and develop specific " \
                          f"recommendations and strategies to improve their business. Provide the result as formatted text"
        try:
            answer = Client.create_completion("gpt3", f'{base_prompt}')
        except:
            pass
        if index == 0:
            t = list()
            for i in answer.split('?'):
                if len(i) != 0:
                    t.append(i)
            return t
        else:
            return answer.split('\n')


class PDFCreate:
    def __init__(self):
        super(PDFCreate, self).__init__()

    def create_pdf(self, company_name, text):
        print(company_name)
        print(text)
        # Создаем PDF файл с дизайном
        pdf = FPDF()
        pdf.add_font('Arial', '', 'arial.ttf', uni=True)
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
        pdf.set_font('Arial', 'B', size=28)
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
