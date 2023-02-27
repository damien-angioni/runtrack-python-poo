class Operation():
    def __init__(self, nombre1, nombre2):#Constructeur
        self.nombre1=nombre1
        self.nombre2=nombre2
    def addition(self):#méthode qui additionne les valeurs
        print(self.nombre1+self.nombre2)

objet_job1=Operation(13,14)
print(objet_job1)
#Job 2
print(objet_job1.nombre1)
print(objet_job1.nombre2)
#job3
objet_job1.addition()