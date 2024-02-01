# Creations d'un dictonnaire

etudiant = {
       
       'paul': 12,
       'amza': 20,
       'zakou': 17     
}


print(etudiant['paul'])
# 12

print(etudiant.get('amza','x'))

# 20 s'il n'existe pas de valeur il met x a sa place

for el in etudiant:
        print(el)

# paul
# amza
# zakou

for el in etudiant.values():
        print(el)
# 12
# 20
# 17

cal = sum(etudiant.values())/len(etudiant)
moy = round(cal)
print(moy)

# 16.333333333333332  <-- 16

for nom,val in etudiant.items():
       print(nom,val)

# paul 12
# amza 20
# zakou 17


etudiants = {
       
       'paul':{
              'id': 1,
              'notes':20,
              'mention':'Bien'
              } ,
       'amza': {
              'id': 2,
              'notes':10,
              'mention':'passable'
               },
       'zakou': {
              'id': 3,
              'notes':9,
              'mention':'faible'
              }
}

print(etudiants['zakou']['mention'])
# faible

for el in etudiants:
       print(etudiants[el]['notes'],etudiants[el]['mention'],etudiants[el]['id'])

# 10 passable 2
# 20 Bien 1
# 9 faible 3

etudiants["Imrane"]={
       'id': 4,
       'notes':13,
      'mention':'Assez Bien'
}

for el,val  in etudiants.items():
       print(el,val)

# paul {'id': 1, 'notes': 20, 'mention': 'Bien'}
# amza {'id': 2, 'notes': 10, 'mention': 'passable'}
# zakou {'id': 3, 'notes': 9, 'mention': 'faible'}
# Imrane {'id': 4, 'notes': 13, 'mention': 'Assez Bien'}


etudiants["amza"]["notes"] = 50
etudiants["amza"]["mention"] = 'Tres bien'

print(etudiants["amza"])

# {'id': 2, 'notes': 50, 'mention': 'Tres bien'}

del etudiants["amza"]

for el in etudiants.items():
       print(el)

# ('paul', {'id': 1, 'notes': 20, 'mention': 'Bien'})
# ('zakou', {'id': 3, 'notes': 9, 'mention': 'faible'})
# ('Imrane', {'id': 4, 'notes': 13, 'mention': 'Assez Bien'})
      

if "amza" in etudiants.keys():
       print("existe")
else:
       print("non existe")

# non existe
