class Tiere:
    def __init__(self,futter,gehege,menge,fuetterungszeit,aktion,name,tierart): 
        self.futter = futter                       
        self.gehege = gehege                    
        self.menge = menge 
        self.fuetterungszeit  = fuetterungszeit
        self.aktion = aktion    
        self.name = name       
        self.tierart = tierart

    def arbeit(self):
        print(f"Das Tier frisst {self.futter}.")
