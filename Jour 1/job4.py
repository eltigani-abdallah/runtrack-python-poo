import random
class Personne():
    def __init__(self, prenom, nom):
        self.prenom=prenom
        self.nom=nom
    
    def SePresenter(prenom, nom):
        print(f"je suis {prenom} {nom}")

randfirstname=random.choice(["Lucie","Olivier","Amélie","Étienne","Chloé","François","Camille","Pierre","Isabelle","Julien"])
randlastname=random.choice(["Dupont","Lefevre","Moreau","Lemoine","Bernard","Martin", "Chevalier","Roux"])

Personne.SePresenter(randfirstname, randlastname)

