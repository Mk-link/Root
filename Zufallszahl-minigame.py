import random       # Importieren des random-Moduls für die Zufallszahlenerzeugung

print("Geben Sie eine Zahl zwischen 1 und 5 ein:")
input_value = input()                           # Benutzereingabe einlesen

if input_value.isdigit():                       # Überprüfen, ob die Eingabe eine Zahl ist
    user_number = int(input_value)              # In eine Ganzzahl umwandeln
    if 1 <= user_number <= 5:                   # Überprüfen, ob die Zahl im gültigen Bereich liegt
        random_number = random.randint(1, 5)    # Zufallszahl zwischen 1 und 5 generieren
        if user_number == random_number:        # Vergleich der Benutzereingabe mit der Zufallszahl
            print("Glückwunsch! Sie haben gewonnen.")
        else:
            print(f"Leider verloren. Die richtige Zahl war {random_number}.")   # Ausgabe der Zufallszahl bei Verlust
    else:
        print("Die Zahl muss zwischen 1 und 5 liegen.")  # Fehlermeldung bei ungültigem Bereich

print("Danke fürs Spielen!")                    # Abschließende Nachricht an den Benutzer