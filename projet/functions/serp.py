# Module de l'algorithme de chiffrement symétrique par bloc SERPENT
import numpy as np


# Fonction de padding
def padding(value, index):
    value = str(value)
    pad = index - len(value)
    if pad != 0:
        value = '0' * pad + value
    return value


def swap(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp
    return array


def sbox_swap(sbox):
    new_sbox = sbox.copy()
    for index_box in range(32):
        for index_bits in range(16):
            i = index_bits + sbox[index_box][index_bits]
            j = sbox[i][index_bits]
            swap(new_sbox, new_sbox[index_box][index_bits], new_sbox[index_box][j])
    return new_sbox


sbox = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
        [], [], [], []]
# SBOX_0
sbox[0] = [
    # S-box 1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    # S-box 2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    # S-box 3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    # S-box 4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    # S-box 5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    # S-box 6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    # S-box 7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    # S-box 8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]


def generate_sbox():
    global sbox
    for i in range(31):
        sbox[i + 1] = sbox_swap(sbox[i])
    return sbox


def initial_swap(array):
    copy_arr = array.copy()
    IniPerm = np.arange(128)
    for i in range(127):
        IniPerm[i] = (32 * i) % 127
    for i in range(128):
        array[i] = copy_arr[IniPerm[i]]
    return array


def final_swap(array):
    copy_arr = array.copy()
    FinPerm = np.arange(128)
    for i in range(127):
        FinPerm[i] = (4 * i) % 127
    for j in range(128):
        array[j] = copy_arr[FinPerm[j]]
    return array


# Vérification de l'aléatoire dans les SBOXs
def get_random(sbox):
    for i in range(31):
        sbox[i + 1] = sbox_swap(sbox[i])
    ref = sbox[0]
    cpt = 0
    for soussbox in sbox:
        if soussbox == ref:
            cpt += 1
    print("Pourcentage de SBOXs similaires :", str(((cpt - 1) / 32) * 100) + '%')


# Génération de la clé d'itération initiale
def generate_init_key():
    import random

    # Générer une clé de 256 bits (32 octets)
    random_key = bytearray(random.getrandbits(8) for i in range(32))

    # Diviser la clé en 8 blocs de 32 bits
    key_blocks = [random_key[i:i + 4] for i in range(0, len(random_key), 4)]

    return key_blocks


# Fonction de construction des différentes clés d'itération
def generate_iter_keys(blocks):
    keys = []
    for i in range(33):
        key = [blocks[i * 4].hex(), blocks[i * 4 + 1].hex(), blocks[i * 4 + 2].hex(), blocks[i * 4 + 3].hex()]
        # for j in range(4):
        #     key[j]=int(key[j],16)
        # key=str(key[0])+str(key[1])+str(key[2])+str(key[3])
        bin_key = [bin(int(key, 16))[2:] for key in key]
        bin_key = [padding(key, 32) for key in bin_key]
        bin_key = bin_key[0] + bin_key[1] + bin_key[2] + bin_key[3]
        keys.append(bin_key)
    return keys


# Fonction de la permutation circulaire
def circular_permutation(value, n, direction):
    value_as_int = int.from_bytes(value, 'big')
    result = ((value_as_int << n) | (value_as_int >> (32 - n))) & 0xFFFFFFFF
    return result.to_bytes(4, 'big')


# Fonction de la permutation circulaire en binaire
def bin_circular_permutation(value, n, direction):
    if len(str(value)) != 32:
        print(str(value))
        raise ValueError(f"La longueur de la chaîne binaire doit être de 32 bits, elle est de {len(str(value))}")

    # Effectuez la permutation circulaire à gauche
    if direction == 'left':
        shifted_string = value[n:] + value[:n]
    # Effectuez la permutation circulaire à droite
    elif direction == 'right':
        shifted_string = value[-n:] + value[:-n]

    return shifted_string


# Fonction de décalage de bits (avec perte)
def shift_bits(value, k, direction):
    if not value:
        raise ValueError("La chaîne binaire ne peut pas être vide")

    # Assurez-vous que la chaîne binaire est de la bonne longueur
    if len(str(value)) < k:
        raise ValueError(f"La chaîne binaire doit avoir au moins {k} bits")

    # Effectuez le découpage pour supprimer les premiers bits
    if direction == 'left':
        result_string = value[k:]
    elif direction == 'right':
        result_string = value[:-k]
    else:
        print("Mauvaise direction")

    return result_string


# Fonction du calcul des blocs supplémentaires de la clé d'itération
def calculate_wi(w8, w5, w3, w1, omega, i):
    result = bytes(x ^ y for x, y in zip(w8, w5))
    result = bytes(x ^ y for x, y in zip(result, w3))
    result = bytes(x ^ y for x, y in zip(result, w1))
    result = bytes(x ^ y for x, y in zip(result, omega.to_bytes(4, 'big')))
    result = bytes(x ^ y for x, y in zip(result, i.to_bytes(4, 'big')))

    result = circular_permutation(result, 11, 'left')
    return bytearray(result)


# Génération des blocs supplémentaires
def generate_iter_blocs(w):
    omega = 0x9e3779b9
    for i in range(8, 132, 1):
        result = calculate_wi(w[i - 8], w[i - 5], w[i - 3], w[i - 1], omega, i)
        w.append(result)
    return w


def revert_s_box(part, s_box):
    if len(part) != 4:
        raise ValueError("La longueur de la partie doit être de 4 bits")
    value = int(part, 2)
    try:
        substituted_value = s_box.index(value)
    except IndexError:
        raise ValueError(f"Index de S-box invalide : index={value}")

    result = format(substituted_value, '04b')

    return result


def apply_s_box(part, s_box):
    if len(part) != 4:
        raise ValueError("La longueur de la partie doit être de 4 bits")
    index = int(part, 2)
    try:
        substituted_value = s_box[index]
    except IndexError:
        raise ValueError(f"Index de S-box invalide : index={index}")

    result = format(substituted_value, '04b')

    return result


def revert_s_box_to_words(words, s_box):
    result_words = []
    for i in range(len(words)):
        word = words[i]
        if len(word) != 32:
            raise ValueError("La longueur de chaque mot doit être de 32 bits")

        # Divisez le mot en huit parties de 4 bits et appliquez la S-box à chaque partie
        parts = [word[i:i + 4] for i in range(0, 32, 4)]
        result_parts = []
        for j in range(len(parts)):
            part = parts[j]
            result_parts.append(revert_s_box(part, s_box[8 * i + j]))

        # Concaténez les résultats pour former le mot résultant
        result_word = ''.join(result_parts)
        result_words.append(result_word)

    return result_words


def apply_s_box_to_words(words, s_box):
    result_words = []
    for i in range(len(words)):
        word = words[i]
        if len(word) != 32:
            raise ValueError("La longueur de chaque mot doit être de 32 bits")

        # Divisez le mot en huit parties de 4 bits et appliquez la S-box à chaque partie
        parts = [word[i:i + 4] for i in range(0, 32, 4)]
        result_parts = []
        for j in range(len(parts)):
            part = parts[j]
            result_parts.append(apply_s_box(part, s_box[8 * i + j]))

        # Concaténez les résultats pour former le mot résultant
        result_word = ''.join(result_parts)
        result_words.append(result_word)

    return result_words


# Transformation Linéaire
def linear_transfo(message, itt, key):
    global sbox

    words = bin(int(message, 2) ^ int(key, 2))[2:]
    words = padding(words, 128)
    message = []
    for i in range(4):
        message.append(str(words)[32 * i:32 * i + 32])
        message[i] = padding(message[i], 32)
    message = apply_s_box_to_words(message, sbox[itt])

    X = message.copy()

    def int_pad(X):
        for i in range(4):
            X[i] = padding(X[i], 32)
        return X

    # # Décalage et XOR

    X[0] = bin_circular_permutation(X[0], 13, 'left')
    X[2] = bin_circular_permutation(X[2], 3, 'left')
    X[1] = bin(int(X[1], 2) ^ int(X[0], 2) ^ int(X[2], 2))[2:]
    X = int_pad(X)
    X[3] = bin(int(X[3], 2) ^ int(X[2], 2) ^ int(shift_bits(X[0], 3, 'left'), 2))[2:]
    X = int_pad(X)
    X[1] = bin_circular_permutation(X[1], 1, 'left')
    X[3] = bin_circular_permutation(X[3], 7, 'left')
    X[0] = bin(int(X[0], 2) ^ int(X[1], 2) ^ int(X[3], 2))[2:]
    X = int_pad(X)

    X[2] = bin(int(X[2], 2) ^ int(X[3], 2) ^ int(shift_bits(X[1], 7, 'left'), 2))[2:]
    X = int_pad(X)
    X[0] = bin_circular_permutation(X[0], 5, 'left')
    X[2] = bin_circular_permutation(X[2], 22, 'left')
    # # Formation du block
    message = ''
    for i in range(4):
        message += X[i]
    return message


def revert_linear_transfo(word, itt, key):
    message = []
    for i in range(4):
        message.append(str(word)[32 * i:32 * i + 32])

    def int_pad(X):
        for i in range(4):
            X[i] = padding(X[i], 32)
        return X

    X = message.copy()
    X[2] = bin_circular_permutation(X[2], 22, 'right')
    X[0] = bin_circular_permutation(X[0], 5, 'right')
    X[2] = bin(int(X[2], 2) ^ int(X[3], 2) ^ int(shift_bits(X[1], 7, 'left'), 2))[2:]
    X = int_pad(X)

    X[0] = bin(int(X[0], 2) ^ int(X[1], 2) ^ int(X[3], 2))[2:]
    X = int_pad(X)
    X[3] = bin_circular_permutation(X[3], 7, 'right')
    X[1] = bin_circular_permutation(X[1], 1, 'right')
    X[3] = bin(int(X[3], 2) ^ int(X[2], 2) ^ int(shift_bits(X[0], 3, 'left'), 2))[2:]
    X = int_pad(X)
    X[1] = bin(int(X[1], 2) ^ int(X[0], 2) ^ int(X[2], 2))[2:]
    X = int_pad(X)
    X[2] = bin_circular_permutation(X[2], 3, 'right')
    X[0] = bin_circular_permutation(X[0], 13, 'right')
    X = revert_s_box_to_words(X, sbox[itt])
    # # Formation du block
    message = ''
    for i in range(4):
        message += X[i]
    words = bin(int(message, 2) ^ int(key, 2))[2:]
    words = padding(words, 128)
    return words


def generate_words(msg):
    arr = bytes(msg, 'latin-1')
    words = [""]
    i = 0
    for bite in arr:
        a = padding(bin(int(bite)).replace("0b", ""), 8)
        words[i] += a
        if len(words[i]) >= 128:
            i += 1
            words.append("")
    return words


def get_text_from_words(words):
    arr = []
    for word in words:
        a = [word[i:i + 8] for i in range(0, len(word), 8)]
        for j in a:
            k = ''
            for lj in j:
                k += str(lj)
            if k != '00000000':
                arr.append(int(k, 2))
    txt = bytes(arr).decode('latin-1')
    return txt


def chiff():
    global sbox
    msg = "Débug des XOR, plus jamais de ma vie"
    words = generate_words(msg)
    # Génération des SBOXs
    sbox = generate_sbox()
    # Génération des clés
    w = generate_init_key()
    wb = generate_iter_blocs(w)
    iter_keys = generate_iter_keys(wb)

    # initial swap
    new_words = []
    for word in words:
        if len(word) != 128:
            word = padding(word, 128)
        word = [int(x) for x in word]
        word = initial_swap(word)
        str_word = ''
        for ch in word:
            str_word += str(ch)
        new_words.append(str_word)
    final_words = []

    for i in range(len(new_words)):
        # 31 premières itérations
        for itt in range(31):
            new_words[i] = linear_transfo(new_words[i], itt, iter_keys[itt])
        word_a = bin(int(new_words[i], 2) ^ int(iter_keys[31], 2))[2:]
        word_a = padding(word_a, 128)
        message = []

        # 32ème itération
        for j in range(4):
            message.append(str(word_a)[32 * j:32 * j + 32])
            message[j] = padding(message[j], 32)
        message = apply_s_box_to_words(message, sbox[31])
        word_a = ''
        for worrd in message:
            word_a += worrd
        word_a = bin(int(word_a, 2) ^ int(iter_keys[32], 2))[2:]

        # final swap
        word_a = padding(word_a, 128)
        word = final_swap([int(x) for x in str(word_a)])
        str_word = ''
        for ch in word:
            str_word += str(ch)
        final_words.append(str_word)
    return final_words, w


def unchiff(words, key):
    global sbox
    # Génération des clés
    wb = generate_iter_blocs(key)
    iter_keys = generate_iter_keys(wb)
    # Génération des SBOXs
    sbox = generate_sbox()

    #inversion du swap final
    new_words = []
    for word in words:
        if len(word) != 128:
            word = padding(word, 128)
        word = [int(x) for x in word]
        word = initial_swap(word)
        str_word = ''
        for ch in word:
            str_word += str(ch)
        new_words.append(str_word)
    final_words = []

    for i in range(len(new_words)):
        # inversion de la 32ème itération

        word_a = bin(int(new_words[i], 2) ^ int(iter_keys[32], 2))[2:]
        word_a = padding(word_a, 128)
        word_a = padding(word_a, 128)
        message = []
        for j in range(4):
            message.append(str(word_a)[32 * j:32 * j + 32])
        message = revert_s_box_to_words(message, sbox[31])
        word_a = ''
        for worrd in message:
            word_a += worrd
        new_words[i] = bin(int(word_a, 2) ^ int(iter_keys[31], 2))[2:]
        new_words[i] = padding(new_words[i], 128)

        # inversion des 31 premières itérations
        for itt in range(31):
            new_words[i] = revert_linear_transfo(new_words[i], 30 - itt, iter_keys[30 - itt])

        # inversion de l'initial swap
        word = final_swap([int(x) for x in str(new_words[i])])
        str_word = ''
        for ch in word:
            str_word += str(ch)
        final_words.append(str_word)
    return final_words


if __name__ == '__main__':
    words, key = chiff()
    print(words)
    txt = unchiff(words, key)
    print(txt)
    print(get_text_from_words(txt))