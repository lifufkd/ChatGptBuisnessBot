from googletrans import Translator

translator = Translator()

x = translator.translate('1. What are the current challenges or obstacles your business is facing?', dest='ru')

print(x.text)
