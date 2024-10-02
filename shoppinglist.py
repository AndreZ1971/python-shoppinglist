
shoppinglist = []


def add_item():
    item = input("Folgndes musst du einkaufen: ")
    shoppinglist.append(item)
    print(f"'{item}' Artikel in die Einkaufsliste eingetragen.")



def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufsliste:")
        for item in shoppinglist:
            print(f"- {item}")
    else:
        print("Alles leer.")



def main():
    while True:
        print("\n----- Einkaufsliste -----")
        print("1. Artikel in die Einkaufsliste eingetragen")
        print("2. Zeig mir was ich holen soll.")
        print("3. Programm beenden")
        choice = input("Du hast die Wahl zwischen: (1, 2, 3): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Auf Wiedersehen.")
            break
        else:
            print("Das war Falsch. Du hast die Wahl zwischen: 1, 2 oder 3.")



if __name__ == "__main__":
    main()
2