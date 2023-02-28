class Voiture():
    def __init__(self,marque,modele,année,kilometrage):
        self.__en_marche=False
        self.__reservoir=50
        self.__marque=marque
        self.__modele=modele
        self.__année=année
        self.__kilometrage=kilometrage
    def affmarche(self):
        return(self.__en_marche)
    def affmarque(self):
        return(self.__marque)
    def affmodele(self):
        return(self.__modele)
    def affannée(self):
        return(self.__année)
    def affkilometrage(self):
        return(self.__kilometrage)
    def setmarque(self,modif):
        self.__marque=modif
    def setmodele(self,modif):
        self.__modele=modif
    def setannée(self,modif):
        self.__année=modif
    def setkilometrage(self,modif):
        self.__kilometrage=modif
    def verifier_plein(self):
        return(self.__reservoir)
    def demarrer(self):
        self.verifier_plein
        if (self.__reservoir>5):
            self.__en_marche=True
            return("Vehicule en marche!")
        else:
            return("Carburant trop bas, pensez à faire le plein!")
    def arreter(self):
        if (self.__en_marche==True):
            self.__en_marche=False
            return("Vehicule éteint")
        else:
            return("Le vehicule est déjà à l'arret!")

WP=Voiture("Matra","Murena",1982,60000)
print("Marque",WP.affmarque())
print("Modèle:",WP.affmodele())
print("Etat de Marche:",WP.affmarche())
print(WP.demarrer())
print("Marque",WP.affmarque())
print("Modèle:",WP.affmodele())
print("Etat de Marche:",WP.affmarche())