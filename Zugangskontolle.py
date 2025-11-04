
print("Halt, bitte gib erst dein Alter an.")
while True:
    try:
        Alter = int(input("Alter: "))
    except ValueError:
        print("Bitte eine ganze Zahl eingeben.")
        continue
    if Alter < 18:
        print("Kein Zugang")
        break
    else:
        print("Willkommen")
        break

