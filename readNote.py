import view

def read_note(allNotes):
    title = view.get_note_title()
    notes = allNotes
    for line in notes:
        if line[1] == title:
            print("\n" + "Содержимое заметки: "+line[2] + "\n")
