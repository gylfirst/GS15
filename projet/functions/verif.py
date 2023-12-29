# Module de vérification des fonctions

import functions.store as store


def check_user_exist(email):
    user = store.read_user_info(email)
    if user != None:
        return True
    else:
        return False


def check_cert_exist(email):
    cert = store.read_cert_info(email)
    if cert != None:
        return True
    else:
        return False
