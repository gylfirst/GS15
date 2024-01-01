# Module de vérification des fonctions

import functions.store as store

# Verifie si l'utilisateur existe dans le fichier
def check_user_exist(email):
    user = store.read_user_info(email)
    if user != None:
        return True
    else:
        return False


# Verifie si le certificat existe dans le fichier
def check_cert_exist(email):
    cert = store.read_cert_info(email)
    if cert != None:
        return True
    else:
        return False


# Vérifie si le message existe déjà dans le locker
def check_encrypt_exist(message_chiffre):
    msg=store.read_encrypt_info(message_chiffre)
    if msg != None:
        return True
    else:
        return False
