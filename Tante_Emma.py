import sys
from datetime import datetime


DEFAULT_PIN = "2206"

def require_admin(prompt: str = "Willkommen bei Tante Emma.Bitte gib den Jugendschutzcode ein: ") -> bool:
    """
    Fordert die PIN bis zu 3-mal an. Gibt True zurück, wenn die richtige PIN eingegeben wurde.
    Einfaches Beispiel; in Produktion niemals Klartext-PINs im Code.
    """
    for attempt in range(3):
        pin = input(prompt).strip()
        if pin == DEFAULT_PIN:
            print("PIN korrekt.Was darf es sein ?\n")
            return True
        print("Falsche PIN.")
    print("Zugriff verweigert.")
    return False

DEFAULT_QTY = 2

# Einfacher Automat mit 10 Artikeln (jeweils DEFAULT_QTY Stück)
inventory = [
    {"name": "Schokolade", "price": 3.20, "qty": DEFAULT_QTY},
    {"name": "Chips", "price": 2.50, "qty": DEFAULT_QTY},
    {"name": "Kaugummi", "price": 0.80, "qty": DEFAULT_QTY},
    {"name": "Wasser", "price": 1.20, "qty": DEFAULT_QTY},
    {"name": "Bier", "price": 1.40, "qty": DEFAULT_QTY},
    {"name": "Kaffeebohnen", "price": 13.90, "qty": DEFAULT_QTY},
    {"name": "Tee", "price": 1.90, "qty": DEFAULT_QTY},
    {"name": "Kekse", "price": 3.90, "qty": DEFAULT_QTY},
    {"name": "Nüsse", "price": 4.70, "qty": DEFAULT_QTY},
    {"name": "Zigaretten", "price": 4.30, "qty": DEFAULT_QTY},
]

def format_euro(value: float) -> str:
    s = f"{value:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{s} €"

def show_list():
    print("\nVerfügbare Waren:")
    for i, item in enumerate(inventory, start=1):
        avail = "nicht verfügbar" if item.get("qty", 0) <= 0 else f"Anzahl: {item['qty']}"
        print(f"{i}. {item['name']} - {format_euro(item['price'])} ({avail})")
    print()

def refill_all(default: int = DEFAULT_QTY):
    for item in inventory:
        item['qty'] = default
    print(f"Alle Artikel wurden wieder auf {default} Stück aufgefüllt.\n")

def all_sold_out() -> bool:
    return all(item.get("qty", 0) <= 0 for item in inventory)

def print_invoice(cart: dict):
    """
    Druckt die Rechnung für die im Cart gesammelten Artikel.
    cart: dict name -> {'price': float, 'qty': int}
    Ausgabe: jede Position untereinander, Einzelpreis einmal (ohne '@'), mit Zeilen- und Gesamtsumme.
    """
    if not cart:
        print("\nKeine gekauften Artikel. Keine Rechnung.\n")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n======= Rechnung =======")
    print(f"Datum: {now}\n")

    total = 0.0
    # Kopfzeile: Pos., Artikel, Stck., Einzelpreis (Summe-Spalte entfernt)
    print(f"{'Pos.':<4} {'Artikel':<20} {'Stck.':>5} {'Einzelpreis':>14}")
    print("-" * 60)

    for i, (name, info) in enumerate(cart.items(), start=1):
        qty = info['qty']
        unit = info['price']
        line_total = qty * unit
        total += line_total
        # Einzelpreis in der letzten Spalte (Summe-Spalte entfernt)
        print(f"{i:<4} {name:<20} {qty:>5} {format_euro(unit):>14}")

    print("-" * 60)
    # Gesamtsumme rechts unter der Einzelpreis-Spalte ausrichten
    print(f"{'Gesamt:':>31} {format_euro(total):>14}")
    print("==T==A==N==T==E====E==M==M==A==\n")

def purchase_loop():
    # Jugendschutzkontrolle VOR dem Anzeigen der Liste durchführen
    if not require_admin():
        print("Zugriff verweigert. Programm beendet.")
        return

    # Einkaufswagen: name -> {'price': float, 'qty': int}
    cart = {}

    while True:
        show_list()
        if all_sold_out():
            print("Keine Artikel mehr verfügbar. Der Automat ist leer.")
            print_invoice(cart)
            return

        raw = input("Wähle die Nummer der Ware (0 zum Beenden, 'refill' zum Auffüllen): ").strip().lower()
        if raw in ("refill", "r"):
            refill_all()
            continue

        try:
            choice = int(raw)
        except ValueError:
            print("Ungültige Eingabe. Bitte eine ganze Zahl, 0 oder 'refill' eingeben.\n")
            continue

        if choice == 0:
            print("Vorgang beendet.")
            print_invoice(cart)
            return

        if not (1 <= choice <= len(inventory)):
            print("Ungültige Artikelnummer. Bitte erneut wählen.\n")
            continue

        idx = choice - 1
        item = inventory[idx]
        qty = item.get("qty", 0)
        print(f"\nAusgewählt: {item['name']}")
        print(f"Verfügbarkeit: {'ja' if qty > 0 else 'nein'} (Anzahl: {qty})")
        print(f"Preis: {format_euro(item['price'])}")

        if qty <= 0:
            print("Dieser Artikel ist aktuell leider nicht verfügbar. Bitte wähle einen anderen Artikel oder schau Morgen wieder rein.\n")
            continue

        # Direktkauf: keine zusätzliche j/n Abfrage nach Nummerneingabe
        # Stückzahl verringern
        item['qty'] = qty - 1

        # In den Warenkorb legen / Menge erhöhen
        name = item['name']
        if name in cart:
            cart[name]['qty'] += 1
        else:
            cart[name] = {'price': item['price'], 'qty': 1}

        print(f"{name} wurde dem Warenkorb hinzugefügt.\n")

        # Frage, ob weitere Einkäufe stattfinden sollen; wenn nicht, Rechnung ausgeben und beenden
        again = input("Möchten Sie noch etwas kaufen? (j/n): ").strip().lower()
        if again not in ("j", "y"):
            print("Danke für Ihren Einkauf. Hier ist Ihre Rechnung:")
            print_invoice(cart)
            return

if __name__ == "__main__":
    try:
        purchase_loop()
    except KeyboardInterrupt:
        print("\nProgramm beendet.")
        sys.exit(0)