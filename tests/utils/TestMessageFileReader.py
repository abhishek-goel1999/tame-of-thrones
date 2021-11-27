import unittest

from main.utils.MessageFileReader import readMessagesFromFile


class TestMessageFileReader(unittest.TestCase):

    __CORRECT_FORMAT_FILE_PATH = 'E:/projects/tame-of-thrones/tests/resources/MessageFileReader/CorrectInputFormat.txt'
    __INCORRECT_FORMAT_FILE_PATH = 'E:/projects/tame-of-thrones/tests/resources/MessageFileReader/IncorrectInputFormat.txt'

    def testGenerateMessageDict(self):
        """
        Should read and generate correcct message dictionary
        """
        correctMessages = {
            'LAND': {'FAIJWJSOOFAMAU'},
            'ICE': {'STHSTSTVSASOS'},
            'FIRE': {'JXGOOMUTOO'}
        }

        resultMessages = readMessagesFromFile(
            self.__CORRECT_FORMAT_FILE_PATH)

        self.assertDictEqual(correctMessages, resultMessages)

    def testRaiseIOError(self):
        """
        Should Raise IOError
        """
        with self.assertRaises(IOError):
            readMessagesFromFile(self.__INCORRECT_FORMAT_FILE_PATH)