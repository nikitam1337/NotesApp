import csv

def get_all_notes():
    notes = []
    with open("Notes.csv", "r", encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter=";")
        for line in reader:
            notes.append(line)
    return notes
