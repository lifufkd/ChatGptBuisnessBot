#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import copy
from freeGPT import Client
from langdetect import detect
#####################################


class TempUserData:
    def __init__(self):
        super(TempUserData, self).__init__()
        self.__user_data = {}
        self.__default = [None, None, None, []]

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