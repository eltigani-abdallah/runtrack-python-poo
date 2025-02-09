class Forme():
    def __init__(self):
        pass
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self,longeur,largeur):
        self.longeur=longeur
        self.largeur=largeur
    def aire(self):
        return self.longeur*self.largeur
    
rectangle1=Rectangle(5,10)
forme1=Forme()
print(forme1.aire())
print(rectangle1.aire())    