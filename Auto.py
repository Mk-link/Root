#objekt orientierte Programmierung in Python
class Auto:
    def __init__(self, marke, modell, baujahr): #Konstruktor der Klasse Auto
        self.marke = marke                      #Attribute1 der Klasse Auto
        self.modell = modell                    #Attribute2 der Klasse Auto
        self.baujahr = baujahr                  #Attribute3 der Klasse Auto

    def starten(self):
        return f"Der {self.marke} {self.modell} startet."

    def stoppen(self):
        return f"Der {self.marke} {self.modell} stoppt."
    
    def Alter(self):
        return f"Der {self.marke} ist von {self.baujahr}."
    
#Erstellen eines Objekts der Klasse Auto
'''
mein_auto = Auto("Toyota", "Corolla", 2020)
print(mein_auto.starten())
print(mein_auto.stoppen())
dein_auto = Auto("BMW", "X5", 2021)
print(dein_auto.starten())
print(dein_auto.stoppen()) 
Mercedes = Auto("Mercedes", "C-Klasse", 2019)
print(Mercedes.starten())
print(Mercedes.stoppen())
print(Mercedes.Alter())
'''
