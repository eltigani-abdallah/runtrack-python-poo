class Tache():
    def __init__(self,titre, desc,statut):
        self.titre=titre
        self.desc=desc
        self.statut=statut
class ListeDeTaches():
    def __init__(self):
        self.liste=[]
    def ajouterTache(self,tache):
        self.liste.append(tache)
    def supprimerTache(self,tache):
        self.liste.pop(tache)
    def marquerCommeFinie(self,tache):
        tache.statut="Fini"
    def afficherListe(self):
        afficheStr=""
        for tache in self.liste:
            if tache.statut=="a faire":
                afficheStr+="\n[ ] "+ tache.titre+": "+tache.desc+" | "+"statut:"+" "+tache.statut
            elif tache.statut=="en cours":
                afficheStr+="\n[C] "+ tache.titre+": "+tache.desc+" | "+"statut:"+" "+tache.statut
            elif tache.statut=="fini":
                afficheStr+="\n[X] "+ tache.titre+": "+tache.desc+" | "+"statut:"+" "+tache.statut
        print(afficheStr)
    def filterListe(self,statut):
        afficheStr=""
        for tache in self.liste:
            if tache.statut==statut:
                if tache.statut=="a faire":
                    afficheStr+="\n[ ] "+ tache.titre+": "+tache.desc+" | "+"statut:"+" "+tache.statut
                elif tache.statut=="en cours":
                    afficheStr+="\n[C] "+ tache.titre+": "+tache.desc+" | "+"statut:"+" "+tache.statut
                elif tache.statut=="fini":
                    afficheStr+="\n[X] "+ tache.titre+": "+tache.desc+" | "+"statut:"+" "+tache.statut
        print(afficheStr)


tache1=Tache("lave les vetements","laver tes vetements","en cours")
tache2=Tache("faire de sport","sors et faire de sport","a faire")
tache3=Tache("faire les devoirs","finir cette job","fini")

liste1=ListeDeTaches()

liste1.ajouterTache(tache1)
liste1.ajouterTache(tache2)
liste1.ajouterTache(tache3)

liste1.afficherListe()