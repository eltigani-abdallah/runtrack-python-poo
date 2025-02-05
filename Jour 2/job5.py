class Voiture():
    def __init__(self, marque, modele, année, kilometrage,reservoir=50, en_marche=False):
        self.__marque=marque
        self.__modele=modele
        self.__année=année
        self.__kilometrage=kilometrage
        self.__en_marche=en_marche
        self.__reservoir=reservoir

    def get_marque(self):
        return self.__marque
    def set_marque(self,marque):
        self.__marque=marque

    def get_modele(self):
        return self.__modele
    def set_modele(self,modele):
        self.__modele=modele

    def get_année(self):
        return self.__année
    def set_année(self,année):
        self.__année=année

    def get_kilometrage(self):
        return self.__kilometrage
    def set_kilometrage(self,kilometrage):
        self.__kilometrage=kilometrage

    def get_en_marche(self):
        return self.__en_marche
    def set_en_marche(self,en_marche):
        self.__en_marche=en_marche

    def demarrer(self):
        if not self.get_en_marche():
            if self.__verifier_plein()>=5:
                self.set_en_marche(True)
            else:
                print("pas de gas...")
        else:
            print("déjà demarré")
    def arreter(self):
        if self.get_en_marche:
            self.set_en_marche(False)
        else:
            print("déjà arreté")
    def __verifier_plein(self):
        return self.__reservoir
    def infovoiture(self):
        print(f"marque: {self.__marque}")
        print(f"modele: {self.__modele}")
        print(f"année: {self.__année}")
        print(f"kilometrage: {self.__kilometrage}")
        print(f"reservoir: {self.__reservoir}")
        print(f"en_marche?: {self.__en_marche}")

    
voiture1=Voiture("Toyota","corolla",2017,5)

voiture1.demarrer()
voiture1.infovoiture()
voiture1.arreter()
voiture1.infovoiture()
