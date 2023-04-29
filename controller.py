import csv
import view
import datetime
import readNote
import edit_a_note


# Выберите команду:\n\
# 1 - Создать новую заметку\n\
# 2 - Прочитать заметку\n\
# 3 - Отредактировать заметку\n\
# 4 - Удалить заметку\n\
# 5 - Показать список заметок\n\
# 6 - Выход из программы\n\
# : '))

def start():
    note_ID = 0
    while True:
        mode = view.get_operating_mode()

        if mode == 1:
            note_ID = note_ID+1
            title = view.get_note_title()
            note_body = view.get_note_body()
            dt_now = datetime.datetime.now()
            headers = ["ID", "Title", "Body", "Last_modified"]
            with open("Notes.csv", "a", newline='', encoding="UTF-8") as file:
                writer = csv.DictWriter(
                    file, fieldnames=headers, delimiter=';')
                writer.writerow(
                    {"ID": note_ID, "Title": title, "Body": note_body, "Last_modified": dt_now})
            print('\n' + "Заметка успешно сохранена!" + '\n')
        elif mode == 2:
            readNote.read_note()

        elif mode == 3: # 3 - Отредактировать заметку\n\
            edit_a_note.edit_note()



        elif mode == 6:
            print('\n' + 'Завершение работы.' + '\n')
            break
