# Waiter.py

menu = {
    "Pizza": {"price": 8.5, "prep_time": 15},
    "Salat": {"price": 5.0, "prep_time": 7},
    "Pasta": {"price": 7.0, "prep_time": 12},
    "Suppe": {"price": 4.5, "prep_time": 10}
}

def waiter():
    print("Willkommen! Unsere Speisekarte:")
    for dish in menu:
        print(f"- {dish}")

    while True:
        choice = input("Bitte geben Sie Ihr gewünschtes Gericht ein: ")
        if choice in menu:
            info = menu[choice]
            print(f"{choice}: Preis: {info['price']}€, Zubereitungsdauer: {info['prep_time']} Minuten.")
            break
        else:
            print("Entschuldigung, das Gericht ist nicht auf der Karte. Bitte suchen Sie etwas anderes aus.")

if __name__ == "__main__":
    waiter()