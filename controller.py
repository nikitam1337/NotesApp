import csv
import view
import datetime
import readNote
import edit_a_note
import createNewNote
import deleteNote
import getAllNotes
import showListNotes

def start():
    note_ID = 0
    while True:
        mode = view.get_operating_mode()

        if mode == 1: # 1 - Создать новую заметку
            createNewNote.createNote()

        elif mode == 2: # 2 - Прочитать заметку
            notes = getAllNotes.get_all_notes()
            readNote.read_note(notes)
            
        elif mode == 3: # 3 - Отредактировать заметку
            notes = getAllNotes.get_all_notes()
            edit_a_note.edit_note(notes)
        
        elif mode == 4: # 4 - Удалить заметку
            notes = getAllNotes.get_all_notes()
            deleteNote.delete_note(notes)
        
        elif mode == 5: # 5 - Показать список заметок
            notes = getAllNotes.get_all_notes()
            showListNotes.showListNotes(notes)

        elif mode == 6: # 6 - Выход из программы\n\
            print('\n' + 'Завершение работы.' + '\n')
            break
