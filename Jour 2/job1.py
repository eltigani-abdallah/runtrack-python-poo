class Rectangle():
    def __init__(self, largeur,longeur):
        self.__largeur=largeur
        self.__longeur=longeur
    def get_largeur(self):
        return self.__largeur
    def set_largeur(self,largeur):
        self.__largeur=largeur
    def get_longeur(self):
        return self.__longeur
    def set_longeur(self,longeur):
        self.__longeur=longeur
    def afficher_rectangle(self):
        rectangle=self.__largeur*self.__longeur
        return rectangle

rect=Rectangle(50,61)

print(rect.get_largeur())
rect.set_largeur(5)
print(rect.get_longeur())
rect.set_longeur(10)
print(rect.afficher_rectangle())