import pickle
from note import Note
from view import View

class ListNotes:
    __notes = []  # Список заметок
    __view = View()  # Взаимод. с пользователем
    __index = 1  # Начальное значение индекса для идентификации заметок
    __index_stack = []  # Освободившиеся индексы

    def __init__(self):
        try:
            with open('notes_data.pkl', 'rb') as file: # Загрузка данных из файлов
                self.__notes = pickle.load(file)
                if self.__notes: # Если есть заметки, установить индекс +1, чем максимальный id
                    self.__index = max(note.get_id() for note in self.__notes) + 1
                else:
                    self.__index = 1  # Если заметок нет, начать с 1
            with open('indexes_data.pkl', 'rb') as file:
                self.__index_stack = pickle.load(file)
        except EOFError:
            self.__notes = [] # Если ошибка, то создать пустые списки и установить начальные значения
            self.__view = View()
            self.__index = 1
            self.__index_stack = []

    def add_note(self):
        note = Note() # Создание новой заметки
        note.set_name(self.__view.input_note_name())
        note.set_txt(self.__view.input_note_text())
        note.update_date()

        if self.__index_stack: # Установка id для заметки
            note.set_id(self.__index_stack.pop())
        else:
            note.set_id(self.__index)

        self.__index += 1  # Увеличение индекса +1 для следующей
        self.__notes.append(note)  # Добавление её в список
        self.__view.info_note_msg('add')  # Оповещение о успешности

    def delete_note(self, note):
        self.__index_stack.append(note.get_id()) # Удаление заметки и освобождение этого id
        self.__notes.remove(note)
        if len(self.__notes) == 0:
            self.__index_stack.clear()
        self.__view.info_note_msg('del')  # Оповещение о успешности действия

    def read_all(self):
        self.__view.show_read_all_banner(len(self.__notes)) # Показ всех заметок
        for note in self.__notes:
            self.__view.show_note(note)

    def manage_note(self):
        commands = {1: self.__view.show_note, # Управление по id
                    2: self.__view.edit_note,
                    3: self.delete_note}
        flag = False
        self.__view.show_manage_note_menu()
        choice = self.__view.input_number(len(commands.keys()), 'menu')
        value = self.__view.input_number(self.__index, 'id')
        for note in self.__notes:
            if note.get_id() == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.__view.not_found()

    def save_to_file(self):
        with open('notes_data.pkl', 'wb') as file: # Сохранение данных в файлы
            pickle.dump(self.__notes, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        with open('indexes_data.pkl', 'wb') as file:
            pickle.dump(self.__index_stack, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        self.__view.saved_info()
