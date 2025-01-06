# Demander un mot à l'utilisateur
mot = input("Entrez un mot : ")

# Vérifier si le mot est un palindrome
if mot == mot[::-1]:
    print("Le mot '{mot}' est un palindrome.")
else:
    print("Le mot '{mot}' n'est pas un palindrome.")
