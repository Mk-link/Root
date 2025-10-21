import random

def roll_d20():
    wurf = random.randint(1, 20)

    if wurf == 1:
        return wurf, "❌ Kritischer Fehlschlag!"
    elif wurf == 20:
        return wurf, "✨ Kritischer Treffer!"
    else:
        return wurf, "Normaler Wurf."

def main():
    print("DnD W20 Würfelroller – 'exit' zum Beenden\n")
    while True:
        eingabe = input("W20 würfeln? (j/n): ").strip().lower()
        if eingabe in ("n", "exit", "q", "quit"):
            print("Auf Wiedersehen!")
            break
        if eingabe == "j" or eingabe == "":
            wurf, text = roll_d20()
            print(f"🎲 Du hast {wurf} gewürfelt → {text}\n")
        else:
            print("Bitte 'j' oder 'n' eingeben.\n")

if __name__ == "__main__":
    main()
