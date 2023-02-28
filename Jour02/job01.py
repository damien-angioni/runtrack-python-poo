class Rectangle():
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
    def affichage(self):
        return("longueur =",self.longueur,"| largeur =",self.largeur)
    def affichelongueur(self):
        return("longueur =",self.longueur)
    def affichelargeur(self):
        return("largeur =",self.largeur)
    def setlongueur(self,longueur):
        self.longueur=longueur
    def setlargeur(self,largeur):
        self.largeur=largeur

Ecran=Rectangle(720,1080)
print(Ecran.affichage())
Ecran.setlargeur(7680)
Ecran.setlongueur(4320)
print(Ecran.affichelargeur())
print(Ecran.affichelongueur())