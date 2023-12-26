# Module de gestion de l'authorité de confiance pour les certificats

import hashlib

# Fonction pour générer et signer un certificat
def generer_certificat(email, cle_publique, cle_privee):
    certificat = f"Email: {email}\nClé publique: {cle_publique}\n"
    
    # Hashage des données du certificat
    hash_certificat = hashlib.sha256(certificat.encode()).hexdigest()

    # Signature du certificat avec la clé privée
    signature = pow(int(hash_certificat, 16), cle_privee, cle_publique)

    print(f"Signature : {signature}")
    return signature

