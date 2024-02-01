# Creation d'une class avec trois attribut
class Player :
    nom  = " Amza "
    vie = 100
    points = 3

# Creation d'une instance de la class pour le joueur1

joueur1 = Player()
print("Bienvenue {} votre nombre de vie est {} et votre total de point est {}".format(joueur1.nom,joueur1.vie,joueur1.points))

# ----------------------------------------------------------------

# Creation d'une class Player
class Player :
# creation d'un constructor 
    def __init__(self,nom,vie,points):
        self.nom = nom
        self.vie = vie
        self.points = points
        print("Bienvenue {} votre nombre de vie est {} et votre total de point est {}".format(self.nom,self.vie,self.points))

# Creation de deux instance de la class pour le joueur1 et le joueur2
joueur1 = Player("Amza",100,10)
joueur2 = Player("zakou",200,20)

# ----------------------------------------------------------------

# Creation d'une class Player
class Player :
# creation d'un constructor 
    def __init__(self,nom,vie,points):
        self.nom = nom
        self.vie = vie
        self.points = points

# Creation des methodes (assesseur) get 
    def get_nom(self):
        return self.nom 

    def get_vie(self):
        return self.vie 

    def get_points(self):
        return self.points 

# Creation des methodes (mutateur) seter permet de modifier
    
    def Bonus_points(self,bonus):
        self.points += bonus
        print("Vous avez ajouter ",bonus," sur votre points")

    def set_vie(self,reduction_vie):
        self.vie -= reduction_vie
        print("votre vie est reduite de",reduction_vie)
        


joueur1 = Player("Amza",100,10)
joueur1.Bonus_points(5)
joueur1.set_vie(10)
print("Aie... vous possedez desormais",joueur1.get_points())
print("votre vie est desormais",joueur1.get_vie())