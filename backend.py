#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import time
from datetime import datetime


#####################################

class TempUserData:
    def __init__(self):
        self.__user_data = {}

    def temp_data(self, user_id):
        if user_id not in self.__user_data.keys():
            self.__user_data.update({user_id: [None, None, []]})
        return self.__user_data