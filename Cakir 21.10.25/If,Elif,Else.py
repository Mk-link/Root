"""
if: Führt einen Block nur aus, wenn eine Bedingung True ist.
elif: Zusätzliche Bedingung, die geprüft wird, 
        wenn alle vorherigen if/elif False waren.
else: Fallback‑Block, der ausgeführt wird, 
        wenn keine der vorhergehenden Bedingungen zutrifft.

Wichtiges zur Syntax:

Bedingung gefolgt von Doppelpunkt (:).
Einrückung für den Block (meist 4 Leerzeichen).
elif/else sind optional; es darf höchstens ein else am Ende geben.
Bedingungen sind beliebige Ausdrücke mit Wahrheitswert 
(z. B. Vergleiche, boolsche Ausdrücke).

Vergleichsoperatoren: ==, !=, >, <, >=, <=
Logische Operatoren: and, or, not
"""
# Beispiel: Temperatur prüfen
temp = 18  
if temp >= 25:
    print("Es ist warm.")
elif temp >= 15:
    print("Es ist mild.")
else:
    print("Es ist kalt.")

# Beispiel für ternären Operator
message = "warm" if temp >= 25 else "nicht warm"

