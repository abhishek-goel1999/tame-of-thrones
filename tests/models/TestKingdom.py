import unittest
from unittest.mock import patch

from main.models.Kingdom import Kingdom
from main.utils.cipherSystem.CaesarCipherUtil import CaesarCipherUtil

class TestKingdom(unittest.TestCase):

    def testCreateCorrectObject(self):
        """
        Should convert to string correctly
        """

        correctString = 'TheGeekTrustKingdom '

        kingdom = Kingdom('TheGeekTrustKingdom', 'Elephant')

        resultString = str(kingdom)

        self.assertEqual(correctString, resultString)

    @patch.object(CaesarCipherUtil, 'decrypt')
    def testReturnAllyForCorrectResponse(self, mockedDecrypt):
        """
        Should return Ally response for the correct response
        """

        mockedDecrypt.return_value = 'elfase phfadsd afadsss dnd ast'

        correctResponse = True

        kingdom = Kingdom('TheGeekTrustKingdom', 'Elephant')
        resultResponse = kingdom.recieveMessage('mtniam xpnilal inilaaa lvl iab')

        mockedDecrypt.assert_called_with('mtniam xpnilal inilaaa lvl iab', 8)
        self.assertEqual(correctResponse, resultResponse)

    @patch.object(CaesarCipherUtil, 'decrypt')
    def testReceiveSupportFromKingdom(self, mockedDecrypt):
        """
        Should recieve ally message when sends correct message
        """

        mockedDecrypt.return_value = 'elfase phfadsd afadsss dnd ast'

        correctResponse = True

        recieverKingdom = Kingdom('TheGeekTrustKingdom', 'Elephant')
        senderKingdom = Kingdom('SPACE', 'Gorilla')
        resultResponse = senderKingdom.sendMessage(recieverKingdom, 'mtniam xpnilal inilaaa lvl iab')

        mockedDecrypt.assert_called_with('mtniam xpnilal inilaaa lvl iab', 8)
        self.assertEqual(correctResponse, resultResponse)

    def testEvaluateRightAllies(self):

        kingdoms = {
            'TheGeekTrustKingdom': Kingdom('TheGeekTrustKingdom', 'Knight'),
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'JUNGLE': Kingdom('JUNGLE', 'Elephant'),
            'SEA': Kingdom('SEA', 'Shark')
        }

        messages = {
            'SPACE': {'smzsNmpkvhmkzy'},
            'JUNGLE': {'popMinlavmxgbtb'},
            'SEA': {'pif'}
        }

        correct_allies = [kingdoms['SPACE'], kingdoms['JUNGLE']]

        kingdom = Kingdom('TheGeekTrustKingdom', 'Knight')

        kingdom.evaluateAllies(kingdoms, messages)

        result_allies = kingdom.getAllies()

        self.assertEqual(correct_allies, result_allies)