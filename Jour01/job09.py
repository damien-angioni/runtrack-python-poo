class Produit():
    def __init__(self,nom,prix):#Constructeur
        self.nom=nom
        self.prixHT=prix
        self.TVA=0.2
        self.prixTTC=(self.CalculerPrixTTC())
    def CalculerPrixTTC(self):
        resultat=self.prixHT+(self.prixHT*self.TVA)
        return(round(resultat,2))
    def afficher(self):
        return(self.nom,self.prixHT,self.prixTTC)
    def editprix(self,prix):
        self.prixHT=prix
    def editnom(self,nom):
        self.nom=nom
    def afficheprix(self):
        return(self.prixHT)
    def affichenom(self):
        return(self.nom)

item1=Produit("Sujama",85)
item2=Produit("Flin",56)
print(item1.afficher())
print(item2.afficher())

item1.editnom("Skouma")
item1.editprix(168)
print(item1.affichenom())
print(item1.afficheprix())
print(item1.CalculerPrixTTC())
item2.editnom("Sucrelune")
item2.editprix(76)
print(item2.affichenom())
print(item2.afficheprix())
print(item2.CalculerPrixTTC())