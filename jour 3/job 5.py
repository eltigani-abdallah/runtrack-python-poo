class Personnage():
    def __init__(self,nom,vie=0,force=1):
        self.nom=nom
        self.vie=int(vie)
        self.force=int(force)
    
    def setForce(self,force):
        self.force=force
    def prendDMG(self,DMG):
        self.vie-=DMG
        print(f"{self.nom} a pris {DMG} de DMG")
        print(f"il le reste {self.vie} HP")

    def attaquer(self,ennemi):
        print(f"attaque de {self.force} sur {ennemi.nom}")
        ennemi.prendDMG(self.force)
    
    def soigner(self,soin):
        self.vie+=soin

class Jeu():
    def __init__(self):
        self.niveau=0

    def choisirNiveau(self,niveau=1):
        niveau=input("choisir le niveau de difficulté (1-3 où 1 est le plus facile)")
        self.niveau=int(niveau)

    def lancerJeu(self):
        joueur=Personnage("joueur")
        ennemi=Personnage("monstre")

        match self.niveau:
            case 1:
                joueur.soigner(50)
                joueur.setForce(5)                
                ennemi.soigner(10)
                ennemi.setForce(5)

                ennemi.attaquer(joueur)
                joueur.attaquer(ennemi)
                ennemi.attaquer(joueur)
                joueur.attaquer(ennemi)
            case 2:
                joueur.soigner(60)
                joueur.setForce(10)
                ennemi.soigner(50)
                ennemi.setForce(10)

                ennemi.attaquer(joueur)
                joueur.attaquer(ennemi)
                ennemi.attaquer(joueur)
                joueur.attaquer(ennemi)
                ennemi.attaquer(joueur)
                joueur.attaquer(ennemi)
                ennemi.attaquer(joueur)
                joueur.attaquer(ennemi)
                ennemi.attaquer(joueur)
                joueur.attaquer(ennemi)
                
            case 3:
                joueur.soigner(10)
                joueur.setForce(5)
                ennemi.soigner(50)
                ennemi.setForce(5)

                ennemi.attaquer(joueur)
                joueur.attaquer(ennemi)
                ennemi.attaquer(joueur)
        if joueur.vie<=0:
            print("vous avez perdu")
        elif ennemi.vie<=0:
            print("vous avez gagne!")

jeu1=Jeu()

jeu1.choisirNiveau()

jeu1.lancerJeu()
