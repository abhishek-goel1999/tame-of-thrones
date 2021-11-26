import unittest

from main.utils.CipherFactory import getCipherTechnique
from main.utils.cipherSystem import *


class TestCipherFactory(unittest.TestCase):

    __CIPHER_TECHNIQUE = 'Caesar'

    def setUp(self):
        self.resultCipher = getCipherTechnique(self.__CIPHER_TECHNIQUE)()

    def testReturnCaesarCipher(self):
        """
        Check if the factory returns correct object
        """
        self.assertIsInstance(self.resultCipher,
                              CaesarCipherUtil.CaesarCipherUtil)

    def testEncryptPlainText(self):
        """
        Cipher should encrypt all the Plain Texts and return Cipher Texts
        """
        plainTextAndKeyArray = [('HELLO', 3), ('Random Tales', 7),
                                  ('tHeMaAroOnKnIgHt', 2), ('Cosmos', 1),
                                  ('abcdefgh', 4)]
        CorrectCipherTextArr = [
            'KHOOR', 'Yhukvt Ahslz', 'vJgOcCtqQpMpKiJv', 'Dptnpt', 'efghijkl'
        ]

        resultCipherTextArr = []

        for plainText, key in plainTextAndKeyArray:
            resultCipherTextArr.append(
                self.resultCipher.encrypt(plainText, key))

        self.assertEqual(CorrectCipherTextArr, resultCipherTextArr)

    def TestDecryptCipherText(self):
        """
        Cipher should decrypt all the Cipher Texts and return Plain Texts
        """

        cipherTextKeyArr = [('KHOOR', 3), ('Yhukvt Ahslz', 7),
                                   ('vJgOcCtqQpMpKiJv', 2), ('Dptnpt', 1),
                                   ('efghijkl', 4)]
        correctPlainTextArr = [
            'HELLO', 'Random Tales', 'tHeMaAroOnKnIgHt', 'Cosmos', 'abcdefgh'
        ]

        resultPlainTextArr = []

        for cipherText, key in cipherTextKeyArr:
            resultPlainTextArr.append(
                self.resultCipher.decrypt(cipherText, key))

        self.assertEqual(correctPlainTextArr, resultPlainTextArr)