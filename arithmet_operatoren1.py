
strompreis = 0.40  # Euro pro kWh
verbrauch_tv= 3*1*3*365
verbrauch_herd = 4*2*2*52 
verbrauch_router= 2*4*365 
verbrauch_heizung= 8*20*170

gesamtverbrauch = verbrauch_tv + verbrauch_herd + verbrauch_router + verbrauch_heizung

stromkosten=strompreis * gesamtverbrauch
print(f"Die gesamten Kosten für den Stromverbrauch betragen: {stromkosten:.2f} Euro") #empfehlung
print(10/2)
print("Das Ergebnis lautet:", stromkosten)
print(f"ich kann auch direkt in den f-string reinrechnen: {strompreis * gesamtverbrauch} Euro")
print("Das Ergebnis lautet:" + str(stromkosten) + " Euro ")

a="7"
b="5"
print(a+b)  # Verkettung
print(int(a)+int(b))  # Addition nach Umwandlung in Integer
print(float(a)+float(b))  # Addition nach Umwandlung in Float
ergebnis = int(a) + float(b)
print(f"{ergebnis:.2f}")  # Formatierung auf 2 Nachkommastellen