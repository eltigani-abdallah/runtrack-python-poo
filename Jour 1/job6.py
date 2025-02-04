class Animal():
    def __init__(self,age, prenom):
        self.age=0
        self.prenom=""

    def veillir(self):
        self.age+=1
        print(f"l'age de l'animal est {self.age}")
    
    def nommer(self,prenom):
        self.prenom=prenom
        print(f"le nom de l'animal est {self.prenom}")

chien=Animal(5, "baguette")

chien.veillir()

chien.nommer("pipi")