import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('einkaufsliste.db')
cursor = conn.cursor()

# Tabelle 'groceries' erstellen, falls sie noch nicht existiert
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groceries (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount INTEGER,
            price REAL
        )
    ''')
    conn.commit()

create_table()

# Funktion zum Hinzufügen eines neuen Lebensmittels
def add_item():
    name = input("Folgndes musst du einkaufen: ")
    amount = int(input("Menge: "))
    price = float(input("Preis pro Einheit: "))
    
    cursor.execute('''
        INSERT INTO groceries (name, amount, price)
        VALUES (?, ?, ?)
    ''', (name, amount, price))
    conn.commit()
    print(f"'{name}' Artikel in die Einkaufsliste eingetragen.")

# Funktion zum Anzeigen der Einkaufsliste
def show_shoppinglist():
    cursor.execute('SELECT * FROM groceries')
    rows = cursor.fetchall()
    
    if rows:
        print("Deine Einkaufsliste:")
        for row in rows:
            print(f"ID: {row[0]}, Artikel: {row[1]}, Menge: {row[2]}, Preis: {row[3]:.2f} Euro")
    else:
        print("Alles leer.")

# Funktion zum Bearbeiten eines Eintrags
def update_item():
    item_id = int(input("Gib die ID des zu bearbeitenden Artikels ein: "))
    name = input("Neuer Name des Artikels: ")
    amount = int(input("Neue Menge: "))
    price = float(input("Neuer Preis pro Einheit: "))
    
    cursor.execute('''
        UPDATE groceries
        SET name = ?, amount = ?, price = ?
        WHERE id = ?
    ''', (name, amount, price, item_id))
    conn.commit()
    print("Der Artikel wurde aktualisiert.")

# Funktion zum Löschen eines Eintrags
def delete_item():
    item_id = int(input("Gib die ID des zu löschenden Artikels ein: "))
    cursor.execute('''
        DELETE FROM groceries
        WHERE id = ?
    ''', (item_id,))
    conn.commit()
    print("Der Artikel wurde gelöscht.")

# Hauptprogramm
def main():
    while True:
        print("\n----- Einkaufsliste -----")
        print("1. Artikel hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Artikel bearbeiten")
        print("4. Artikel löschen")
        print("5. Programm beenden")
        choice = input("Du hast die Wahl zwischen: (1, 2, 3, 4, 5): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Das war Falsch. Du hast die Wahl zwischen: 1, 2, 3, 4 oder 5.")

# Programm starten
if __name__ == "__main__":
    main()



