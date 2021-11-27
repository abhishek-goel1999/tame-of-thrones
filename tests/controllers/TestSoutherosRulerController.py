import unittest
from unittest.mock import patch

from main.models.Kingdom import Kingdom
from main.controllers.SoutherosRulerController import SoutherosRulerController
from main.services.SoutherosRulerServices.SoutherosRulerByMessagesService import SoutherosRulerByMessagesService


class TestSoutherosRulerController(unittest.TestCase):

    __CORRECT_MESSAGES_FILE_PATH = 'tests/resources/Controllers/CorrectMessages.txt'
    __INCORRECT_MESSAGES_FILE_PATH = 'tests/resources/Controllers/IncorrectMessages.txt'
    __INCORRECT_FILE_PATH = 'tests/resources/Controllers/IncotMessages.txt'

    @patch.object(SoutherosRulerByMessagesService,
                  'checkSoutherosRuler')
    def testReturnAllies(self, mockedCheckRuler):
        """
        Controller Should return a RulerKingdom and Allies Output for the correct input
        """

        mockedCheckRuler.return_value = Kingdom('TheGeekTrustKingdom', 'TameOfThrones', [
                Kingdom('SPACE', 'Gorilla'),
                Kingdom('JUNGLE', 'Elephant'),
                Kingdom('SEA', 'Shark')
            ])

        messages = {
            'SPACE': {'smzsNmpkvhmkzy'},
            'JUNGLE': {'popMinlavmxgbtb'},
            'SEA': {'pifxfXffxomkfw'}
        }

        correct_output = 'TheGeekTrustKingdom SPACE JUNGLE SEA'

        result_output = SoutherosRulerController(
        ).checkIfKingdomIsRuler(
            'TheGeekTrustKingdom', self.__CORRECT_MESSAGES_FILE_PATH)

        mockedCheckRuler.assert_called_with('TheGeekTrustKingdom', messages)
        self.assertEqual(correct_output, result_output)

    @patch.object(SoutherosRulerByMessagesService,
                  'checkSoutherosRuler')
    def testReturnNone(self, mockedCheckRuler):
        """
        Should return NONE for incorrect messages
        """

        mockedCheckRuler.return_value = None

        messages = {
            'SPACE': {'smzsFDSmkzy'},
            'JUNGLE': {'popMiSDFASxgbtb'},
            'SEA': {'pifx'}
        }

        correct_output = 'NONE'

        result_output = SoutherosRulerController(
        ).checkIfKingdomIsRuler(
            'TheGeekTrustKingdom', self.__INCORRECT_MESSAGES_FILE_PATH)

        mockedCheckRuler.assert_called_with('TheGeekTrustKingdom', messages)
        self.assertEqual(correct_output, result_output)

    def testRaiseFileNotFoundError(self):
        """
        Should Raise FileNotFound Error for incorrect file path
        """

        with self.assertRaises(FileNotFoundError):
            SoutherosRulerController(
            ).checkIfKingdomIsRuler(
                'TheGeekTrustKingdom', self.__INCORRECT_FILE_PATH)