class Vehicule():
    def __init__(self,marque,modele,an,prix):
        self.marque=marque
        self.modele=modele
        self.an=an
        self.prix=prix
    def informationsVehicule(self):
        print(f"marque: {self.marque}")
        print(f"modele: {self.modele}")
        print(f"an: {self.an}")
        print(f"prix: {self.prix}")
    
    def demarrer(self):
        print("attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, an, prix):
        super().__init__(marque, modele, an, prix)
        self.portes=4

    def informationsVehicule(self):
        print(f"nombre des portes: {self.portes}")
        return super().informationsVehicule()
    def demarrer(self):
        print("la voiture roule")

class Moto(Vehicule):
    def __init__(self, marque, modele, an, prix):
        super().__init__(marque, modele, an, prix)
        self.roue=2

    def informationsVehicule(self):
        print(f"nombre de roue: {self.roue}")
        return super().informationsVehicule()
    def demarrer(self):
        print("le moto roule")


voiture1=Voiture("toyota","camry",2000,2)

voiture1.informationsVehicule()
voiture1.demarrer()


moto1=Moto("yamaha","ghost rider",2003,500)

moto1.informationsVehicule()
moto1.demarrer()
        