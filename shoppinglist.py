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


# Hauptprogramm
def main():
    while True:
        print("\n----- Einkaufsliste -----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        choice = input("Wähle eine Option (1, 2, 3): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen.")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3.")



if __name__ == "__main__":
    main()
