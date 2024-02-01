#Exercice 1 : Manipulation de base
# Créez un dictionnaire vide appelé mon_dictionnaire.
# Ajoutez des paires clé-valeur à mon_dictionnaire 
# représentant des informations sur une personne (par exemple, nom, âge, ville).
# Affichez le contenu de mon_dictionnaire.

mon_dictionnaire = {
    "nom" : "Paul",
    "age" : 20,
    "ville" : "Tunis"
}
print(mon_dictionnaire)

# resultat  {'nom': 'Paul', 'age': 20, 'ville': 'Tunis'}


# Exercice 2 : Accès et modification
# Accédez à une valeur spécifique dans mon_dictionnaire en utilisant une clé. 
# Modifiez la valeur associée à une clé dans mon_dictionnaire.
# Affichez le dictionnaire mis à jour.

valeur_specifique = mon_dictionnaire['ville']
mon_dictionnaire['ville'] = 'Ariana'
print(mon_dictionnaire)

# resultat {'nom': 'Paul', 'age': 20, 'ville': 'Ariana'}

# Exercice 3 : Parcourir un dictionnaire

# Utilisez une boucle pour parcourir toutes les clés de mon_dictionnaire et affichez chaque clé.

for cle  in mon_dictionnaire :
    print(cle )
# nom
# age
# ville

# Utilisez une boucle pour parcourir toutes les valeurs de mon_dictionnaire et affichez chaque valeur.

for valeur  in mon_dictionnaire.values():
    print(valeur )

# Paul
# 20
# Ariana

# Utilisez une boucle pour parcourir toutes les paires clé-valeur de mon_dictionnaire et affichez chaque paire.

for cle, valeur in mon_dictionnaire.items():
    print(cle, valeur)

# nom Paul
# age 20
# ville Ariana

#Utilisez la méthode keys() pour afficher toutes les clés de mon_dictionnaire.

for cle in mon_dictionnaire.keys():
    print(cle)

# nom
# age
# ville

nouveau_dictionary = {
    "pays" : "Tunis",
    "Langue" : "Arabe"
}

# Exercice 5 : Fusion de dictionnaires
# Créez un second dictionnaire appelé nouveau_dictionnaire avec des informations supplémentaires.
# Fusionnez mon_dictionnaire et nouveau_dictionnaire pour créer un troisième dictionnaire appelé dictionnaire_combine.
# Affichez le contenu du dictionnaire combiné.

dictionnaire_Combinaison = mon_dictionnaire | nouveau_dictionary
print(dictionnaire_Combinaison)

# resultat {'nom': 'Paul', 'age': 20, 'ville': 'Ariana', 'pays': 'Tunis', 'Langue': 'Arabe'}

# ajouter les elements de nouveau dictionary dans mon dictionaire

mon_dictionnaire.update(nouveau_dictionary)
print(mon_dictionnaire)

# resultat {'nom': 'Paul', 'age': 20, 'ville': 'Ariana', 'pays': 'Tunis', 'Langue': 'Arabe'}

# Exercice 6 : Suppression d'éléments
# Supprimez une clé spécifique de mon_dictionnaire.
# Affichez le dictionnaire après la suppression.

del nouveau_dictionary["Langue"]
print(nouveau_dictionary)

# result {'pays': 'Tunis'}

# Exercice 7 : Compréhension de dictionnaire
# Créez un dictionnaire appelé carre_dict qui 
# contient les carrés des nombres de 1 à 5 en utilisant une compréhension de dictionnaire.
# Affichez le contenu de carre_dict.

carre_dict = {}

for nombre in range(1, 6):
    carre_dict[nombre] = nombre ** 2

print(carre_dict)

# result {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}