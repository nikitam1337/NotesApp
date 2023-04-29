def showListNotes(allNotes):
    notes = allNotes
    for line in notes:
        print("|" + line[1] + "| " + " Содержимое: " + line[2] + "\n")
