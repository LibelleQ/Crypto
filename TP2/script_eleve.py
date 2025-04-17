from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 16
# variable de type byte 'immutable' (ne peut être modifiée). Il s'agit d'un tableau d'octets.
a = b'toto'

#variable de type bytearray (modifiable)
b = bytearray(b'toto')
#!/usr/bin/env python3
# Padding manuel sans bibliothèque externe

# Taille de bloc d'exemple (AES)
BLOCK_SIZE = 16

plaintext = b'toto'

def pad_pkcs7(data, block_size):
    # Nombre d'octets à ajouter
    pad_len = block_size - (len(data) % block_size)
    # Le padding est constitué de pad_len répétitions de la valeur pad_len
    return data + bytes([pad_len] * pad_len)

def pad_iso7816(data, block_size):
    # ISO/IEC 7816-4 : on ajoute d'abord un octet 0x80 puis des 0x00
    pad_len = block_size - (len(data) % block_size)
    # Le padding commence par 0x80 suivi de (pad_len - 1) octets 0x00
    return data + bytes([0x80]) + bytes([0x00] * (pad_len - 1))

def pad_x923(data, block_size):
    # X9.23 : on ajoute d'abord des 0x00 puis le dernier octet est la longueur du padding
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([0x00] * (pad_len - 1)) + bytes([pad_len])

# Application des paddings sur plaintext
plaintext_pkcs7 = pad_pkcs7(plaintext, BLOCK_SIZE)
plaintext_iso7816 = pad_iso7816(plaintext, BLOCK_SIZE)
plaintext_x923 = pad_x923(plaintext, BLOCK_SIZE)

print("Plaintext original :", plaintext)
print("PKCS#7 padded    :", plaintext_pkcs7, " (taille :", len(plaintext_pkcs7), ")")
print("ISO7816-4 padded :", plaintext_iso7816, " (taille :", len(plaintext_iso7816), ")")
print("X9.23 padded     :", plaintext_x923, " (taille :", len(plaintext_x923), ")")



#Remplir un bytearray à partir de valeur hexa directement
c = bytearray.fromhex("0178be45")

# padding 
# plaintext_padde = pad(plaintext_unpad, AES.block_size, style = 'iso7816')
# cipher = AES.new(key, AES.MODE_ECB) ensuite ciphertext = cipher.encrypt(plaintext)
# r = get_random_bytes(22) #génération de 22 octets aléatoires
# c[0:16] #affichage des octets entre 0 et 16 du bytearray c

