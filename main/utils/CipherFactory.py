from main.utils.cipherSystem import *
# return cipher technique requested by the client
def getCipherTechnique (cipherTechnique):
    if cipherTechnique == 'Caesar':
        return CaesarCipherUtil.CaesarCipherUtil
    else:
        raise NotImplementedError (cipherTechnique + ' not implemented' )