class Produit():
    def __init__(self,nom, prixHT, TVA):
        self.TVA=TVA
        self.nom=nom
        self.prixHT=prixHT

    def CalculerPrixTTC(self):
        return self.prixHT*(1+self.TVA/100)
    def afficher(self):
        info=f"nom: {self.nom} prix: {self.prixHT} TVA: {self.TVA}"
        return info
    def modifier_prix(self,prix):
        self.prixHT=prix
    def modifier_nom(self,nom):
        self.nom=nom

thon=Produit("thon",1.10,0.12)

thon.modifier_prix(2)
thon.modifier_nom("banane")
print(thon.CalculerPrixTTC())
print(thon.afficher())