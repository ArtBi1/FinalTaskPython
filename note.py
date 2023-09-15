from datetime import datetime


class Note:
    __id = 0
    __name = ""
    __date = ""
    __txt = ""

    def set_id(self, value):
        self.__id = value

    def set_name(self, name):
        self.__name = name

    def set_txt(self, txt):
        self.__txt = txt

    def update_date(self):
        self.__date = datetime.now().strftime('%Y, %B %d, %A | %H:%M')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_txt(self):
        return self.__txt