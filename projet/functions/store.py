# Module d'enregistrement dans un fichier

user_file_path = "projet/logs/user_ids.txt"
cert_file_path = "projet/logs/certs.txt"
locker_file_path = "projet/logs/locker.txt"

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
    return parties[0], parties[1], parties[2]


# Lecture et récupération des informations du fichier user_ids.txt
def read_user_info(email):
    cpt = 0
    for utilisateur in read_file(user_file_path):
        info = recuperer_info(utilisateur)
        if email.strip() == info[0]:
            # print("Utilisateur trouvé dans la base de données.")
            return info
        else:
            cpt += 1
    if cpt == len(list(read_file(user_file_path))):
        # print("Utilisateur non trouvé dans la base de données.")
        return None


# Enregistrement du certificat dans le fichier
def log_cert(user, certificate, date):
    try:
        with open(cert_file_path, 'a') as file:
            file.write(user + ':' + str(certificate) + ':' + str(date) + '\n')
        print("Certificat enregistré avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement du certificat : {e}")


# Lecture et récupération des informations du fichier certs.txt
def read_cert_info(email):
    cpt = 0
    for utilisateur in read_file(cert_file_path):
        info = recuperer_info_cert(utilisateur)
        if email.strip() == info[0]:
            # print("Certificat trouvé dans la base de données")
            return info
        else:
            cpt += 1
    if cpt == len(list(read_file(cert_file_path))):
        # print("Certificat non trouvé dans la base de données.")
        return None


# Supression du certificat si expiré
def del_exp_cert(email):
    try:
        # Lecture du fichier certs.txt
        cert_lines = list(read_file(cert_file_path))

        # Recherche de la ligne correspondant à l'e-mail
        for i, cert_info in enumerate(cert_lines):
            info = recuperer_info_cert(cert_info)
            if email == info[0]:
                # Suppression de la ligne correspondant à l'e-mail
                del cert_lines[i]

                # Réécriture du fichier certs.txt
                with open(cert_file_path, 'w') as file:
                    for line in cert_lines:
                        file.write(line + '\n')

                print("Certificat expiré supprimé avec succès.")
                return  # Sortir de la fonction après la suppression
    except Exception as e:
        print(f"Erreur lors de la suppression du certificat expiré : {e}")


# Lecture du locker pour récuperer les messages
def read_encrypt_info(message_chiffre):
    cpt = 0
    for message in read_file(locker_file_path):
        if message == message_chiffre:
            # print("Message chiffré trouvé dans le locker.")
            return message
        else:
            cpt += 1
    if cpt == len(list(read_file(locker_file_path))):
        # print("Message chiffré non trouvé dans le locker.")
        return None


# Enregistrement du message chiffré dans le locker
def log_message_locker(message_chiffre):
    try:
        with open(locker_file_path, 'a') as file:
            file.write(message_chiffre + '\n')
        print("Message enregistré avec succès dans le locker.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de l'utilisateur : {e}")
