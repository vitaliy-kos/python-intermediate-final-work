from random import *
from datetime import datetime
import json

notes = {}

def save_note(id, name, body):

    dt_now = datetime.now()
    dt_now_str = dt_now.strftime("%Y-%m-%d %H:%M:%S")
    notes = get_notes()
    notes.append({'id': id, 'name': name, 'body': body, 'date': dt_now_str})

    with open("python-intermediate-final-work/notes.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(notes, ensure_ascii=False))
    return

def delete_note(id):
    notes = get_notes()
    i = 0
    for note in notes:
        if(note['id'] == int(id)):
            del notes[i]
            save_notes(notes)
            return True
        i += 1

    return False

def save_notes(notes):
    with open("python-intermediate-final-work/notes.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(notes, ensure_ascii=False))
    return


def get_notes():
    with open("python-intermediate-final-work/notes.json", "r", encoding="utf-8") as fh:
        notes = json.load(fh)

    sorted_notes = sorted(notes, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=True)

    return sorted_notes

def find_max_id(notes):
    max_id = 0
    for note in notes:
        if (note['id'] > max_id):
            max_id = note['id']
    return max_id

def get_note_by_id(id):
    notes = get_notes()
    for note in notes:
        if (note['id'] == int(id)):
            return note
    return False

while True:
    command = input("*** Введите команду: ")

    if command == 'list':

        notes_list = get_notes()

        print("------ \nСписок заметок: ")
        for note in notes_list:
            print("- Заметка №" + str(note['id']) + ": " + note['name'] + " (" + note['date'] + ")")
        print("------")
        continue

    if command == 'read':

        note_id = input("Введите номер заметки, которую хотите прочитать: ")

        note = get_note_by_id(note_id)

        if (note):
            print("------\nЗаметка №" + str(note['id']) + " от " + note['date'] + "\nНазвание заметки: " + note['name'] + "\nТекст заметки: " + note['body'] + "\n------")
        else:
            print("Заметка с таким номером не найдена.\n------")

        continue

    if command == 'add':

        print("Введите название заметки: ")
        name = input()
        
        print("Введите текст заметки: ")
        body = input()

        notes_list = get_notes()

        if (len(notes_list) > 0):
            id = find_max_id(notes_list) + 1
        else:
            id = 1

        save_note(id, name, body)
        print("заметка сохранена.\n------")
        continue

    if command == 'edit':

        note_id = input("Введите номер заметки, которую хотите изменить: ")

        note = get_note_by_id(note_id)

        if (note):
            print("------\nЗаметка №" + str(note['id']) + " от " + note['date'] + "\nНазвание заметки: " + note['name'] + "\nТекст заметки: " + note['body'] + "\n------\n *Режим редактирования*")
        else:
            print("Заметка с таким номером не найдена.\n------")
            continue

        print("Введите новое название заметки: ")
        name = input()
        
        print("Введите новый текст заметки: ")
        body = input()

        if (delete_note(note['id'])):
            save_note(note['id'], name, body)

        print("заметка успешно обновлена.\n------")
        continue

    if command == 'delete':

        delete_note_id = input("Введите номер заметки, которую нужно удалить: ")

        if (delete_note(delete_note_id)):
            print("Заметка удалена успешно.\n------")
        else:
            print("Заметка с таким номером не найдена.\n------")

        continue

    if command == 'help':

        print("------ \nПриложение имеет следующие функции: \nlist - просмотр списка заметок, \nadd - добавить заметку, \nread - чтение заметки (указать № заметки), \nedit - изменить заметку (указать № заметки), \ndelete - удалить заметку (указать № заметки), \nhelp - посмотреть туториал\n------")
    
    else:
        
        print("Неопознанная команда. Изучите мануал - введите help.")