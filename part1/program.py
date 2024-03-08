import json
import datetime
import sys
import os

class NoteManager:
    def __init__(self, file_name):
        # Загрузка всех заметок из файла
        self.notes = self.__load_notes(file_name)

    # Возвращает список заметок (без текста)
    def get_notes_list(self):
        notes = []
        for note in self.notes:
            notes.append("{}. {}\tДата создания: {}".format(note.id, note.head, note.created_at))
        return notes

    # Поиск заметки по id (публичный, возвращает строку)
    def find_note(self, id):
        data = self.__find_note_by_id(id)
        if data != False:
            return "\nid: {} \nЗаголовок: {} \nДата создания: {} \n\t{}".format(data.id, data.head, data.created_at, data.text)
        return "Заметка не найдена"
    
    # Создание заметки (без сохранения)
    def create_note(self, head, text):
        id = ((self.notes[-1]).id + 1) if len(self.notes) != 0 else 1
        note = self.__Note(id, head, text)
        self.notes.append(note)

    # Редактирование заметки по id
    def edit_note(self, id):
        data = self.__find_index_note_by_id(id)
        if data > -1:
            print("Введите данные (если не нужно менять нажмите Enter)")
            head = input("Введите заголовок: ")
            text = input("Введите текс: ")
            if head != "":
                (self.notes[data]).head = head
            if text != "":
                (self.notes[data]).text = text
            return "Данные успешно изменены"
        return "Заметка не найдена"
    
    # Удаление заметки по id
    def delete_note(self, id):
        data = self.__find_index_note_by_id(id)
        if data > -1:
            del self.notes[data]
            if self.__find_index_note_by_id(id) == -1:
                return "Данные успешно удалены"
            else: 
                return "Ошибка в сохранении данных"
        return "Заметка с id {} не найдена".format(id)

    # Сохранение всех заметок
    def save_notes(self, file_name):
        with open(file_name, "w") as file:
            note_list = []
            for note in self.notes:
                note_dict = {
                    "id" : note.id,
                    "head" : note.head,
                    "text": note.text,
                    "created_at": note.created_at
                }
                note_list.append(note_dict)
            json.dump(note_list, file)

    # Выгрузка заметок в список
    def __load_notes(self, file_name):
        if os.path.exists("notes.json"):
            with open(file_name, "r") as file:
                note_list = json.load(file)
                notes = []
                for note_dict in note_list:
                    note = self.__Note(note_dict["id"], note_dict["head"], note_dict["text"])
                    note.created_at = note_dict["created_at"]
                    notes.append(note)
                return notes
        else:
            return []

    # Поиск заметки по id (приватный, возвращает заметку)
    def __find_note_by_id(self, id):
        for note in self.notes:
            if id == note.id:
                return note
        return False
    
    # Поиск индекса заметки по id
    def __find_index_note_by_id(self, id):
        for i in range(len(self.notes)):
            note = self.notes[i]
            if id == note.id:
                return i
        return -1
    
    class __Note:
        def __init__(self, id, head, text):
            self.id = id
            self.head = head
            self.text = text
            self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class View:
    def __init__(self):
        self.file_name = "notes.json"
        self.manager = NoteManager(self.file_name)
        self.main_menu_strings = ["\nГЛАВНОЕ МЕНЮ\n", 
                                  "1 - посмотреть список заметок\n", 
                                  "2 - посмотреть заметку по id\n", 
                                  "3 - создать заметку\n", 
                                  "4 - редактировать заметку\n", 
                                  "5 - удалить заметку\n", 
                                  "6 - сохранить изменения\n"
                                  "7 - выйти\n", 
                                  "\nВведите номер команды: "]
        
    # Работа с менеджером заметок
    def run(self):
        while(True):
            try:
                self.main_menu_output()
                com = int(input())
                if com == 1:
                    for note in self.manager.get_notes_list():
                        print(note)
                elif com == 2:
                    print(self.manager.find_note(int(input("Введите id заметки: "))))
                elif com == 3:
                    self.manager.create_note(input("Введите заголовок: "), input("Введите текст заметки: "))
                elif com == 4:
                    print(self.manager.edit_note(int(input("Введите id заметки: "))))
                elif com == 5:
                    print(self.manager.delete_note(int(input("Введите id заметки: "))))
                elif com == 6:
                    self.manager.save_notes(self.file_name)
                elif com == 7:
                    sys.exit()
                else:
                    print("Неверный ввод")
            except ValueError:
                print("Неверный ввод")
            
    # Вывод главного меню
    def main_menu_output(self):
        for string in self.main_menu_strings:
            print(string, end="")

start = View()
start.run()