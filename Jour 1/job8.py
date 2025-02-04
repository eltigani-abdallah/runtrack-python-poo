class Cercle():
    def __init__(self,rayon):
        self.rayon=rayon

    def changerRayon(self,rayon):
        self.rayon=rayon
    
    def circonférence(self):
        circonférencee=2*3.14*self.rayon
        return circonférencee
    def aire(self):
        airee=3.14*self.rayon**2
        return airee 
    def diametre(self):
        diametree=2*self.rayon
        return diametree
    def afficherInfo(self):
        print(f"rayon: {self.rayon} circonférence: {self.circonférence()} aire: {self.aire()} diametre: {self.diametre()}")
circle4=Cercle(4)
circle7=Cercle(7)

circle4.afficherInfo()
circle7.afficherInfo()