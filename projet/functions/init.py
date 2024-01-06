# Module d'initialisation des fichiers

import os

# Fonction d'initialisation
def start():
    # Vérification de la présences des fonctions
    functions_paths = [
        "projet/functions/inscription.py",
        "projet/functions/serp.py",
        "projet/functions/store.py",
        "projet/functions/certificat.py",
        "projet/functions/hash.py",
        "projet/functions/date.py",
        "projet/functions/verif.py",
        "projet/functions/register_file.py",
        "projet/functions/proof.py"
    ]

    # Vérification de la présence des fichiers de logs
    files_paths = [
        "projet/logs/user_ids.txt",
        "projet/logs/certs.txt",
        "projet/logs/locker.txt",
        "projet/logs/crypted_msg.txt"
    ]

    def verifier_existence_fichiers(paths):
        fichiers_inexistants = []
        for path in paths:
            if not os.path.exists(path):
                fichiers_inexistants.append(path)

        return fichiers_inexistants
    
    def creer_fichier(nom_fichier):
        try:
            open(nom_fichier, 'w')
            print(f"Le fichier {nom_fichier} a été créé avec succès.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def check_functions_files():
        fonctions_inexistants = verifier_existence_fichiers(functions_paths)
        if fonctions_inexistants:
            print("Les fonctions suivantes n'existent pas :")
            for fonction in fonctions_inexistants:
                print(f"- {fonction}")
                return False
        else:
            #print("Toutes les fonctions existent.")
            return True

    def init_log_files():
        fichiers_inexistants = verifier_existence_fichiers(files_paths)
        if fichiers_inexistants:
            print("Les fichiers suivants n'existent pas :")
            for fichier in fichiers_inexistants:
                print(f"- {fichier}")
                creer_fichier(fichier)
                return False
        else:
            #print("Tous les fichiers existent.")
            return True
 
    while init_log_files() != True:
        init_log_files()
    
    # Fin de l'initialisation
    if check_functions_files() and init_log_files():
        return True
    else:
        return False
