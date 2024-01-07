# Importation des libraries

import numpy as np
import os
import bitarray as ba
import subprocess
import functions.init as init
import functions.serp as serp
import functions.inscription as inscription
import functions.store as store
import functions.certificat as certificat
import functions.date as date
import functions.verif as verif
import functions.register_file as rf
import functions.proof as proof
import functions.hash as hash

# Fonction de chiffrement, déchiffrement de message
def def1():
    # Temporaire
    script_path = 'projet/functions/serp.py'
    subprocess.run(['python', script_path])
    
    # Faire la fonction qui enregistre dans un fichier et qui peut le déchiffrer depuis la lecture du fichier
    """ 
    choice=input("Voulez vous chiffrer (1) ou déchiffrer (2) un message ? ")
        match choice:
            case "1":
                message_to_crypt = str(input("Quel est votre message ? "))
                store.log_crypt(message_to_crypt)
            case "2":
                message_to_uncrypt = str(input("Quel est votre message à déchiffrer ? "))
                msg_uncrypt = store.read_crypt(message_to_uncrypt)
                print(f"Votre message '{message_to_uncrypt}' déchiffré est le suivant :\n{msg_uncrypt}")
            case _:
                print("Vous avez fait une erreur dans la selection !") 
    """
    return


# Création d'un couple de clé publique/privée
def def2():
    infos = inscription.inscription_user()
    if not verif.check_user_exist(infos.split(':')[0]):
        store.log_user(infos)
    else:
        print("L'utilisateur existe déjà")
    return


# Signature d'un certificat
def def3():
    email = str(input("Quelle adresse mail voulez-vous recuperer ? "))
    if verif.check_user_exist(email):
        if not verif.check_cert_exist(email):
            user = store.read_user_info(email)
            certificat_utilisateur = certificat.generer_certificat(
                user[0], user[1])
            store.log_cert(user[0], certificat_utilisateur, date.get_date())
        else:
            print("Certificat déjà trouvé")
    else:
        print("Utilisateur non trouvée")
    return


# Vérification d'un certificat
def def4():
    email = str(input("Quelle adresse mail voulez-vous recuperer ? "))
    if verif.check_user_exist(email):
        if verif.check_cert_exist(email):
            user = store.read_user_info(email)
            cert = store.read_cert_info(email)
            expired = certificat.verifier_certificat(
                user, int(cert[1]), cert[2])
            if expired:
                store.del_exp_cert(email)
        else:
            print("Certificat non existant")
    else:
        print("Utilisateur non trouvée")
    return


# Enregistrement d'un document dans un locker
def def5():
    message=str(input("Quel message voulez-vous mettre dans le coffre-fort ? "))
    msg=rf.chiffre_vigenere(message)
    hashed_message=hash.hash(msg.encode())
    if not verif.check_encrypt_exist(hashed_message):
        store.log_message_locker(hashed_message)
    else:
        print("Message déjà trouvé dans le locker.")
    return


# Envoie d'un message en asynchrone
def def6():
    return


# Demande d'une preuve de connaissance
def def7():
    email = str(input("Pour quelle adresse mail voulez-vous vérifier la preuve de connaissance ? "))
    if verif.check_user_exist(email):
        if proof.preuve_connaissance(email):
            print("La preuve de connaissance est validée")
        else:
            print("La preuve de connaissance n'est pas valide.")
    else:
        print("Utilisateur non trouvée")
    return


# Fonction de création du menu, à l'aide d'un switch case
def menu():
    # while True:
    print("Bonjour ô maître Rémi ! Que souhaitez vous faire aujourd'hui ?")
    print("->1<- Chiffrer / déchiffrer des message.")
    print("->2<- Créer un couple de clé publique / privée (générer un grand nombre premier)")
    print("->3<- Signer / générer un certificat.")
    print("->4<- Vérifier un certificat.")
    print("->5<- Enregistrer un document dans le coffre fort.")
    print("->6<- Envoyer un message (asynchrone).")
    print("->7<- Demander une preuve de connaissance.")
    print("->0<- I WANT IT ALL !! I WANT IT NOW !! SecCom from scratch?.")
    choice = input("Quel est votre choix : ")

    match choice:
        case "1":
            def1()
        case "2":
            def2()
        case "3":
            def3()
        case "4":
            def4()
        case "5":
            def5()
        case "6":
            def6()
        case "7":
            def7()
        case "0":
            def1()
            def2()
            def3()
            def4()
            def5()
            def6()
            def7()
        case _:
            print("Vous avez fait une erreur dans la selection !")


# Execution du script
if init.start():
    print("Initialisation complète !\nLancement du logiciel en cours....\n\n")
    menu()
else:
    print("Initialisation non réussie...\nMerci de ré-essayer.")
