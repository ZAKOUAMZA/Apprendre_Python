def afficher(annee):
    # global annee
    print("Fin de l'annee ",annee)
    annee += 1
    print("Debut de l'annee ",annee)
#----------------------------------------------------------------
def somme_de_deux_nombre(a,b):
    # return  a + b
    somme = a + b
    print("La somme de {} et de {} est : {}".format(a,b,somme))
#----------------------------------------------------------------
def soustration_de_deux_nombre(a,b):
    # return  a - b
    difference = a - b
    print("La somme de {} et de {} est : {}".format(a,b,difference))
#----------------------------------------------------------------
def multiplication_de_deux_nombre(a,b):
    # return  a * b
    multiplication = a * b
    print("La multiplication de {} et de {} est : {}".format(a,b,multiplication))

#----------------------------------------------------------------
def division_de_deux_nombre(a,b):
    # return  a / b
    division = a / b
    print("La division de {} par {} est : {}".format(a,b,division))

#----------------------------------------------------------------
def modulo_de_deux_nombre(a,b):
    # return  a % b
    modulo = a % b
    print("Le modulo de {} par {} est : {}".format(a,b,modulo))

#----------------------------------------------------------------
def maximum_de_deux_nombre(a,b):
    # maximum = max(a,b)
    if a > b :
        # return a
        max = a
    else :
        # return b
        max = b
    print("Le maximun de {} et {} est : {}".format(a,b,max))
#----------------------------------------------------------------
def minimum_de_deux_nombre(a,b):
    # minimum = min(a,b)
    if a < b :
        # return a
        min = a
    else :
        # return b
        min = b
    print("Le minimum de {} et {} est : {}".format(a,b,min))
#----------------------------------------------------------------
# Principe de recursivité

def ajouter(a):
    a +=1
    print(a)
    if a < 10 :
        ajouter(a)
#----------------------------------------------------------------
# Exercice de fin 

def nombre_voyelle(mots):
    cpt = 0
    l = ["a", "e", "i", "o", "u","y"]
    for el in mots :
        if el in l :
       # if el== 'a' or el== 'e' or el=='i' or el=='o' or el=='u' or el=='y':
            cpt +=1
    print("Le nombre de voyelle dans {} est {}".format(mots,cpt))

afficher(2000)
somme_de_deux_nombre(10,2)
soustration_de_deux_nombre(10,2)
multiplication_de_deux_nombre(10,2)
division_de_deux_nombre(10,2)
modulo_de_deux_nombre(10,2)
maximum_de_deux_nombre(1000,500)
minimum_de_deux_nombre(1000,500)
ajouter(1)
nombre_voyelle("zakouamzay")