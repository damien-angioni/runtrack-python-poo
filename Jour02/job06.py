class Commande():
    def __init__(self,num,contenu):
        self.__num=num
        self.__contenu=contenu
        self.statut="en cours"
    def ajout(self,annx,pr):
        self.__contenu[annx]=(pr)
    def consulte_commande(self):
        return(self.__contenu)
    def affiche_numero(self):
        return(self.__num)
    def facturation(self):
        somme=0
        for i,j in self.__contenu.items():
            somme=somme+j+(j*0.2)
        return(round(somme,2))

repas={"Pain":6,"Sujamma":85,"Patate":8,"Mapo Tofu":35,"Fraise":12}
Bunet=Commande(14,repas)
print(Bunet.consulte_commande())
Bunet.ajout("Chocolat",17)
print(Bunet.consulte_commande())
print(Bunet.facturation())