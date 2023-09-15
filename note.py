from datetime import datetime  # Для работы с датой и временем

class Note:
    __id = 0  # Уникальный id заметки
    __name = ""  # Заголовок/название
    __date = ""  # Дата и время создания/последнего изменения
    __txt = ""  # Текст заметки

    def set_id(self, value):
        self.__id = value  # Установка id

    def set_name(self, name):
        self.__name = name  # Установка заголовка

    def set_txt(self, txt):
        self.__txt = txt  # и текста заметки

    def update_date(self):
        self.__date = datetime.now().strftime('%Y, %B %d, %A | %H:%M')  # Обновление даты и времени

    def get_id(self):
        return self.__id  # Получение id

    def get_name(self):
        return self.__name  # Получение заголовка

    def get_date(self):
        return self.__date  # Получение даты и времени

    def get_txt(self):
        return self.__txt  # Получение текста
