class Point():
    def __init__(self,x,y):#Constructeur
        self.x=x
        self.y=y
    def afficherLesPoints(self):#méthode qui affiche les coordonnées
        print("x=",self.x)
        print("y=",self.y)
    def afficherX(self):#méthode qui affiche seulement X
        print("x=",self.x)
    def afficherY(self):#méthode qui affiche seulement Y
        print("y=",self.y)
    def changerX(self,valeur):#Méthode qui change la valeur associé a X
        self.x=valeur
    def changerY(self,valeur):#Méthode qui change la valeur associé a Y
        self.y=valeur

sirius=Point(8.917,58.017)
sirius.afficherLesPoints()
rigel=sirius
rigel.changerX(32.3)
rigel.afficherX()
rigel.changerY(6)
rigel.afficherY()