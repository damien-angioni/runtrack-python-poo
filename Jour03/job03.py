class Tache():
    def __init__(self,titre,desc):
        self.__statut="En cours"
        self.__titre=titre
        self.__desc=desc
    def togglestatut(self):
        if(self.__statut=="En cours"):
            self.__statut="Terminé"
            print("vous venez d'accomplir la tache",self.__titre)
        else:
            print("Cette tache est déjà terminé!")
    def etat_de_tache(self):
        return(self.__statut)
    def sortie(self):
        return(self.__titre,self.__desc)

class ListeDeTache():
    def __init__(self):
        self.__taches=[]
    def ajouterTache(self,item):
        self.__taches.append(item)
    def supprimerTache(self,item):
        try:
            self.__taches.remove(item)
        except:
            print("Cet élément ne fait pas partie du programme: Exister.exe")
    def marquerCommeFinie(self,item):
        try:
            self.__taches[self.__taches.index(item)].togglestatut()
        except:
            print("Cet élément ne fait pas partie du programme: Exister.exe")
    def afficherListe(self):
        i=0
        while(i<len(self.__taches)):
            print(self.__taches[i].sortie())
            i+=1
    def filtrerListe(self):
        i=0
        while(i<len(self.__taches)):
            if(self.__taches[i].etat_de_tache=="En cours"):
                print(self.__taches[i].sortie())
            i+=1

sirop=Tache("Fruit","Apprécier les fruits au sirop")
aja=Tache("le masque","Trouver la pirerre d'aja à insérer dans le masque")
supertask=Tache("La quete","accomplir les tâches")
la_liste=ListeDeTache()
la_liste.ajouterTache(sirop)
la_liste.afficherListe()
la_liste.ajouterTache(aja)
la_liste.ajouterTache(supertask)
la_liste.afficherListe()
la_liste.marquerCommeFinie(sirop)
la_liste.afficherListe()
la_liste.filtrerListe()
la_liste.supprimerTache(aja)
la_liste.afficherListe()
la_liste.supprimerTache(sirop)
la_liste.afficherListe()
la_liste.filtrerListe()
