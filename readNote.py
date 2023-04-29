import csv
import view


def read_note():
    title = view.get_note_title()

    with open("Notes.csv", "r", encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter=";")
        for line in reader:
            if line[1] == title:
                print()
                print("Содержимое заметки:")
                print(line[2])