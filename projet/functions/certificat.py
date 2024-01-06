# Module de gestion de l'authorité de confiance pour les certificats

import functions.hash as hashf
import functions.date as dat

auth_key="(691828171298457272381677622628619997243493402788608438149194634739859677974020567292649527111845806241405867584588927172744597535311646201208804650424466096179870815779308876900448495638902659061058770969101133334099875998204352359935483514414110083987049186372505287040131093602808673051746528945270881785964975861559542866203982810285681790877418541740339840570379501925465729277814781650880327608378545376117629111971910380982874126342059879529527643292730267232004131214640510953146484974034639330369972920467266621106305299062521176694991118242205663428609499258030771473104116609672895444185178712150980791433, 65537):(691828171298457272381677622628619997243493402788608438149194634739859677974020567292649527111845806241405867584588927172744597535311646201208804650424466096179870815779308876900448495638902659061058770969101133334099875998204352359935483514414110083987049186372505287040131093602808673051746528945270881785964975861559542866203982810285681790877418541740339840570379501925465729277814781650880327608378545376117629111971910380982874126342059879529527643292730267232004131214640510953146484974034639330369972920467266621106305299062521176694991118242205663428609499258030771473104116609672895444185178712150980791433, 238994610650427585130860145815523394992030313244947053415593733776499124301262273883540370993670583842797638618110278334237723548521532416732034381885193286502468457043251185941165356077708106888358798461028879238964572571209340333383269706674633448303504792399309087974557394436235841706082692453437489717743784158913777917837399703412714772925831197355947664024348138978505459493690601476215704187495022801262172119668491577178799254055829290372962241242949585920458647722737913244438448994035925127592339939574853280012006144305726027110713664718197809201330544337638096251146600668038659531900326822491322890433)"

# Fonction pour récuperer les valeurs de n,e,d des clé RSA
def get_key_var(key):
    import ast
    keys=key.split(":")
    tuples = [ast.literal_eval(chaine) for chaine in keys]
    
    return tuples[0][0], tuples[0][1], tuples[1][1]


# Fonction pour générer et signer un certificat
def generer_certificat(email, cle_publique):
    certificat = f"Email: {email}\nClé publique: {cle_publique}\n"

    # Hashage des données du certificat
    hash_certificat = hashf.hash(certificat.encode())

    # Signature du certificat avec la clé privée
    n,e,d=get_key_var(auth_key)
    signature = pow(int(hash_certificat, 16), e, n)

    # print(f"Signature : {signature}")
    return signature


# Fonction pour vérifier la signature d'un certificat
def verifier_certificat(user, signature, date):
    certificat = f"Email: {user[0]}\nClé publique: {user[1]}\n"

    # Hashage des données du certificat
    hash_certificat = hashf.hash(certificat.encode())

    # Signature du certificat avec la clé privée
    n,e,d=get_key_var(auth_key)
    signature_base = pow(int(hash_certificat, 16), e, n)

    if signature == signature_base:
        if dat.get_date() < dat.get_exp_date(int(date)):
            print("Le certificat est valide")
            return False
        else:
            print("Le certificat est expiré")
            return True
    else:
        print("Le certificat n'est pas valide (signature différente)")
