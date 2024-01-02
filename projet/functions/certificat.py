# Module de gestion de l'authorité de confiance pour les certificats

import functions.hash as hashf
import functions.date as d

auth_pub_key=117595882689524427769631721863580324628821668756809407793988988210482186163487328473479561168432343563943889989764233725451612159627288958435757078857666054377960187915455132575735738371455584463981168090612200568210612680488053849416193553008349975287239001686275630206557807521941176321065559344070585354457
auth_prv_key=170156074705106353377093421220632309463078213902928261445892305679988106903285508034933303358294557002807239893779232308731025614120458577101638520322839677249107539446794060189970419327728883133664927220151617452891725018278119384197881623682422067693942773735821459939805821594661298767372051856804079719823

# Fonction pour générer et signer un certificat
def generer_certificat(email, cle_publique):
    certificat = f"Email: {email}\nClé publique: {cle_publique}\n"

    # Hashage des données du certificat
    hash_certificat = hashf.hash(certificat.encode())

    # Signature du certificat avec la clé privée
    signature = pow(int(hash_certificat, 16), auth_prv_key, cle_publique)

    # print(f"Signature : {signature}")
    return signature


# Fonction pour vérifier la signature d'un certificat
def verifier_certificat(user, signature, date):
    certificat = f"Email: {user[0]}\nClé publique: {int(user[1])}\n"

    # Hashage des données du certificat
    hash_certificat = hashf.hash(certificat.encode())

    # Signature du certificat avec la clé privée
    signature_base = pow(int(hash_certificat, 16), auth_prv_key, int(user[1]))

    if signature == signature_base:
        if d.get_date() < d.get_exp_date(int(date)):
            print("Le certificat est valide")
            return False
        else:
            print("Le certificat est expiré")
            return True
    else:
        print("Le certificat n'est pas valide (signature différente)")
