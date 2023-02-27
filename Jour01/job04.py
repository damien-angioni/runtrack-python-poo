class Personne():
    def __init__(self,nom,prenom):#Constructeur
        self.nom=nom
        self.prenom=prenom
    def SePresenter(self):#méthode qui affiche les noms et prénoms associés
        print("Nom:",self.nom,"Prénom:",self.prenom)

moi = Personne("Mograine","Frestfeld")
wotlk = Personne("Menethil III","Arthas")
vampr = Personne("Tepes","Vlad")

moi.SePresenter()
wotlk.SePresenter()
vampr.SePresenter()