class View:
    def greeting(self):
        print("Здравствуйте! Вы открыли Заметки! ")  # Приветствие
    def show_main_menu(self): # Отображение главного меню
        print("Выберите действие:\n"
              "\t1. Добавить заметку\n"
              "\t2. Прочитать / Изменить / Удалить заметку\n"
              "\t3. Показать список заметок\n"
              "\t4. Сохранить заметки\n"
              "\t0. Завершить работу приложения")

    def show_manage_note_menu(self): # Отображение меню 2)управления заметкой
        print("Выберите необходимое:\n"
              "\t1. Прочитать заметку\n"
              "\t2. Изменить заметку\n"
              "\t3. Удалить заметку\n")

    def error(self):
        print("Введенное число некорректно! Попробуйте снова:")  # Ошибка ввода числа

    def not_found(self):
        print("Значение не найдено. Повторите попытку:")  # Сообщ: неуд. поиск

    def saved_info(self):
        print("Сохранение успешно!")  # Сообщ: Усп. сохр. дан.

    def show_note(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"[{str(note.get_date())}]\t"
        result += f"[{str(note.get_name())}]\n"
        result += f"{str(note.get_txt())}\n"
        print(result)  # Отображение инфы о заметке

    def show_read_all_banner(self, count):
        result = f"\t Все заметки:\n" \
                 f"Найдено заметок: {count}\n"
        print(result)  # Отображение инфы о всех заметках

    def info_note_msg(self, key):
        info = {'add': 'добавлена', 'del': 'удалена', 'edit': 'изменена'}
        print(f"Заметка успешно {info[key]}!")  # Информация об успешном выполнении операции с заметкой

    def input_note_name(self):
        return input(f"Введите имя заметки:")  # Ввод имени заметки

    def input_note_text(self):
        return input(f"Введите текст заметки:")  # Ввод её текста
    def edit_note(self, note):
        note.set_txt(self.input_note_text())  # Редактирование её текста
        note.update_date()
        self.info_note_msg('edit')  # Обновление даты и времени изменения

    def input_number(self, limit, preset):
        presets = {'id': 'заметки', 'menu': 'пункта меню'}
        value = 0
        while True:
            try:
                value = int(input(f"Введите номер {presets[preset]}: "))  # Ввод числа
            except ValueError:
                self.error()
                continue
            if 0 <= value <= limit:
                break
            else:
                self.not_found()
        return value

    def exit_msg(self):
        print("До свидания!")  # Прощание