# Module d'inscription pour les utilisateurs

from random import getrandbits

# Etape 1 : génération de couple de clés publiques et privées (1024 bits minimum)
def generer_nombre_premier(taille):
    def est_premier(n, k=5):

        # Vérification si un nombre est premier.
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False

        # Écriture de n - 1 comme 2^r * d avec d impair
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        # Test de la primalité k fois
        for _ in range(k):
            a = getrandbits(n.bit_length())
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    # Génération des nombres aléatoires jusqu'à trouver un nombre premier
    while True:
        nombre = getrandbits(taille)
        if est_premier(nombre):
            return nombre


# Clés avec une taille de 1024 bits
def generer_couple_cles(taille):
    pubkey = generer_nombre_premier(taille)
    prvkey = generer_nombre_premier(taille)
    key=str(pubkey)+':'+str(prvkey)
    return key


# Etape 2 : enregistrement à l'aide d'un identifiant(email - télélphone)
def generer_user(key):
    id=str(input('Quelle est votre adresse email ? '))
    user=id+':'+key
    return user


# Etape finale : génération du string d'identification
def inscription_user():
    taille=int(input('Quelle taille de clés voulez vous ? '))
    if taille > 1023:
        key=generer_couple_cles(taille)
        user=generer_user(key)
        return user
    else:
        print("La taille de la clé n'est pas assez grande")
        return None

