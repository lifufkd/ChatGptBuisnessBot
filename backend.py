#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import time
from datetime import datetime
from fpdf import FPDF
from PIL import Image


#####################################

class TempUserData:
    def __init__(self):
        self.__user_data = {}

    def temp_data(self, user_id):
        if user_id not in self.__user_data.keys():
            self.__user_data.update({user_id: [None, None, []]})
        return self.__user_data


class PDFCreate:
    def __init__(self):
        super(PDFCreate, self).__init__()

    def create_pdf(self, company_name, text):
        # Создаем PDF файл с дизайном
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font('Arial', size=20)

        # Добавляем дизайн в PDF файл
        pdf.image('DesignPDF.png', x=0, y=0, w=210, h=297)

        # Добавляем логотип в правом верхнем углу
        pdf.image('logo.png', x=87, y=40, w=40, h=40)

        # Добавляем текст "Your Company Name"
        pdf.set_xy(0, 80)
        pdf.cell(210, 20, company_name, 0, 1, 'C')

        # Добавляем длинный текст

        # Разбиваем текст на строки, чтобы он не выходил за границы страницы
        lines = pdf.multi_cell(w=0, h=10, txt=text)

        # Сохраняем изменения в PDF файле
        pdf.output('pdftest.pdf')
