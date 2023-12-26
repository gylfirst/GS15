# Module d'enregistrement dans un fichier

user_file_path = "projet/logs/user_ids.txt"
cert_file_path = "projet/logs/certs.txt"

# Enregistrement des logs des utilisateurs


def log_user(user):
    try:
        with open(user_file_path, 'a') as file:
            file.write(user + '\n')
        print("Utilisateur enregistré avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de l'utilisateur : {e}")


# Lecture des fichiers
def read_file(file):
    # Parcourir les lignes du fichier
    try:
        with open(file, 'r') as file:
            for ligne in file:
                yield ligne.strip()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")


# Récuperer identifiants et clés depuis le string d'indentification
def recuperer_info(user):
    parties = user.split(':')
    return parties[0], parties[1], parties[2]


# Récuperer identifiants et signature depuis le string du certificat
def recuperer_info_cert(user):
    parties = user.split(':')
    return parties[0], parties[1]


# Lecture et récupération des informations du fichier user_ids.txt
def read_user_info(email):
    cpt = 0
    for utilisateur in read_file(user_file_path):
        info = recuperer_info(utilisateur)
        if email.strip() == info[0]:
            print("Utilisateur trouvé dans la base de données")
            return info
        else:
            cpt += 1
    if cpt == len(list(read_file(user_file_path))):
        print("Utilisateur non trouvé dans la base de données")


# Enregistrement du certificat dans le fichier
def log_cert(user, certificate):
    try:
        with open(cert_file_path, 'a') as file:
            file.write(user+':'+str(certificate) + '\n')
        print("Certificat enregistré avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement du certificat : {e}")


# Lecture et récupération des informations du fichier certs.txt
def read_cert_info(email):
    cpt = 0
    for utilisateur in read_file(cert_file_path):
        info = recuperer_info_cert(utilisateur)
        if email.strip() == info[0]:
            print("Certificat trouvé dans la base de données")
            return info
        else:
            cpt += 1
    if cpt == len(list(read_file(cert_file_path))):
        print("Certificat non trouvé dans la base de données")
