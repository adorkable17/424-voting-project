# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:12:42 2020

@author: danau
"""
#taking in the encrypted vote with digital signature
def Verify_Signature (encryptSign, RSAkey) : 
    plaintext = rsa.decrypt(encryptSign,RSAkey)
    namefound = False
    #seeing if the encrptyed name is in the file 
    with open('myfile.txt') as myfile:    #myfile just a placeholder for the file of names 
     if plaintext in myfile.read():
         namefound = True
    return namefound 
    

#need to know where in the file the name for the voter is being located in order to 
#check to see if the name is correct 