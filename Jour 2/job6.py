class Commande():
    def __init__(self,numero,liste,statut,prix,TVA=0):
        self.__numero=numero
        self.__liste=list(liste)
        self.__statut=statut
        self.__prix=prix
        self.__TVA=TVA
        self.__prix_final=self.__calculer()
    def ajout_plat(self,plat):
        self.__liste.append(plat)
    def annuler(self,plat):
        self.__liste.pop(plat)
    def __calculer(self):
        return self.__prix*(1+self.__TVA/100)
    def afficher_commande(self):
        print(f"liste des commandes: {self.__liste}")
        print(f"numero de commande: {self.__numero}")
        print(f"statut de commande: {self.__statut}")
        print(f"prix de commande: {self.__prix}")
        print(f"TVA de commande: {self.__TVA}")
        print(f"prix final: {self.__prix_final}")

menu_dict={
    "poisson":5,
    "kebab":10,
    "poulet":7,
}
reverse_dict={value:key for key,value in menu_dict.items()}

commande1=Commande(1,[reverse_dict[10]], "en cours",menu_dict["kebab"] ,0.15)

commande1.afficher_commande()


