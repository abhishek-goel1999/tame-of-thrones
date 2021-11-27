from main.utils.cipherSystem.CipherUtil import CipherUtil

class CaesarCipherUtil(CipherUtil): 
    #inherit and define cypher func of abstract class CipherUtil
    def encrypt (self, plainMessage:str, key:int):
        cipheredMessage = ''
        for i in plainMessage:
            if i.isalpha():
                if i.isupper():
                    cipheredMessage += chr((ord(i) - ord('A') + key) % 26 + ord('A'))
                else:
                    cipheredMessage += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
            else:
                cipheredMessage += chr(ord(i) + key)

        return cipheredMessage

    def decrypt (self, cipheredMessage:str, key:int):             
        plainMessage = ''
        
        for i in cipheredMessage:
            if i.isalpha():
                if i.isupper():
                    plainMessage += chr((ord(i) - ord('A') - key) % 26 + ord('A'))
                else:
                    plainMessage += chr((ord(i) - ord('a') - key) % 26 + ord('a'))
            else:
                plainMessage += chr(ord(i) - key)
        
        return plainMessage