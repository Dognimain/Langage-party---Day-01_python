# Saisie de la phrase par l'utilisateur
phrase = input("Entrez une phrase : ")

# Liste des voyelles
voyelles = "a e i o u y A E I O U Y"

# Comptage des voyelles
nombre_voyelles = sum(1 for lettre in phrase if lettre in voyelles)

# Affichage du résultat
print("Il y a {nombre_voyelles} voyelle(s) dans la phrase.")
