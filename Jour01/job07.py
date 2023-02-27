class Personnage():
    def __init__(self):#Constructeur
        self.x=0
        self.y=0
    def haut(self):#Méthode qui modifie la valeur de coordonnée pour aller en haut sur pygame
        self.y = self.y-1
    def bas(self):#Méthode qui modifie la valeur de coordonnée pour aller en bas sur pygame
        self.y =+ 1
    def gauche(self):#Méthode qui modifie la valeur de coordonnée pour aller a gauche sur pygame
        self.y = self.x-1
    def droite(self):#Méthode qui modifie la valeur de coordonnée pour aller a droite sur pygame
        self.x =+ 1
    def position(self):#Méthode qui retourne les coordonnées
        return(self.x,self.y)

cloud_strife=Personnage()
oukilé=cloud_strife.position()
print(oukilé)
cloud_strife.haut()
cloud_strife.haut()
cloud_strife.droite()
oukilé_encore=cloud_strife.position()
print(oukilé_encore)