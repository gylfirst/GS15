# Enoncé du TP:
#     - avec bitarray (ou autre package python) lire un fichier en binaire, sous la forme d'une suite de bits (et le ré-écrire en binaire, en modifiant quelques bits ici et là ... pour tester)
#     - fonctions arithmétiques modulaire (addition, multiplication, soustraction)
#     - Implémentation du calcul du PGCD (Euclide)
#     - Implémentation de l'inverse modulaire (Fermat / Euler et/ou Euclide étendu / Bezout)
#     - Implémentation de l'exponentiation modulaire rapide

#     - POUR S'AMUSER : implémentation de la décomposition en facteur premier d'un entier (tester le temps en fonction de la taille de l'entier) / calcul de la fonction indicatrice d'Euler
#     - POUR S'AMUSER : implémentation du test de primarité de Fermat et faire un algo permettant de trouver un menteur (voir un p tel que tous les a sont des menteurs)
#       Rappel de théorème de Fermat : Si p est premier alors tout a,  0<a<p, vérifie a^(p-1) = 1 mod p 
#       Aussi si on trouve 0<a<p, vérifiant a^(p-1) = 1 mod p alors il est possible / probable que p soit premier ; si ce n’est pas le cas est appelé un menteur (liar) de la primarité de p ...
    
#     - POUR ALLER PLUS LOIN : implémentation du Théorème des restes Chinois (CRT)
#     - POUR ALLER PLUS LOIN : implémentation du test de primalité de Rabin-Miller

import bitarray

def binafile():
    bits = bitarray.bitarray('0000011111')
    print(bits)

    # write binary in the file
    with open('tp1\\somefile.bin', 'wb') as file:
        bits.tofile(file)

    # read binary from file
    a = bitarray.bitarray()
    with open('tp1\\somefile.bin', 'rb') as file:
        a.fromfile(file)

    print(a)

def arith_functions_menu():
    choice=int(input('1:addition, 2:multiplication, 3:soustraction\n'))

    match choice:
        case 1: 
            add()
        case 2:
            mult()
        case 3:
            sous()
        case _:
            print('Error')

def add():
    print('Addition')

def mult():
    print('Multiplication')

def sous():
    print('Soustraction')

def PGCD():
    a=int(input('Enter the first number: '))
    num1=a
    b=int(input('Enter the second number: '))
    num2=b
    while a != b:
        if a > b:
            a-=b
        else:
            b-=a
    print('Le plus grand commun diviseur de', num1, 'et', num2, 'est :', a)

def inverse_mod():
    a=int(input('Enter the first number: '))
    b=int(input('Enter the second number: '))
    
    if a > b:
        temp=a
        a=b
        b=temp
    
    r1 = b
    r2 = a
    u1 = 0
    v1 = 1
    u2 = 1
    v2 = 0

    while (r2 != 0):
        q = r1//r2
        r3 = r1 
        u3 = u1
        v3 = v1
        r1 = r2
        u1 = u2
        v1 = v2
        r2 = r3 - q*r2
        u2 = u3 - q*u2
        v2 = v3 - q*v2
    
    print('Le plus grand commun diviseur de', a, 'et', b, 'est :', r1)
    print("Il peut s'écrire ainsi (selon Bezout) : ",a,'*',u1,'+',b,'*',v1)

def exp_mod():
    print("j'ai pas encore fait non plus")

# Execute the functions
binafile()
arith_functions_menu()
PGCD()
inverse_mod()
exp_mod()