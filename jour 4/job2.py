class Personne():
    def __init__(self,age=14):
        self.age=age

    def afficherAge(self):
        print(self.age)
    
    def bonjour(self):
        print("Hello.")

    def modifierAge(self,nAge):
        try:
            self.age=int(nAge)
        except ValueError:
            print("age non valide")


class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        print("je vais en cours")
    
    def afficherAge(self):
        print(f"j'ai {self.age} ans ")
    
class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee=matiereEnseignee
    
    def enseigner(self):
        print("le cours va commancer")

enfant1=Personne()

eleve1=Eleve()

eleve1.bonjour()

eleve1.allerEnCours()

eleve1.modifierAge(15)

eleve1.afficherAge()

prof1=Professeur("maths")

prof1.modifierAge(40)

prof1.afficherAge()

prof1.enseigner()