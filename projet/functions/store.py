# Module d'enregistrement dans un fichier

file_path="projet/logs/user_ids.txt"

# Enregistrement des logs des utilisateurs
def log_user(user):
    try:
        with open(file_path, 'a') as file:
            file.write(user + '\n')
        print("Utilisateur enregistré avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de l'utilisateur : {e}")


# Lecture des logs
def read_logs():
    ## Lecture du fichier pour trouver l'utilisateur
    try:
        with open(file_path, 'r') as file:
            for ligne in file:
                yield ligne.strip()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")


## Récuperer identifiants et clés depuis le string d'indentification
def recuperer_info(user):
    parties = user.split(':')
    return parties[0], parties[1], parties[2]

def read_inf():
    cpt=0
    email=str(input("Quelle adresse mail voulez vous recuperer ? "))
    for utilisateur in read_logs():
        #print(utilisateur)
        info=recuperer_info(utilisateur)
        if email.strip() == info[0]:
            print("Utilisateur trouvé dans la base de données")
            return
        else:
            cpt+=1
    if cpt == len(list(read_logs())):
        print("Utilisateur non trouvédans la base de données")

