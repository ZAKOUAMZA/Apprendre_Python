def main():
    usernames = " Amza "
    age = 24
    wallet = 125.7
    is_happy = True
    print("Bonjour monsieur "+usernames+ ",vous avez "+str(age)+ " ans") 
    
    note1 = int(input("Entrez la premiere note : "))
    note2 = int(input("Entrez la deuxieme note : "))
    note3 = int(input("Entrez la troisieme note : "))

    moyenne = (note1 + note2 + note3)/3

    print("Votre moyenne est "+str(moyenne))

if __name__ == '__main__':
    main()





