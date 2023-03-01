class Joueur():
    def __init__(self,nom,numéro,position):
        self.__nom=nom
        self.__numéro=numéro
        self.__position=position
        self.__nb_but=0
        self.__passes=0
        self.__carton_jaune=0
        self.__carton_rouge=0
    def marquerUnBut(self):
        self.__nb_but+=1
    def effectuerUnePasseDecisive(self):
        self.__passes+=1
    def recevoirUnCartonJaune(self):
        self.__carton_jaune+=1
    def recevoirUnCartonRouge(self):
        self.__carton_rouge+=1
    def afficherStatistiques(self):
        print("--------------------")
        print("Joueur:",self.__nom)
        print("Numéro:",self.__numéro)
        print("Position:",self.__position)
        print("But marqués:",self.__nb_but)
        print("Passes décisives:",self.__passes)
        print("Cartons jaunes reçus:",self.__carton_jaune)
        print("Cartons rouges reçus:",self.__carton_rouge)
        print("--------------------")
    def changement_general(self,position,nb_but,passes,carton_jaunes,cartons_rouges):
        self.__position=position
        self.__nb_but=+nb_but
        self.__passes=+passes
        self.__carton_jaune=+carton_jaunes
        self.__carton_rouge=+cartons_rouges

class Equipe():
    def __init__(self,nom):
        self.__nom=nom
        self.__liste_joueurs=[]
    def ajouterJoueur(self,joueur):
        self.__liste_joueurs.append(joueur)
    def AfficherStatistiqueJoueurs(self):
        print("--------------------")
        print("Joueurs de l'équipe des",self.__nom)
        i=0
        while(i<len(self.__liste_joueurs)):
            self.__liste_joueurs[i].afficherStatistiques()
            i+=1
    def mettreAJourStatistiquesJoueur(self,joueur,position,nb_but,passes,carton_jaunes,cartons_rouges):
        try:
            self.__liste_joueurs[self.__liste_joueurs.index(joueur)].changement_general(position,nb_but,passes,carton_jaunes,cartons_rouges)
        except:
            print("Ce joueur n'existe pas!")

#---|création des équipes|---#
Luca_Goers=Equipe("Luca Goers")
Besaid_Aurochs=Equipe("Besaid Aurochs")
Ronso_Fangs=Equipe("Ronso Fangs")
Guado_Glories=Equipe("Guado Glories")
Al_Bhed_Psyches=Equipe("Al Bhed Psyches")
Kilika_Beasts=Equipe("Kilika Beasts")

#---|création des joueurs|---#
#Luca Goers:
Bickson=Joueur("Bickson",1,"Attaquant")
Ambus=Joueur("Ambus",2,"Attaquant")
Glaab=Joueur("Glaab",3,"Centre")
Dorame=Joueur("Dorame",4,"Défenseur")
Bargerda=Joueur("Bargerda",5,"Défenseur")
Laudia=Joueur("Laudia",6,"Gardien")
#Besaid Aurochs:
Tidus=Joueur("Tidus",1,"Attaquant")
Wakka=Joueur("Wakka",2,"Attaquant")
Frangin=Joueur("Frangin",3,"Centre")
Wedge=Joueur("Wedge",4,"Défenseur")
Biggs=Joueur("Biggs",5,"Défenseur")
Zidane=Joueur("Zidane",6,"Gardien")
#Ronso Fangs:
Basik=Joueur("Basik",1,"Attaquant")
Argey=Joueur("Argey",2,"Attaquant")
Gazna=Joueur("Gazna",3,"Centre")
Noubei=Joueur("Noubei",4,"Défenseur")
Irga=Joueur("Irga",5,"Défenseur")
Zazmi=Joueur("Zazmi",6,"Gardien")
#Guado Glories:
Giera=Joueur("Giera",1,"Attaquant")
Zaji=Joueur("Zaji",2,"Attaquant")
Navara=Joueur("Navara",3,"Centre")
Audey=Joueur("Audey",4,"Défenseur")
Pah=Joueur("Pah",5,"Défenseur")
Noi=Joueur("Noï",6,"Gardien")
#Al Bhed Psyches:
Eygaar=Joueur("Eygaar",1,"Attaquant")
Blappa=Joueur("Blappa",2,"Attaquant")
Berrik=Joueur("Berrik",3,"Centre")
Juhda=Joueur("Juhda",4,"Défenseur")
Lakkam=Joueur("Lakkam",5,"Défenseur")
Loumnik=Joueur("Loumnik",6,"Gardien")
#Kilika Beasts:
Larbeit=Joueur("Larbeit",1,"Attaquant")
Isken=Joueur("Isken",2,"Attaquant")
Vuroja=Joueur("Vuroja",3,"Centre")
Kwarkan=Joueur("Kwarkan",4,"Défenseur")
Dihm=Joueur("Dihm",5,"Défenseur")
Nizarut=Joueur("Nizarut",6,"Gardien")

#---|Remplissage des équipes|---#
#Luca Goers:
Luca_Goers.ajouterJoueur(Bickson)
Luca_Goers.ajouterJoueur(Ambus)
Luca_Goers.ajouterJoueur(Glaab)
Luca_Goers.ajouterJoueur(Dorame)
Luca_Goers.ajouterJoueur(Bargerda)
Luca_Goers.ajouterJoueur(Laudia)
#Besaid Aurochs:
Besaid_Aurochs.ajouterJoueur(Tidus)
Besaid_Aurochs.ajouterJoueur(Wakka)
Besaid_Aurochs.ajouterJoueur(Frangin)
Besaid_Aurochs.ajouterJoueur(Wedge)
Besaid_Aurochs.ajouterJoueur(Biggs)
Besaid_Aurochs.ajouterJoueur(Zidane)
#Ronso Fangs:
Ronso_Fangs.ajouterJoueur(Basik)
Ronso_Fangs.ajouterJoueur(Argey)
Ronso_Fangs.ajouterJoueur(Gazna)
Ronso_Fangs.ajouterJoueur(Noubei)
Ronso_Fangs.ajouterJoueur(Irga)
Ronso_Fangs.ajouterJoueur(Zazmi)
#Guado Glories:
Guado_Glories.ajouterJoueur(Giera)
Guado_Glories.ajouterJoueur(Zaji)
Guado_Glories.ajouterJoueur(Navara)
Guado_Glories.ajouterJoueur(Audey)
Guado_Glories.ajouterJoueur(Pah)
Guado_Glories.ajouterJoueur(Noi)
#Al Bhed Psyches:
Al_Bhed_Psyches.ajouterJoueur(Eygaar)
Al_Bhed_Psyches.ajouterJoueur(Blappa)
Al_Bhed_Psyches.ajouterJoueur(Berrik)
Al_Bhed_Psyches.ajouterJoueur(Juhda)
Al_Bhed_Psyches.ajouterJoueur(Lakkam)
Al_Bhed_Psyches.ajouterJoueur(Loumnik)
#Kilika Beasts:
Kilika_Beasts.ajouterJoueur(Larbeit)
Kilika_Beasts.ajouterJoueur(Isken)
Kilika_Beasts.ajouterJoueur(Vuroja)
Kilika_Beasts.ajouterJoueur(Kwarkan)
Kilika_Beasts.ajouterJoueur(Dihm)
Kilika_Beasts.ajouterJoueur(Nizarut)

#---|Début du tournois|---#
Luca_Goers.AfficherStatistiqueJoueurs()
Besaid_Aurochs.AfficherStatistiqueJoueurs()
Ronso_Fangs.AfficherStatistiqueJoueurs()
Guado_Glories.AfficherStatistiqueJoueurs()
Al_Bhed_Psyches.AfficherStatistiqueJoueurs()
Kilika_Beasts.AfficherStatistiqueJoueurs()

Tidus.marquerUnBut()
Wakka.marquerUnBut()
Wakka.effectuerUnePasseDecisive()
Tidus.marquerUnBut()
Wakka.recevoirUnCartonJaune()
Bickson.recevoirUnCartonRouge()
print("Fin de la première mi-temps:")
Luca_Goers.AfficherStatistiqueJoueurs()
Besaid_Aurochs.AfficherStatistiqueJoueurs()
Besaid_Aurochs.mettreAJourStatistiquesJoueur(Wakka,"Défenseur",0,5,0,0)
Besaid_Aurochs.mettreAJourStatistiquesJoueur(Zidane,"Attaquant",5,0,1,0)
Tidus.marquerUnBut()
Besaid_Aurochs.mettreAJourStatistiquesJoueur(Wedge,"Gardien",0,1,0,0)
print("Fin du match!")
Besaid_Aurochs.AfficherStatistiqueJoueurs()