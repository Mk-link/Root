""""
split trennt einen String an einem Trennzeichen und liefert eine Liste der Teilstrings zurück.

Kurz:

Rückgabe: list von str
Default (kein Argument): trennt an beliebigen Whitespace und entfernt leere Teile
Mit sep: trennt genau an diesem Separator (z. B. ",")
Optional maxsplit: maximal so viele Trennungen
"""

studenten= "Jörg,Patrick,Holger,Christopher"
print(studenten.split(","))

print(type(studenten.split(",")))  # <class 'list'>

s = "Jörg,Patrick,Holger,Christopher"

print(s.split(","))       
 # ['Jörg', 'Patrick', 'Holger', 'Christopher']

s2 = "ein  zwei\tdrei\nvier"
print(s2.split())          
# ['ein', 'zwei', 'drei', 'vier'] (Whitespace wird zusammengefasst)

print(s.split(",", 2))     
# ['Jörg', 'Patrick', 'Holger,Christopher'] (höchstens 2 Splits)

print("keine-komma".split(","))  
# ['keine-komma'] (wenn Separator nicht vorkommt,
# komplette Zeichenkette als einziges Element)