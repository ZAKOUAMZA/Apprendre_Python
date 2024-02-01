import statistics
from random import shuffle
# Les liste

Liste = ["Zakou","Amza","Dari"]
print(Liste)

# Récuperation du premier element de la liste

print(Liste[0])

# Récuperation du dernier element de la liste

print(Liste[len(Liste)-1])

# Modification du premier element de la liste par Souleymane

Liste[0] = "Souleymane"
print(Liste)

# Ajouter un element a la liste en position i avec la methode insert

Liste.insert(2, "Zalika")
print(Liste)

# Modification de l'element d'indices 2 et 4

Liste[2:4] = ["Ibrahim","Assane"]
print(Liste)

# Ajouter un element a la fin de la liste avec la methode append

Liste.append("Safoura")
print(Liste)

# Ajouter plusieur element a la fin de la liste avec la methode extend

Liste.extend(["Mariam","Nouroundine"])
print(Liste)

# Suppression d'un element de la liste avec la methode del

del Liste[2]
print(Liste)

# Suppression d'un element de la liste avec la methode pop

Liste.pop(3)
print(Liste)

# Suppression d'un element de la liste avec la methode remove en precisant le nom de la personne

Liste.remove("Nouroundine")
print(Liste)

# Methode permetant de vider une liste

Liste.clear()
print(Liste)


# Un petit exercice avec les listes pour calculer la moyenne des 
# elements d'une liste avec le module import statistics

Tables_Liste = [10,20,30,40,50,60]
print(Tables_Liste)

# Melanger les elements de la liste avec le module from random import shuffle

shuffle(Tables_Liste)
print(Tables_Liste)

moyenne_liste = statistics.mean(Tables_Liste)
print("la moyenne est {}".format(moyenne_liste))

# une autre façon de creer une liste en utiliser les donner saisi et la methode split()
Liste2 = input("Entrez une chaine en suivant ce format (email-nom-prenom-telephone)").split("-")
print("Bonjour monsieur {},{} votre email est {} et votre numero de telephone est {}".format(Liste2[1],Liste2[2],Liste2[0],Liste2[3]))

# Exercice demander en console une chaine de la forme "mot1/mot2/mot3/mot4/mot5/.."
# transformer cette chaine en une liste
# la melanger
# si le nombre d'element de cette chaine est inférieur à 10
#  -> afficher les deux premiers mots
# si le nombre d'element de cette chaine est supérieur ou egal à 10 
# -> afficher les 3 derniers nombres 

chaine = input("Entrez une chaine du format suivant ce format (mot1/mot2/mot3/mot4)").split("/")
print(chaine)
shuffle(chaine)
print(chaine)

if len(chaine) < 10 :
    print(chaine[0:2])

else:
    print(chaine[len(chaine)-3:len(chaine)])