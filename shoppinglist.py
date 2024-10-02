# Liste, in der die Artikel gespeichert werden
shoppinglist = []

# Funktion zum Hinzufügen eines Artikels
def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
    shoppinglist.append(item)
    print(f"'{item}' wurde der Einkaufsliste hinzugefügt.")


# Funktion zur Anzeige der Einkaufsliste
def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufsliste:")
        for item in shoppinglist:
            print(f"- {item}")
    else:
        print("Deine Einkaufsliste ist leer.")

