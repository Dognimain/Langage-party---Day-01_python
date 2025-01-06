# Demander à l'utilisateur d'entrer plusieurs notes séparées par des virgules
notes = input("Entrez plusieurs notes séparées par des virgules : ")

# Convertir les notes en une liste de nombres
notes_list = notes.split(",")  # Diviser la chaîne par les virgules

# Initialisation de la somme des notes et du nombre de notes
somme = 0
nombre_de_notes = 0

# Ajouter chaque note à la somme et compter le nombre de notes
for note in notes_list:
    somme += float(note)  # Convertir la note en nombre décimal et l'ajouter à la somme
    nombre_de_notes += 1  # Compter le nombre de notes

# Calculer la moyenne
moyenne = somme / nombre_de_notes

# Afficher la moyenne
print("La moyenne des notes est : {moyenne}")
