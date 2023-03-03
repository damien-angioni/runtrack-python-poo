class Personne():
    def __init__(self):
        self.__age=14
    def afficherAge(self):
        print("âge:",self.__age)
    def bonjour(self):
        print("Hello")
    def modifierAge(self,valeur:int):
        self.__age=valeur
class Eleve(Personne):
    def __init__(self):
        super().__init__()
    def allerEnCour(self):
        print("Je vais en cours")
    def affichageAge(self):
        self.afficherAge()
class Professeur(Personne):
    def __init__(self,matière):
        super().__init__()
        self.__matiereEnseignée=matière
    def enseigner(self):
        print("Le cour va comencer")

jean=Personne()
jean.bonjour()
michel=Eleve()
michel.affichageAge()
michel.allerEnCour()
edouard=Professeur("Physique")
edouard.bonjour()
edouard.enseigner()