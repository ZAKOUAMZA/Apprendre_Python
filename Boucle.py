from random import randint

# Exemple si on desir afficher 5 clients avec leur numero client

print("Vous être le client numero 1")
print("Vous être le client numero 2")
print("Vous êtes le client numero 3")
print("Vous être le client numero 4")
print("Vous être le client numero 5")

# sauf que si on a 1000 clients ça sera complique de dupliquer cela d'ou l'utiliter des boucles 

# Boucles for  
# Exemple affichons 10 clients avec leurs numeros clients

for numero_clients in range(1,11) :
    print("Vous être le client numero {} ".format(numero_clients))

# NB la methode range defini l'intervalle 

# Boucle for each avec les listes

Listes_chaines = ["zakoumaza52@gamil.com","zakoumaza616@gamil.com","zakoumaza502@gamil.com"]

for Liste_chaine in Listes_chaines :
    print("Email envoyer à {}".format(Liste_chaine))



# Un petit exemple 

Listes_chaines = ["zakoumaza52@gamil.com","zakoumaza616@gamil.com","zakoumaza502@gamil.com"]
non_autriser = ["zakoumaza616@gamil.com"]

for Liste_chaine in Listes_chaines :

    if Liste_chaine in non_autriser :

        print("Email non autoriser "+ Liste_chaine+" envoie impossible !")
        # continue permet de continuer l'affichage sauf l'email en question
        # break permet de ne rien afficher une fois trouver l'email en question il affichera les elements avant
    
    print("Email envoyer à {}".format(Liste_chaine))


# La boucle While  s'exécute tant qu'une codition est vrai 

salary = 1500

while salary < 2000 :
    salary += 100
    print("Votre salaire est de {}".format(salary))
print("Fin du programme")    


         
# Exercice un youtuber qui a 2500 abonné qui souhaite augmenter de 10 % le nombre d'abonnement
# par mois on souhaite estimer le nombre d'abonner qu'il aurra en 2 ans 

abonnement = 2500
mois = 0
pourcentage_d_augmentation = 1+(10/100)

while mois <= 24 :
    abonnement *= pourcentage_d_augmentation
    mois += 1
    print("Votre abonnement est de {}".format(abonnement))


# Exercice un youtuber qui a 2500 abonné qui souhaite diminuer de -20 % le nombre d'abonnement
# par mois on souhaite estimer le nombre d'abonner qu'il aurra en 2 ans 

abonnement = 2500
mois = 0
pourcentage_d_augmentation = 1-(20/100)

while mois <= 24 :
    abonnement *= pourcentage_d_augmentation
    mois += 1
    print("Votre abonnement est de {}".format(abonnement))


# Exercice demander a l'utiliser de choisir un prix et tant que le jeu n'est pas terminé demander 
# lui d'entrer un prix si son choix est egal au prix Vous avez gagné le prix ! sinon si choix < prix Ces moins!
# sinon si choix et > au prix Ces plus!

prix = 50
i=0
nombre = int(input("Choisir un nombre entre 1 et 1000 "))

while i <= nombre :
    choix = int(input("Entrez un prix "))
    if choix == prix :
        print("Vous avez gagné le prix !")
        break
    elif choix < prix :
        print("Ces moins!")
    else:
        print("Ces plus!")

    i += 1    

# deuxieme methode avec le module randint de random
 
prix = randint(1, 1000) 
 
running = True
 
while running:
         
    choix = int(input("Entrer un prix"))
 
    if choix == prix:
     print("Trouvé !")
     running = False
 
    elif choix < prix:
     print("C'est moins")
       
    elif choix > prix:
     print("C'est plus")
 
print("Fin du jeu !")




