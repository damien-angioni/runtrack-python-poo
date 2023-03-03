class Rectangle():
    def __init__(self):
        self.__longueur=5
        self.__largeur=10
    def afficheLongueur(self):
        print("Longueur:",self.__longueur)
    def afficheLargeur(self):
        print("Largeur:",self.__largeur)
    def toucheLongueur(self,valeur):
        self.__longueur=valeur
    def toucheLargeur(self,valeur):
        self.__largeur=valeur
    def périmètre(self):
        print("Périmètre:",(2*self.__longueur)+(2*self.__largeur))
    def surface(self):
        print("Surface:",self.__longueur*self.__largeur)
    def returnlongueur(self):
        return(self.__longueur)
    def returnlargeur(self):
        return(self.__largeur)
class Parallélépipède(Rectangle):
    def __init__(self,hauteur):
        super().__init__()
        self.__hauteur=hauteur
    def afficheHauteur(self):
        print("Hauteur:",self.__hauteur)
    def toucheHauteur(self,valeur):
        self.__hauteur=valeur
    def volume(self):
        print("Volume:",self.returnlongueur*self.returnlargeur*self.__hauteur)

figure=Rectangle()
figure.afficheLongueur()
figure.afficheLargeur()
figure.toucheLongueur(4)
figure.toucheLargeur(8)
figure.afficheLongueur()
figure.afficheLargeur()
figure.périmètre()
figure.surface()
boite=Parallélépipède(3)
boite.volume()
boite.afficheHauteur()
boite.toucheHauteur(6)
boite.afficheHauteur()