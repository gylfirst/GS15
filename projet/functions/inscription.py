# Module d'inscription pour les utilisateurs

import random

# Etape 1 : génération de couple de clés publique et privée RSA (1024 bits minimum)
def generer_cles(taille):
    # Fonction pour définir si un nombre est premier ou non
    def est_premier(nombre, tests=5):
        if nombre < 2:
            return False
        for _ in range(tests):
            a = random.randint(2, nombre - 1)
            if pow(a, nombre - 1, nombre) != 1:
                return False
        return True

    # Fonction pour générer un nombre premier
    def generer_nombre_premier(bits):
        # Générer un nombre aléatoire de bits et s'assurer qu'il est premier
        nombre = random.getrandbits(bits)
        while not est_premier(nombre):
            nombre = random.getrandbits(bits)
        return nombre

    # Foncion permettant de calculer l'inverse modulaire
    def inverse_modulaire(a, m):
        # Calculer l'inverse modulaire de a modulo m
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    # Génération de deux nombres premiers aléatoires
    p = generer_nombre_premier(taille)
    q = generer_nombre_premier(taille)

    # Calcul des constantes de RSA
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choisir un exposant de chiffrement e
    e = 65537

    # Calculer l'exposant de déchiffrement d
    d = inverse_modulaire(e, phi_n)

    # Retourner la clé publique et privée
    cle_publique = (n, e)
    cle_privee = (n, d)

    return cle_publique, cle_privee


# Fonction générant les couples de clés avec une taille de base de 1024 bits
def generer_couple_cles(taille):
    pubkey,prvkey = generer_cles(taille)
    key = str(pubkey)+':'+str(prvkey)
    return key


# Etape 2 : enregistrement à l'aide d'un identifiant(email - télélphone)
def generer_user(key):
    id = str(input('Quelle est votre adresse email ? '))
    user = id+':'+key
    return user


# Etape finale : génération du string d'identification
def inscription_user():
    taille = int(input('Quelle taille de clés voulez vous ? '))
    if taille > 1023:
        key = generer_couple_cles(taille)
        user = generer_user(key)
        return user
    else:
        print("La taille de la clé n'est pas assez grande.")
        return None
