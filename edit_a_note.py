import csv
import datetime
import view


# 1;Head-1;telo-1;2023-04-28 19:39:14.710388
# 2;Head-2;Telo-2;2023-04-28 19:39:22.307406
# 3;Head-3;Telo-3;2023-04-28 19:39:28.609585
# 1;поптыка33;тело новой заметки;2023-04-28 19:58:52.072867

def edit_note():
    rows = []
    with open ("Notes.csv", newline='') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            rows.append(row)
    
    title = view.get_note_title()
    new_body = view.get_new_body()
    dt_now = datetime.datetime.now()

    # with open("Notes.csv", "a", encoding="UTF-8") as file:
    #     writer = csv.writer(file, delimiter=";")
        




            

