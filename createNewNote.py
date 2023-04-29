import csv
import view
import datetime

def createNote():
    note=[]
    note_ID = 1
    title = view.get_note_title()
    note_body = view.get_note_body()
    dt_now = datetime.datetime.now()

    note=[note_ID, title, note_body, dt_now]

    with open("Notes.csv", "a", newline='', encoding="UTF-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(note)  
    
    print('\n' + "Заметка успешно сохранена!" + '\n')



