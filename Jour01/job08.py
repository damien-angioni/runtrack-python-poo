class Cercle():
    def __init__(self,rayon):#Constructeur
        self.rayon=rayon
    def changerRayon(self,valeur):#Méthode pour changer de rayon
        self.rayon=valeur
    def afficherInfos(self):#Méthode pour afficher les infos
        print("le Rayon est:",self.rayon)
        print("La circonference est:",self.circonférence)
        print("L'aire est:",self.aire)
        print("Le diametre est:",self.diametre)
    def circonférence(self):#Méthode qui retourne la circonférence
        return((22/7)*(2*self.rayon))
    def aire(self): #Méthode qui retourne l'aire
        return((self.rayon*self.rayon)*(22/7))
    def diametre(self): #Méthode qui retourne le diametre
        return(self.rayon*2)

circle1= Cercle(4)
circle2= Cercle(7)
circle1.afficherInfos()
print(circle1.circonférence())
print(circle1.aire())
print(circle1.diametre())
circle2.afficherInfos()
print(circle2.circonférence())
print(circle2.aire())
print(circle2.diametre())