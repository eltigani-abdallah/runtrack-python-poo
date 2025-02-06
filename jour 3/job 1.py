class Ville():
    def __init__(self, nom, popul):
        self.__nom=nom
        self.__popul=popul
    def increment_popul(self):
        self.__popul+=1
        return self.__popul
    def afficher(self):
        return (self.__nom,self.__popul)
ville1=Ville("Paris", 1000000)
ville2=Ville("Marseille",861635)

class Personne():
    def __init__(self,nom,age,ville):
        self.__nom=nom
        self.__age=age
        self.__ville=ville
    def ajouterPopulation(self):
        self.__ville.increment_popul()

print(ville1.afficher())
print(ville2.afficher())

personne1=Personne("Jhon",45,ville1)
personne2=Personne("Myrtelle",4,ville1)
personne3=Personne("Chloé",18,ville2)

personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()

print(ville1.afficher())
print(ville2.afficher())
        


