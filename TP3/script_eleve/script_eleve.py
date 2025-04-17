#https://pycryptodome.readthedocs.io/en/latest/src/hash/hash.html
from Crypto.Hash import SHA256, HMAC
m_1 = b'tito'
m_2 = b'titn'

print(type(m_1))
print(type(m_2))

print(m_1.hex())
print(m_2.hex())

def xor(x, y):
    if type(x) == bytearray and type(y) == bytearray:
        if len(x) == len(y):
            return bytearray([a ^ b for a, b in zip(x, y)])
        else:
            return "Error on len"
    else:
        return "Error not bytearray"

ba1 = bytearray(m_1)
ba2 = bytearray(m_2)

resultat = xor(ba1, ba2)
print(resultat.hex())

# On constate qu'il y a un bytes de différence 
# donc sur la sortie nous avons un hash complétement différent, donc nous avons bien la diffusion ici 

h_1 = SHA256.new()
h_2 = SHA256.new()
h_1.update(m_1) 
h_2.update(m_2) 
print(h_1.hexdigest())
print(h_2.hexdigest())

message = b'message'
m = SHA256.new()
m.update(message)
hmac = HMAC.new()
hmac.update(m)
