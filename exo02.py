#on initialise les variables
operation = 0
nombre1 = 0
nombre2 = 0
 
#on demande à l'utilisateur de chosir une operation
print("CALCULATRICE SIMPLE")
print("-------------------")
print("Veuillez choisir l'operation :")
print("1    -   Addition")
print("2    -   Soustraction")
print("3    -   multiplication")
print("4    -   division")
 
operation = int(input())
 
#on demande à l'utilisateur d'entrer les valeurs du premier nombre et du deuxieme
nombre1 = int(input("veuillez entrer la valeur du premier nombre"))
 
nombre2 = int(input("Veuillez entrer la valeur du deuxieme nombre"))
 
#on fait une series de conditions puis on fait l'operation que l'utilisateur a demande
if (operation == 1):
        print(nombre1 + nombre2)
elif operation == 2:
    print(nombre1 - nombre2)   
elif operation == 3:
    print(nombre1 * nombre2)   
elif operation == 4:
    print(nombre1 / nombre2)
