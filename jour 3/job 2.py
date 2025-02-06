class CompteBancaire():
    def __init__(self,numero,nom,prenom,solde):
        self.__numero=numero
        self.__nom=nom
        self.__prenom=prenom
        self.__solde=solde
        self.__decouvert=False
    def afficher(self):
        print(f"numero de compte: {self.__numero}")
        print(f"nom: {self.__nom}")
        print(f"prenom: {self.__prenom}")
        print(f"solde: {self.__solde}")
    def afficherSolde(self):
        print(f"solde: {self.__solde}")
    def versement(self,montant):
        self.__solde+=montant
        print(f"solde: {self.__solde}")
    def retrait(self,montant):
        try:
            if not self.__decouvert:
                if montant<=self.__solde:
                    self.__solde-=montant
                else:
                    print("impossible de retirer le momnatant demandé")
            else:
                self.__solde-=montant
        except ValueError:
            print(f"{montant} n'est pas valide, veuillez essayer encore")
        print(f"solde restant: {self.__solde}")
    def agios(self):
        if self.__solde<0:
            print(f"vous avez un solde negatif, veuillez payer les agios de 20 s'il vous plaît")
            self.__solde-=20
        print(f"solde: {self.__solde}")
    def virement(self,compte,montant):
        if montant<=self.__solde:
            self.retrait(montant)
            compte.versement(montant)
        print(f"solde: {self.__solde}")


client1=CompteBancaire(1234,"TABLE","chaise",50)
client2=CompteBancaire(5678,"DE-TERRE", "Pomme",-20)

client2.afficherSolde()
#client1.afficher()

client1.afficherSolde()

client1.versement(50)
#client1.retrait(110)
client1.virement(client2,40)

client2.afficherSolde()

