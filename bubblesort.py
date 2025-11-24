feld=[1,3,4,5,6,9]                  #unsortiertes Feld
while True:                         #Äußere Schleife
    getauscht=False                 #Tausch-Flag zurücksetzen
    for i in range(len(feld)-1):    #Innere Schleife
        if feld[i]>feld[i+1]:       #Vergleich benachbarter Elemente 
            temp=feld[i]            #Tausch der Elemente
            feld[i]=feld[i+1]       
            feld[i+1]=temp          
            getauscht=True          #Tausch-Flag setzen
    if not getauscht:               #Abbruchbedingung
        break           
print(feld)                         #Ausgabe des sortierten Feldes

'''
Die drei Zeilen implementieren den klassischen Tausch (swap) zweier benachbarter Elemente in einer Liste.
 Zuerst wird der aktuelle Wert von feld[i] in der temporären Variablen temp gesichert,
damit er beim Überschreiben nicht verloren geht.
Danach wird an der Position i der Wert von feld[i+1] abgelegt 
und schließlich wird der zuvor gesicherte Wert aus temp an die Position i+1 zurückgeschrieben.
Dadurch werden die Inhalte von feld[i] und feld[i+1] vertauscht.

Wichtiges zu beachten: i muss so gewählt sein,
dass sowohl feld[i] als auch feld[i+1] existieren
(also typischerweise 0 <= i < len(feld)-1).
Außerdem sollte die Einrückung konsistent sein —
inkonsistente Einrückung kann in Python zu Syntaxfehlern führen.
In einem Bubblesort‑Kontext werden diese Tauschoperationen innerhalb einer Schleife mehrfach ausgeführt,
wenn zwei benachbarte Elemente in falscher Reihenfolge sind.
'''