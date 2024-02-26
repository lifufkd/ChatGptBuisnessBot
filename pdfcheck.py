from fpdf import FPDF
from PIL import Image

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
pdf.cell(210, 20, 'Your Company Name', 0, 1, 'C')

# Добавляем длинный текст
text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry standard dummy text ever since the 1500s, "
        "when an unknown printer took a galley of type and scrambled it to make a type "
        "specimen book. It has survived not only five centuries, but also the leap into "
        "electronic typesetting, remaining essentially unchanged.")

# Разбиваем текст на строки, чтобы он не выходил за границы страницы
lines = pdf.multi_cell(w=0, h=10, txt=text)

# Сохраняем изменения в PDF файле
pdf.output('pdftest.pdf')