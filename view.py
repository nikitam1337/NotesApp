
def get_operating_mode():
    op_mode = int(input('Выберите команду:\n\
1 - Создать новую заметку\n\
2 - Прочитать заметку\n\
3 - Отредактировать заметку\n\
4 - Удалить заметку\n\
5 - Показать список заметок\n\
6 - Выход из программы\n\
: '))
    return op_mode

def get_note_title():
    title = input('Введите заголовок заметки: ')
    return title

def get_new_note_title():
    title = input('Введите новый заголовок заметки: ')
    return title

def get_note_body():
    body = input('Введите тело заметки:')
    return body

def get_new_body():
    body = input('Введите новое содержимое заметки:')
    return body

    