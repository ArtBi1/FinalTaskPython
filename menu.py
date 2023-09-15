from list_notes import ListNotes  # Импорт классов
from view import View

class Menu:
    __view = View()  # Создание экземпляра класса View для взаимодействия с пользователем
    __notes = ListNotes()  # Создание экземпляра класса ListNotes для управления заметками
    __commands = {  # Словарь команд, связанных с функциями ListNotes
        1: __notes.add_note,  # Для добавления заметки
        2: __notes.manage_note,  # Для управления заметкой по id
        3: __notes.read_all,  # Для чтения всех заметок
        4: __notes.save_to_file  # Для сохранения заметок в файл
    }

    def start(self):
        self.__view.greeting()  # Приветствие пользователя
        while(True):
            self.__view.show_main_menu()  # Отображение главного меню
            choice = self.__view.input_number(len(self.__commands.keys()), 'menu')  # Ввод от пользователя
            if choice == 0:
                self.__view.exit_msg()  # Оповещение о завершении работы
                break
            else:
                self.__commands[choice]()  # Выполнение выбранной команды
