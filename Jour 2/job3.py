class Livre():
    def __init__(self,titre,auteur,pages, disponible=True):
        self.__titre=titre
        self.__auteur=auteur
        self.__pages=pages
        self.__disponible = disponible
    def get_titre(self):
        return self.__titre
    def set_titre(self,titre):
        self.__titre=titre
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self,auteur):
        self.__auteur=auteur
    def get_pages(self):
        return self.__pages
    def set_pages(self,pages):
        if pages>0:
            self.__pages=int(pages)
        else:
            print("numéro de pages invalide")
    def set_disponible(self,disponibilité):
        self.__disponible=disponibilité
    def verification(self):
        return self.__disponible
    def emprunter(self):
        if self.verification():
            self.set_disponible(False)
            print(f"vous avez pris {self.__titre}")
        else:
            print("livre indisponible")
    def rendre(self):
        if not self.verification():
            self.set_disponible(True)
            print("vous avez rendu le livre. merci")
        else:
            print("le livre est déjà sur nos étagéres")


livre1=Livre("comment respirer pour les nuls","Aire RESPIRE", "1")


livre1.emprunter()

livre1.emprunter()

livre1.rendre()

livre1.rendre()


