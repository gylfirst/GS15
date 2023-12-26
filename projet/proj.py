# Importation des libraries
import numpy as np
import os
import bitarray as ba
import functions.serp as serp, functions.inscription as inscription, functions.store as store, functions.certificat as certificat

# Fonction de chiffrement, déchiffrement de message
def def1():
    return

# Création d'un couple de clé publique/privée
def def2():
    infos=inscription.inscription_user()
    store.log_user(infos)
    return

# Signature d'un certificat
def def3():
    email=str(input("Quelle adresse mail voulez-vous recuperer ? "))
    user=store.read_user_info(email)
    certificat_utilisateur = certificat.generer_certificat(user[0], int(user[1]), int(user[2]))
    store.log_cert(user[0],certificat_utilisateur)
    return

# Vérification d'un certificat
def def4():
    email=str(input("Quelle adresse mail voulez-vous recuperer ? "))
    user=store.read_user_info(email)
    cert=store.read_cert_info(email)
    certificat.verifier_certificat(user, int(cert[1]))
    return

# Enregistrement d'un document dans un locker
def def5():
    return

# Envoie d'un message en asynchrone
def def6():
    return

# Demande d'une preuve de connaissance
def def7():
    return

# Fonction de création du menu, à l'aide d'un switch case
def menu():
    #while True:
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
menu()
