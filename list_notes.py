import pickle
from note import Note
from view import View


class ListNotes:
    __notes = []
    __view = View()
    __index = 1
    __index_stack = []

    def __init__(self):
        try:
            with open('notes_data.pkl', 'rb') as file:
                self.__notes = pickle.load(file)
            if self.__notes:
                self.__index = max(note.get_id() for note in self.__notes) + 1
            else:
                self.__index = 1
            with open('indexes_data.pkl', 'rb') as file:
                self.__index_stack = pickle.load(file)
        except EOFError:
            self.__notes = []
            self.__view = View()
            self.__index = 1
            self.__index_stack = []

    def add_note(self):
        note = Note()
        note.set_name(self.__view.input_note_name())
        note.set_txt(self.__view.input_note_text())
        note.update_date()

        if self.__index_stack:
            note.set_id(self.__index_stack.pop())
        else:
            note.set_id(self.__index)

        self.__index += 1  # Увеличиваем индекс после добавления заметки
        self.__notes.append(note)
        self.__view.info_note_msg('add')




    def delete_note(self, note):
        self.__index_stack.append(note.get_id())
        self.__notes.remove(note)
        if len(self.__notes) == 0:
            self.__index_stack.clear()
            self.__view.info_note_msg('del')


    def read_all_notes(self):
        self.__view.show_read_all_banner(len(self.__notes))
        for note in self.__notes:
            self.__view.show_note(note)

    def manage_note_by_id(self):
        commands = {1: self.__view.show_note,
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

    def save_notes_to_file(self):
        with open('notes_data.pkl', 'wb') as file:
            pickle.dump(self.__notes, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        with open('indexes_data.pkl', 'wb') as file:
            pickle.dump(self.__index_stack, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        self.__view.saved_info()