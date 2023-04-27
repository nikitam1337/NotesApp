import csv
import view


# Выберите команду:\n\
# 1 - Создать новую заметку\n\
# 2 - Прочитать заметку\n\
# 3 - Отредактировать заметку\n\
# 4 - Удалить заметку\n\
# 5 - Показать список заметок\n\
# 6 - Выход из программы\n\
# : '))

def start():

    while True:
        mode = view.get_operating_mode()
        note_ID = 0
        if mode == 1:
            # note_ID = 1
            title = view.get_note_title()
            note_body = view.get_note_body()
            header = ["ID", "Title", "Body", "Last_modified"]
            with open("Notes.csv", "a", newline='',encoding="cp1251") as file:
                # quoting=csv.QUOTE_NONNUMERIC
                writer = csv.DictWriter(file, fieldnames=header, delimiter=';')
                writer.writeheader()
                writer.writerow(
                    {"ID": note_ID, "Title": title, "Body": note_body, "Last_modified": 2023})
            print('\n' + "Заметка успешно сохранена!" + '\n')
        elif mode == 6:
            print('\n' + 'Завершение работы.' + '\n')
            break
