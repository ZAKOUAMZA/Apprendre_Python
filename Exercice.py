# Écrivez une fonction qui prend un nombre en entrée et renvoie le carré de ce nombre.

def carré(x):
    return x*x

# Écrivez une fonction qui prend deux nombres en entrée et renvoie leur somme.

def somme(x,y):
    return x + y

# Écrivez une fonction qui prend deux nombres en entrée et renvoie leur produit.   

def produit(x,y):
    return x * y

# Écrivez une fonction qui prend un nombre en entrée et renvoie sa factorielle. 
# La factorielle de n (notée n!) est le produit de tous les entiers de 1 à n.

def factorielle(x):
    if x == 0 :
        return 1
    else:    
        return x * factorielle(x-1)


# Écrivez une fonction qui prend un nombre en entrée et renvoie vrai (True) 
# s'il s'agit d'un nombre premier, sinon faux (False).

def nombre_premier(x):
    if x <= 1 :
        print('Impossible car le nombre est inférieur à 1')
    else :
        for i in range(2,x):
            if x%i ==0 :
                return  False
            
        return True
################################################################

def nombre_premier(nombre) :
    if nombre <= 1 :
        print('Impossible car le nombre est inférieur à 1')
    else :
        for i in range(2,nombre):
            if nombre % i == 0 :
                return  False
            
        return True
for i in range(2,100) :
    if(nombre_premier(i)):
        print(i)        
# Écrivez une fonction qui prend une chaîne de caractères en 
# entrée et renvoie vrai si la chaîne est un palindrome, sinon faux. 
# Un palindrome est une séquence de caractères qui se lit de la même 
# manière de gauche à droite et de droite à gauche.

def palindrome(mots):
    if mots == mots[::-1] :
        return True
    else :
        return False


def palindrome(mots):
    chaine = mots.lower()
    ch = ' '
    for el in chaine :
        if el != " ":
            ch += el
    chaine_debut = ch
    chaine_inverse = ch[::-1]
    if chaine_debut == chaine_inverse :
        return True
    else:
        return False    


# Écrivez une fonction qui convertit une température donnée de Celsius à 
# Fahrenheit (ou vice versa). La formule de conversion de Celsius à Fahrenheit 
# est : F = 9/5 C +32.

def convertit_temperature( ):
    choix = input("Entrez votre choix (C pour Celsius et F pour Fahrenheit)").upper()
    if choix == 'C' :
        cel = int(input("Entrez en Celsius"))   
        F = (9/5)* (cel) + 32
        print ("La temperature en  Fahrenheit est {}".format(F))

    if choix == 'F' :
        fah = int(input("Entrez en Fahrenheit"))
        C = (( fah-32) * (5)) /9
        print ("La temperature en Celsius est {}".format(C))


# Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une 
# nouvelle liste contenant les mêmes nombres triés par ordre croissant.


def trier_liste_bulle(Liste):
    taille = len(Liste)
    for i in range (taille) :
        for j in range(taille-i-1) :
            if Liste[j]>Liste[j+1] :
                Liste[j],Liste[j+1] = Liste[j+1],Liste[j]
    return Liste

# Écrivez une fonction de recherche binaire qui prend une liste triée et un élément cible, 
# et renvoie l'index de l'élément cible s'il est présent, sinon -1.

def recherche_binaire(liste,el) :
    debut = 0
    fin = len (liste)-1
    while deut <= fin :
        milieu = (debut + fin )//2
        valeur_milieu = liste [milieu]
        if valeur_milieu == el :
            return milieu
        elif valeur_milieu < el :
            debut = milieu + 1
        else :
            fin = milieu -1
    return -1    







# Écrivez une fonction qui prend deux nombres en entrée ,a et b, et renvoie a élevé à la puissance b.


