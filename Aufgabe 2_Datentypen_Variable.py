#Aufgabe1:
Fred=("Fred", 30, 1.82)
George=("George", 30, 1.82)
Ron=("Ron", 27, 1.78)

print(Fred)
print(George) 
print(Ron)

#Aufgabe2:
Länge=12
Breite=8
Fläche= Länge * Breite
Ergebnis=("Die Fläche des Rechtecks beträgt:", Fläche, "Quadratmeter")
print(Ergebnis)

#Aufgabe3:
Alter_Harry= int(26)
print("Harry ist", Alter_Harry, "Jahre alt.")
Raumtemperatur= 20.5
print("Die Raumtemperatur beträgt", Raumtemperatur, "Grad Celsius.")
Name_Harrys_Eule= "Hedwig"
print("Harrys Eule heißt", Name_Harrys_Eule)
Ist_es_regnerisch= False
if Ist_es_regnerisch:
    print("Ja, es regnet.")
else:
    print("Nein, es regnet nicht.")

#Aufgabe4:
Zahl1= int(15)
Zahl2= int(27)
Summe= Zahl1 + Zahl2
Fläche_Kreis= 3.14 * (Summe ** 2)
print("Die Fläche des Kreises mit dem Radius", Summe,"m beträgt:", Fläche_Kreis ,"m²")

#Aufgabe5:
print("Wie heißt du nochmal?")
input1= input()
print("Du warst wie alt?")
input2= input()
print("Was isst du am liebsten?")
input3= input()


I_know_U=(Name, Alter, Lieblingsessen)=(input1, input2, input3)
print("Klar", I_know_U[0],",wusste doch das du ", I_know_U[1], "bist und gerne", I_know_U[2], "isst.")

