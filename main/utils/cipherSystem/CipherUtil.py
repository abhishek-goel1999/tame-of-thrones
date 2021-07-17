import abc

class CipherUtil(metaclass = abc.ABC.Meta):
    #define encryption and decryption of meassage

    @abc.abstractmethod
    def decrypt (self,cipheredMessage:str,key):
        pass

    @abc.abstractmethod
    def encrypt (self,plainMessage:str,key):
        pass