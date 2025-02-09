class Rectangle():
    def __init__(self,longeur,largeur):
        self.__longeur=longeur
        self.__largeur=largeur
    
    def getlongeur(self):
        return self.__longeur
    def setlongeur(self, nlongeur):
        self.__longeur=nlongeur
        return self.__longeur
    def getlargeur(self):
        return self.__largeur
    def setlongeur(self, nlargeur):
        self.__largeur=nlargeur
        return self.__largeur
        
    def perimetre(self):
        result=(self.getlargeur()+self.getlongeur())*2
        return result
    def surface(self):
        result=self.getlargeur()*self.getlongeur()
        return result
    
class Parallelepipede(Rectangle):
    def __init__(self, longeur, largeur,hauteur):
        super().__init__(longeur, largeur)
        self.hauteur=hauteur

    def volume(self):
        result=self.getlongeur()*self.getlargeur()*self.hauteur
        return result
    
rectangle1=Rectangle(5,10)
parallelepipede1=Parallelepipede(5,10,5)

#print(rectangle1.surface())
#print(rectangle1.perimetre())

print(parallelepipede1.perimetre())
print(parallelepipede1.surface())
print(parallelepipede1.volume())
