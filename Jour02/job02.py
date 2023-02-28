class Livre():
    def __init__(self,titre,auteur,nbpage):
        self.__titre=titre
        self.__auteur=auteur
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

best_seller= Livre("Ascension de la Horde","Christie Golden","beaucoup")
best_seller= Livre("Ascension de la Horde","Christie Golden",318)
print(best_seller.afftitre())
print(best_seller.affauteur())
print(best_seller.affnbpage())
best_seller.changetire("L'Heure des ténèbres")
best_seller.changeauteur("Aaron Rosenberg")
best_seller.changenbpage(308)
print(best_seller.afftitre())
print(best_seller.affauteur())
print(best_seller.affnbpage())