from Tiere import Tiere  

list_tiere = []
pinguin=Tiere("Fisch","15",3,"12:00","schwimmen","Jackie","Vogel")
pinguin2=Tiere("Fisch","16",4,"13:00","watscheln","Pablo","Vogel")
tiger=Tiere("Fleisch","5",5,"11:00","schlafen","Shere Khan","Raubkatze")
list_tiere.append(pinguin)
list_tiere.append(tiger)
list_tiere.append(pinguin2)

print("Willkommen im Zoo!")
print("Unsere Tiere heute sind:")
for tier in list_tiere:
    print(tier.name + " ist ein " + tier.tierart + "- " + tier.futter + " im Gehege " + tier.gehege + ", Menge: " + str(tier.menge) + ", Fütterungszeit: " + tier.fuetterungszeit + ", Aktion: " + tier.aktion
          )