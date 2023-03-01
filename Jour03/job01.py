class Ville():
    def __init__(self,nom,nbhabitant):
        self.__nom=nom
        self.__nbhabitant=nbhabitant
    def affiche_nom(self):
        return(self.__nom)
    def affiche_nbhabitant(self):
        return(self.__nbhabitant)
    def touche_nom(self,entry):
        self.__nom=entry
    def touche_nbhabitant(self,entry):
        self.__nbhabitant=entry

class Personne():
    def __init__(self,nom,age,city):
        self.__nom=nom
        self.__age=age
        self.__city=city
        self.ajouterPopulation()
    def affiche_nom(self):
        return(self.__nom)
    def affiche_age(self):
        return(self.__age)
    def affiche_habitation(self):
        return(self.__city)
    def touche_nom(self,entry):
        self.__nom=entry
    def touche_age(self,entry):
        self.__age=entry
    def touche_habitation(self,entry):
        self.__city=entry
    def ajouterPopulation(self):
        self.__city.touche_nbhabitant(self.__city.affiche_nbhabitant()+1)
    
Sud=Ville("Marseille",861635)
print("nombre d'habitant a Marseille:",Sud.affiche_nbhabitant())
Nord=Ville("Paris",1000000)
print("nombre d'habitant a Paris:",Nord.affiche_nbhabitant())
Jon=Personne("John",45,Nord)
print("Ajout de la pop: John")
print("nombre d'habitant a Marseille:",Sud.affiche_nbhabitant())
print("nombre d'habitant a Paris:",Nord.affiche_nbhabitant())
Framboise=Personne("Myrtille",4,Nord)
print("Ajout de la pop: Myrtille")
print("nombre d'habitant a Marseille:",Sud.affiche_nbhabitant())
print("nombre d'habitant a Paris:",Nord.affiche_nbhabitant())
Kurore=Personne("Chloé",18,Sud)
print("Ajout de la pop: Chloé")
print("nombre d'habitant a Marseille:",Sud.affiche_nbhabitant())
print("nombre d'habitant a Paris:",Nord.affiche_nbhabitant())