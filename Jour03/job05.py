class Personnage():
    def __init__(self,nom,pv,degat):
        self.__nom=nom
        self.__vie=pv
        self.__basepv=pv
        self.__degat=degat
    def affiche_stats(self):
        print("-----")
        print(self.__nom)
        print("pv:",self.__vie,"/",self.__basepv)
        print("-----")
    def viewname(self):
        return(self.__nom)
    def viewdamage(self):
        return(self.__degat)
    def PVcontrol(self):
        return(self.__vie)
    def touchePV(self,effect):
        self.__vie=self.__vie-effect
    def attaquer(self,cible):
        cible.touchePV(self.__degat)
    def heal(self):
        if((self.__vie+10)>=self.__basepv):
            self.__vie=self.__basepv
            print("vous êtes totalement guéris")
        else:
            self.__vie+=10
            print("Vous vous soignez de 10 pv")
    def reset(self):
        self.__vie=self.__basepv

class jeu():
    def __init__(self,player):
        self.__joueur=player
        self.__target=()
    def difficult(self,oponent):
        self.__target=oponent
    def gameloop(self):
        game_over=False
        while(game_over==False):
            self.__joueur.affiche_stats()
            self.__target.affiche_stats()
            print("[1=Attaquer][2=Soigner 10 PV][3=Capituler]")
            choix=input("Que faites vous? ")
            if(choix=="1"):
                print("Vous attaquez",self.__target.viewname(),"et infligez", self.__joueur.viewdamage())
                self.__joueur.attaquer(self.__target)
                print(self.__target.viewname(),"Vous attaque et inflige", self.__target.viewdamage())
                self.__target.attaquer(self.__joueur)
            elif(choix=="2"):
                print("Vous vous soignez grâce à la puissance de Falchion")
                self.__joueur.heal()
                print(self.__target.viewname(),"Vous attaque et inflige", self.__target.viewdamage())
                self.__target.attaquer(self.__joueur)
            elif(choix=="3"):
                game_over=True
            else:
                print("Cette option n'est pas disponible")
            if(self.__joueur.PVcontrol()<=0)or(self.__target.PVcontrol()<=0):
                game_over=True

        if(self.__target.PVcontrol()>0):
            print("Marth: Peut-être que je ne suis pas fait pour l'aventure au final...")
            print("Vous avez perdu!")
        else:
            print("Marth: J'ai gagné, et je gagnerai encore!")
            print("Félicitations, vous avez vaincu",self.__target.viewname())
        self.__joueur.reset()
        self.__target.reset()
        print("-----")
        print("-----")


Main=Personnage("Marth, roi-héros",26,8)
Boss=Personnage("Brigand Boss",25,4)
King=Personnage("Michalis, roi de Macedon",42,6)
Knight=Personnage("Camus, le Chevalier Noir",54,8)
God=Personnage("Medeus, Dieu des ténèbres",99,9)
Game=jeu(Main)
Menu=True
while(Menu==True):
    print("Marth: l'Emblème du Feu et l'Epée de lumière.")
    print("Vous êtes Marth, Marth Lowell, héritier du trône d'Altea. Votre père, le roi fut assassiné par les sbires du dieu noir Medeus, provoquant alors la guerre dans tout le continent")
    print("Les bandits ravagent votre royaume, l'ambitieu Roi de Medon tente de l'envahir, tandis que le chevalier noir revendique votre trône! allez vous vous laisser faire?")
    print("grace à Falchion, l'épée de lumière, un artefact divin capable de soigner son porteur, vous allez vaincre vos ennemis et assembler l'emblème du feu!")
    print("choisissez votre difficulté! [1=normal][2=Difficile][3=Expert][4=Abyssal][5=Quitter]")
    difficult=input("Faites votre choix: ")
    if (difficult=="1"):
        print("Vous allez affronter le boss des brigands!")
        Game.difficult(Boss)
        Game.gameloop()
    elif (difficult=="2"):
        print("Vous allez affronter le roi Michalis!")
        Game.difficult(King)
        Game.gameloop()
    elif (difficult=="3"):
        print("Vous allez affronter le chevalier noir!")
        Game.difficult(Knight)
        Game.gameloop()
    elif (difficult=="4"):
        print("Vous allez affronter le dieu obscur!")
        Game.difficult(God)
        Game.gameloop()
    elif (difficult=="5"):
        Menu=False
    else:
        print("Cette option n'est pas disponible")
