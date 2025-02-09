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
    
class Cercle(Forme):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    
    def aire(self):
        return self.radius**2*3.14
    
rectangle1=Rectangle(5,10)
forme1=Forme()
cercle1=Cercle(5)
print(forme1.aire())
print(rectangle1.aire())
print(cercle1.aire())
