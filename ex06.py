import random

# Génération d'un nombre aléatoire entre 1 et 100
nombre_a_deviner = random.randint(1, 100)

print("Bienvenue dans le jeu de devinettes !")
print("J'ai choisi un nombre entre 1 et 100. À vous de deviner !")

# Initialisation des variables
devine = False
tentatives = 0

# Boucle de devinettes
while not devine:

 # Saisie de l'utilisateur
 proposition = int(input("Entrez votre proposition : "))
 tentatives += 1

 # Vérification de la proposition
if proposition < nombre_a_deviner:
        print("C'est plus !")
elif proposition > nombre_a_deviner:
    print("C'est moins !")
else:
     print(f"Bravo ! Vous avez trouvé le nombre {nombre_a_deviner} en {tentatives} tentatives.")
     devine = True
    
print("Veuillez entrer un nombre entier valide.")
