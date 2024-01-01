# Module d'enregistrement d'un fichier sécurisé

cle='jesuisunprojetdeGS15'

# Fonction de chiffrement du contenu par le chiffrement de Vignere
def chiffre_vigenere(message):
    message_chiffre = ""
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            decalage = ord(cle[i % len(cle)].upper()) - ord('A')
            if char.isupper():
                message_chiffre += chr((ord(char) + decalage - ord('A')) % 26 + ord('A'))
            else:
                message_chiffre += chr((ord(char) + decalage - ord('a')) % 26 + ord('a'))
        else:
            message_chiffre += char
    return message_chiffre


# Fonction de déchiffrement du contenu par le chiffrement de Vignere
def dechiffre_vigenere(message_chiffre):
    message_dechiffre = ""
    for i in range(len(message_chiffre)):
        char = message_chiffre[i]
        if char.isalpha():
            decalage = ord(cle[i % len(cle)].upper()) - ord('A')
            if char.isupper():
                message_dechiffre += chr((ord(char) - decalage - ord('A')) % 26 + ord('A'))
            else:
                message_dechiffre += chr((ord(char) - decalage - ord('a')) % 26 + ord('a'))
        else:
            message_dechiffre += char
    return message_dechiffre
