#Einführung in Python
"""
Dies ist ein mehrzeiliger Kommentar
"""
#Dies ist ein einzeiliger Kommentar
#Deklaration
Umschüler=21
"""
int, float, str, bool,sind ähnlich wie in der deutschen Sprache Artikel
"""
'int' #Ganzzahl
float #Gleitkommazahl  
str #Zeichenkette
bool #Wahrheitswert
#Zuweisung
Umschüler=21
#Ausgabe    
print(Umschüler)
#Eingabe   
input("Wie alt bist du?")
#Datentypen überprüfen
type(Umschüler) #int
#Mehrere Variablen in einer Zeile deklarieren und zuweisen
a,b,c=1,2,3
#Mehrere Variablen in einer Zeile ausgeben
print(a,b,c)
#Mehrere Variablen in einer Zeile eingeben
x,y=input("Gib zwei Zahlen ein:").split()
#Datentypen umwandeln
x=int(x)
y=int(y)
z=x+y
print(z)
#Rechenoperationen
# Addition: +
# Subtraktion: -
# Multiplikation: *
# Division: /
# Ganzzahlige Division: //
# Modulo: %
# Exponentiation: **
#Vergleichsoperatoren
# Gleich: ==
# Ungleich: !=
# Größer als: >
# Kleiner als: <
# Größer gleich: >=
# Kleiner gleich: <=
#Logische Operatoren
# Und: and
# Oder: or
# Nicht: not
#If-Bedingungen
if z>10:
    print("z ist größer als 10")
elif z==10:
    print("z ist gleich 10")
else:
    print("z ist kleiner als 10")
#Schleifen
#For-Schleife
for i in range(5): #0,1,2,3,4
    print(i)
#While-Schleife
count=0
while count<5:
    print(count)
    count+=1 #count=count+1
#Funktionen
def addiere(a,b):
    return a+b  #Rückgabewert
ergebnis=addiere(3,4)
print(ergebnis)
#Listen
meine_liste=[1,2,3,4,5]
print(meine_liste)
# Zugriff auf Elemente
print(meine_liste[0]) # 1
# Hinzufügen
meine_liste.append(6)
# Entfernen
meine_liste.remove(3)
meine_liste.pop(0) # Entfernt das erste Element
meine_liste.sort() # Sortieren
