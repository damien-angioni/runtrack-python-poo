class CompteBancaire():
    def __init__(self,id,nom,prenom,solde):
        self.__id=id
        self.__nom=nom
        self.__prenom=prenom
        self.__solde=solde
        self.__decouvert= False
        self.__interet=0
    def toggle_decouvert(self):
        if(self.__decouvert == True):
            self.__decouvert = False
        else:
            self.__decouvert = True
    def afficher(self):
        print("Numéro de compte:",self.__id)
        print("Nom:",self.__nom)
        print("Prénom:",self.__prenom)
        print("Votre solde:",round(self.__solde,2))
        self.agios()
    def afficherSolde(self):
        print("Votre solde:",round(self.__solde),2)
        self.agios()
    def versement(self,valeur):
        self.__solde=round((valeur+self.__solde),2)
        self.agios()
    def retrait(self,valeur):
        if (self.__decouvert==True):
            self.__solde=self.__solde-valeur
        elif (self.__solde<valeur):
            print("Opération impossible, solde insuffisant")
        else:
            self.__solde=self.__solde-valeur
        self.agios()
    def virement(self,valeur,cible):
        if (self.__decouvert==True):
            self.__solde=self.__solde-valeur
            cible.versement(valeur)
            print("Opération réussi, virement de:",valeur,"à la personne")
        elif (self.__solde<valeur):
            print("Opération impossible, solde insuffisant")
        else:
            self.__solde=self.__solde-valeur
            cible.versement(valeur)
            print("Opération réussi, virement de:",valeur,"à la personne")
        self.agios()
    def agios(self):
        if(self.__solde<0):
            somme=self.__solde*(-0.08)
            if(somme>self.__interet):
                self.__interet=somme
                print("vous devez des intérets de:",self.__interet)
            else:
                print("vous devez des intérets de:",self.__interet)
        if(self.__interet<self.__solde)and(self.__interet>0):
            self.__solde=self.__solde-self.__interet
            self.__interet=0
            print("vos intérets sont de 0")

pelo1=CompteBancaire(145789,"Jean","Jacques",742)
pelo1.afficher()
pelo1.retrait(865)
pelo1.afficherSolde()
pelo1.toggle_decouvert()
pelo1.retrait(865)
pelo1.afficherSolde()
pelo1.versement(2845)
pelo1.afficherSolde()
pelo2=CompteBancaire(358914,"Jean","Claude",5)
pelo2.toggle_decouvert()
pelo2.afficher()
pelo2.retrait(85)
pelo2.afficher()
pelo1.virement(165,pelo2)
pelo2.afficher()