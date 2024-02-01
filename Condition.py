# première partie

port_money = 5000
cout_produit = 10000

if  port_money >=cout_produit:
    port_money -= cout_produit
    print(port_money)    


else:
    print("Achat impossible car le cout du produit est superieur à "+str(port_money))

# Deuxième partie

passwords = input("Entrez votre mot de passe ")
passwords_length = len(passwords)

if passwords_length <= 8 :
    print("Le mot de passe est trop court !")

else:
    print("Mot de passe valide !")    


# troisième partie

age = int(input("Quel est votre age ? "))

prix_mineur = 7
prix_mageur = 12


if age < 18 :
    print("Votre montant a payer est " + str(prix_mineur) + " $")

else:
    print("Votre montant a payer est "+str(prix_mageur))

corn = input("Souhaiter vous du pop corn ? ")

if corn == "oui" and age < 18 :
    Total = prix_mineur + 5

else:
    Total = prix_mageur + 5

print("Votre montant a payer est " + str(Total))    

