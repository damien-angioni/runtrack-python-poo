class Student():
    def __init__(self,nom,prenom,id):
        self.__nom=nom
        self.__prenom=prenom
        self.__id=id
        self.__credit=0
    def add_credits(self,credit):
        if (credit>0):
            self.__credit=self.__credit+credit
            return("points crédités")
        else:
            return("Vous ne pouvez pas créditer une valeur nulle ou négative")
    def studentEval(self):
        if (self.__credit<60) and (self.__credit>=0):
            self.__level="Insufisant"
        elif (self.__credit<70) and (self.__credit>=60):
            self.__level="Passable"
        elif (self.__credit<80) and (self.__credit>=70):
            self.__level="Bien"
        elif (self.__credit<90) and (self.__credit>=80):
            self.__level="Très bien"
        elif (self.__credit>=90):
            self.__level="Exelent"
    def studentInfo(self):
        self.studentEval()
        print("Nom:",self.__nom)
        print("Prénom:",self.__prenom)
        print("ID:",self.__id)
        print("Niveau:",self.__level)
pelo=Student("John","Doe",145)
pelo.studentInfo()
pelo.add_credits(14)
pelo.add_credits(37)
pelo.add_credits(24)
pelo.studentInfo()