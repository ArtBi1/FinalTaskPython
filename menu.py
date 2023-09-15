from list_notes import ListNotes
from view import View


class Menu:
    __view = View()
    __notes = ListNotes()
    __commands = {1: __notes.add_note, 2: __notes.manage_note_by_id, 3: __notes.read_all_notes,
                  4: __notes.save_notes_to_file}

    def start(self):
        self.__view.greeting()
        while(True):
            self.__view.show_main_menu()
            choice = self.__view.input_number(len(self.__commands.keys()), 'menu')
            if choice == 0:
                self.__view.exit_msg()
                break
            else:
                self.__commands[choice]()