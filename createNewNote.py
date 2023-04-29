import view
import datetime
import getAllNotes


def createNote():
    current_notes = getAllNotes.get_all_notes()
    note = []
    allID = []
    allTitle =[]

    for line in current_notes:
        allID.append(line[0])
        allTitle.append(line[1])

    while True:
        note_ID = view.get_note_ID()
        if note_ID in allID:
            print("Данный ID уже существует. Введите другой: ")
        else:
            break

    while True:
        title = view.get_note_title()
        if title in allTitle:
            print("Данный заголовок уже существует. Введите другой: ")
        else:
            break

    note_body = view.get_note_body()
    dt_now = datetime.datetime.now()

    note = [note_ID, title, note_body, dt_now]

    return note
