class Livre():
    def __init__(self,titre,auteur,nbpage):
        self.__titre=titre
        self.__auteur=auteur
        self.__disponible=True
        if (type(nbpage) == int):
            self.__nbpage=nbpage
        else:
            print("Erreur | le nombre de page doit être un entier!")
    def changetire(self,titre):
        self.__titre=titre
    def changeauteur(self,auteur):
        self.__auteur=auteur
    def changenbpage(self,nbpage):
        self.__nbpage=nbpage
    def afftitre(self):
        return(self.__titre)
    def affauteur(self):
        return(self.__auteur)
    def affnbpage(self):
        return(self.__nbpage)
    def verification(self):
        if self.__disponible==True:
            return("Le livre est disponible")
        else:
            return("Le livre n'est pas en notre possession")
    def emprunter(self):
        if self.__disponible==True:
            self.__disponible=False
            return("Merci pour l'emprunt!")
        else:
            return("Le livre est déjà emprunté")
    def rendre(self):
        if self.__disponible==False:
            self.__disponible=True
            return("Le livre est bien rendu!")
        else:
            return("Nous avons déjà ce livre dans nos inventaires")

true_best_seller=Livre("Arthas l'ascension du roi-liche","Christie Golden",360)
print(true_best_seller.verification())
print(true_best_seller.rendre())
print(true_best_seller.emprunter())
print(true_best_seller.verification())
print(true_best_seller.emprunter())
print(true_best_seller.rendre())