print("Bitte gib einen Text ein:")
eingabe = input()

"""
f-Strings (formatted string literals) fügen ein f vor die Anführungszeichen;
 Ausdrücke in geschweiften Klammern {} werden ausgewertet und ins Ergebnis eingefügt.
"""
print(f"Du hast folgendes eingegeben: {eingabe}")

"""
int() wandelt Werte in ganze Zahlen (int) um.
print(int())             # 0
print(int(3.9))          # 3
print(int(-3.9))         # -3
print(int(True))         # 1
print(int("  42\n"))     # 42
print(int("FF", 16))     # 255
"""
eingabe2 = int(input("diese Zahl wird addiert: "))
eingabe3 = int(input("diese Zahl wird mit der vorigen addiert: "))

print(f"Die Summe der beiden Zahlen ist: {eingabe2 + eingabe3}")
