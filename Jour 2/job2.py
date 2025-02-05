class Livre():
    def __init__(self,titre,auteur,pages):
        self.__titre=titre
        self.__auteur=auteur
        self.__pages=pages
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

livre1=Livre("comment respirer pour les nuls","Aire RESPIRE", "1")

print(livre1.get_titre())
print(livre1.get_auteur())
print("pages: ",livre1.get_pages())

livre1.set_titre("je sais respirer")
livre1.set_auteur("Méchant ASPHYXIE")
livre1.set_pages(2)

print(livre1.get_titre())
print(livre1.get_auteur())
print("pages: ",livre1.get_pages())



    