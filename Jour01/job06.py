class Animal():
    def __init__(self):#Constructeur
        self.age=0
        self.prenom=0
    def vieillir(self):#Méthode qui incrémente la valeur de age et l'affiche
        self.age +=1
        print("l'âge de l'animal est de",self.age,"ans!")
    def nommer(self,nom):#Méthode qui change la valeur du nom et l'affiche
        self.prenom=nom
        print("l'animal s'appelle",self.prenom)

charlemagne=Animal()
charlemagne.nommer("Charlemagne")
for i in range(10):
    charlemagne.vieillir()