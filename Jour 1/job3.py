class Operation():
    def __init__(self, nombre1=1, nombre2=2):
        self.nombre1= nombre1
        self.nombre2= nombre2


    def addition(nombre1,nombre2):
        resultat= nombre1+ nombre2
        print(f"Le resultat est: {resultat}")

Operation.addition(1,2)