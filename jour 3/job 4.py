class Joueur():
    def __init__(self,nom,numero,position,buts,passes,jaunes,rouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passes=passes
        self.jaunes=jaunes
        self.rouges=rouges
    def marquerUnBut(self):
        self.buts+=1

    def effectuerUnePasseDecisive(self):
        self.passes+=1

    def recevoirUnCartonJaune(self):
        self.jaunes+=1
    def recevoirUnCartonRouge(self):
        self.rouges+=1
    def afficherStatistiques(self):
        print(f"nom:{self.nom}  \n numero: {self.numero} \n position: {self.position}\n buts marqués:{self.buts}\n passes effectuées: {self.passes}\n cartons jaunes:{self.jaunes} \n cartons  rouges: {self.rouges}")
class Equipe():
    def __init__(self,nom,listej=None):
        self.nom=nom
        self.listej=list(listej) if listej is not None else []
    def ajouterJoueur(self,joueur):
        if joueur not in self.listej:
            self.listej.append(joueur)
        else:
            print("cette joueur est déjà dans l'equipe")
        return self.listej
    def AfficherStatistiquesJoueurs(self):
        print(f"equipe {self.nom}")
        for joueur in self.listej:
            joueur.afficherStatistiques()
    def mettreAJourStatistiquesJoueur(self,nom_joueur,position=None,buts=None,passes=None,jaunes=None,rouges=None):
        for joueur in self.listej:
            if joueur.nom==nom_joueur:
                if position is not None:
                    joueur.position=position
                if buts is not None:
                    joueur.buts+=buts
                if passes is not None:
                    joueur.passes+=passes
                if jaunes is not None:
                    joueur.jaunes+=jaunes
                if rouges is not None:
                    joueur.rouges+=rouges
        if joueur.nom not in self.listej:
            print("le joueur n'est pas là, essaie un autre equipe")

    
joueur1=Joueur("mamie",2,"attaque",5,2,0,10)
joueur2=Joueur("junior",55,"gardian",90,0,0,0)
joueur3=Joueur("papi",69,"defense",0,0,3,5)
joueur4=Joueur("cheri",2,"attaque",6,50,0,99)

equipe1=Equipe("Lamamie")

equipe2=Equipe("les fleurs")

equipe1.ajouterJoueur(joueur2)

equipe2.ajouterJoueur(joueur3)

equipe1.ajouterJoueur(joueur1)

equipe2.ajouterJoueur(joueur4)

#equipe1.AfficherStatistiquesJoueurs()
#equipe2.AfficherStatistiquesJoueurs()

equipe2.mettreAJourStatistiquesJoueur("papi",rouges=1)


#equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()