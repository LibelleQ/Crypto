#!/usr/bin/env python3

ciphertext = "gz xcdaamzhzio kvm yzxvgvbz zno avdwgz!"
alphapet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
L = [] # empty list
# L.append('a') # append a to the list
#print(L[0]) # print fist element of L
#L.index('a') # position(s) of element 'a' in the list L
# len(L) # number of element in L
# type(L) # type of variable L
# c = a%b # c = a modulo (b)
# a.lower() # string method --> lowercase
# a.upper() # string method --> uppercase
# M = ''.join(L) # concatenate L element with '' in between


def encrypt(key, plaintext):
    encrypted_text = ""
    for char in plaintext:
        if char in alphapet:
            original_index = alphapet.index(char)
            new_index = (original_index + key) % len(alphapet)
            encrypted_text += alphapet[new_index]
    return print(encrypted_text)

def decrypt(key, ciphertext):
    decrypted_text = ""
    for char in ciphertext:
        if char in alphapet:
            original_index = alphapet.index(char)
            new_index = (original_index - key) % len(alphapet)
            decrypted_text += alphapet[new_index]
    return print(decrypted_text)


def attack(ciphertext):
    for key in range(1, 25):
        decrypted_text = decrypt(key, ciphertext)
        print(decrypted_text)



encrypt(3,"toto")
decrypt(3,"wrwr")
attack(ciphertext)