class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def afficherLesPoints(self):
        print(self.x, self.y)
    def afficherX(self):#
        print(self.x)
    def afficherY(self):#
        print(self.y)
    def changerX(self,x):#
        self.x=x
        print(self.x)
    def changerY(self,y):#
        self.y=y
        print(self.y)

pointy=Point(5,6)


pointy.afficherLesPoints()

pointy.afficherX()

pointy.afficherY()

pointy.changerX(7)

pointy.changerY(8)