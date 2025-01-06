# Demander trois nombres à l'utilisateur
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))

# Trouver le plus grand nombre
plus_grand = nombre1  # Par défaut, le premier nombre est considéré comme le plus grand

if nombre2 > plus_grand:
    plus_grand = nombre2
if nombre3 > plus_grand:
    plus_grand = nombre3

# Affichage du résultat
print("Le plus grand nombre est : {plus_grand}")
