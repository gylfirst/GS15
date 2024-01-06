# Module de preuve de connaissance

import functions.hash as hash
import functions.store as st
import functions.certificat as cert

# Fonction pour la preuve de connaissance par chiffrement de message
def preuve_connaissance(email):
    # Encodage du messsage de test
    message="Test de chiffrement"
    H=hash.hash(message.encode())
    hashed_message=int(H,16)

    # Récupération des morceaux de clés de l'utilisateur cible
    info=st.read_user_info(email)
    key=info[1]+':'+info[2]
    n,e,d=cert.get_key_var(key)

    # Génération de la signature avec la clé publique
    signature = pow(hashed_message, e, n)

    # Génération de la signature inverse avec la clé privée
    uncoded_message=pow(signature,d,n)

    # Vérification si les messages hashés
    if uncoded_message == hashed_message:
       return True
    else:
       return False
    