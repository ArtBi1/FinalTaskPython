class View:
    def greeting(self):
        print("Здравствуйте! Вы открыли Заметки. ")

    def show_main_menu(self):
        print("Выберите действие:\n"
              "\t1. Добавить заметку\n"
              "\t2. Прочитать / Изменить / Удалить заметку\n"
              "\t3. Показать список заметок\n"
              "\t4. Сохранить заметки\n"
              "\t0. Завершить работу приложения")

    def show_manage_note_menu(self):
        print("Выберите необходимое:\n"
              "\t1. Прочитать заметку\n"
              "\t2. Изменить заметку\n"
              "\t3. Удалить заметку\n")

    def error(self):
        print("Введенное число некорректно! Попробуйте снова:")

    def not_found(self):
        print("Значение не найдено. Повторите попытку:")

    def saved_info(self):
        print("Сохранение успешно!")

    def show_note(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"[{str(note.get_date())}]\t"
        result += f"[{str(note.get_name())}]\n"
        result += f"{str(note.get_txt())}\n"
        print(result)

    def show_read_all_banner(self, count):
        result = f"\t Все заметки:\n" \
                 f"Найдено заметок: {count}\n"
        print(result)

    def info_note_msg(self, key):
        info = {'add': 'добавлена', 'del': 'удалена', 'edit': 'изменена'}
        print(f"Заметка успешно {info[key]}!")

    def input_note_name(self):
        return input(f"Введите имя заметки:")

    def input_note_text(self):
        return input(f"Введите текст заметки:")

    def edit_note(self, note):
        note.set_txt(self.input_note_text())
        note.update_date()
        self.info_note_msg('edit')

    def input_number(self, limit, preset):
        presets = {'id': 'заметки', 'menu': 'пункта меню'}
        value = 0
        while True:
            try:
                value = int(input(f"Введите номер {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= limit:
                break
            else:
                self.not_found()
        return value

    def exit_msg(self):
        print("До свидания!")