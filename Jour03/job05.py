class Personnage():
    def __init__(self,nom,pv,degat):
        self.__nom=nom
        self.__vie=pv
        self.__basepv=pv
        self.__degat=degat
    def touchePV(self,effect):
        self.__vie=self.__vie-effect
    def attaquer(self,cible):
        cible.touchePV(self.__degat)
    def heal(self):
        if((self.__vie+10)>=self.__basepv):
            self.__vie=self
        else:
            self.__vie+=10
    def reset(self):
        self.__vie=self.__basepv

class jeu():
    def __init__(self,player,oponent):
        self.__joueur=player
        self.__target=oponent
    def jeu(self):
        game_over=False
        while(not game_over):
            print()

Main=Personnage("Marth, roi-héros",26,8)
Boss=Personnage("Brigand Boss",18,4)
King=Personnage("Michalis, roi de Macedon",29,6)
Knight=Personnage("Camus, le Chevalier Noir",35,8)
God=Personnage("Medeus, Dieu des ténèbres",99,9)
Menu=False
while(not Menu):
    print("Marth: l'Emblème du Feu et l'Epée de lumière.")
    print("Vous êtes Marth, Marth Lowell, héritier du trône d'Altea. Votre père, le roi fut assassiné par les sbires du dieu noir Medeus, provoquant alors la guerre dans tout le continent")
    print("Les bandits ravagent votre royaume, l'ambitieu Roi de Medon tente de l'envahir, tandis que le chevalier noir revendique votre trône! allez vous vois laisser faire?")
    print("choisissez votre difficulté! [1=normal][2=Difficile][3=Expert][4=Abyssal]")
    difficult=input("Faites votre choix: ")