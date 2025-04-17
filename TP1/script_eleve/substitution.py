#!/usr/bin/env python3
# by Louiza Khati
# Substitution


ciphertext = "hglk! ziivgva! glfg xvggv yzgzroov! lm wvgifrg wvh ervh sfnzrmvh! nvnv hr xszjfv hlowzg\
z fmv uznroov jfr o'zggvmw, nvnv hr lm z wvqz zxxlnkor mlgiv yfg, lm xlmgrmf wv klfixszhhvi wvh krizgvh\
jfr mv evfovmg kzh hv yzggiv, xlmgrmfzmg fmv yzgzroov jfr wveizrg wvqz vgiv gvinrmvv vg zylmwlmmzmg wvh\
hlowzgh jfr kvfevmg vgiv hzfevh hr lm hlrtmv ovfih yovhhfivh nzrmgvmzmg! vg klfigzmg, lm hzxirurv vmxliv\
kofh wv nlmwv! jf'vm vhg-ro wvh hlowzgh jfr glnyvmg zkivh xz ? lm ovh uzrg kzhhvi klfi wvh rwrlgh!? \
jfr vh-gf ? gf n'zh uzrg kviwiv nlm gvnkh"

french = {'a': 0.08372093023255814, 'b': 0.01627906976744186, 'c': 0.023255813953488372, 'd': 0.044186046511627906, 
'e': 0.1558139534883721, 'f': 0.009302325581395349, 'g': 0.002325581395348837, 'h': 0.0069767441860465115, 
'i': 0.06976744186046512, 'j': 0.004651162790697674, 'k': 0.0, 'l': 0.03953488372093023, 'm': 0.03255813953488372, 
'n': 0.07906976744186046, 'o': 0.06046511627906977, 'p': 0.030232558139534883, 'q': 0.018604651162790697, 
'r': 0.05116279069767442, 's': 0.09069767441860466, 't': 0.10465116279069768, 'u': 0.06279069767441861, 
'v': 0.011627906976744186, 'w': 0.0, 'x': 0.0, 'y': 0.0, 'z': 0.002325581395348837}

alphabet_in=  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_out= ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']

def substitution (alphabet_in, alphabet_out, plaintext):
    result = ""
    for char in plaintext:
            if char in alphabet_in:
                  index = alphabet_in.index(char)
                  result += alphabet_out[index]

    return print(result)
                                    

# def attack():


substitution(alphabet_in, alphabet_out, "testdephrase")