import unittest
from unittest.mock import patch

from main.models.Kingdom import Kingdom
from main.RepositoryServices.KingdomRepositoryServices import KingdomRepositoryCsvService
from main.services.SoutherosRulerServices.SoutherosRulerByMessagesService import SoutherosRulerByMessagesService


class TestSoutherosRulerByMessagesService(unittest.TestCase):
    def getKingdoms(self):
        """
        Helper Function to return Kingdoms Dictionary
        """

        return {
            'TheGeekTrustKingdom': Kingdom('TheGeekTrustKingdom', 'Knight'),
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'JUNGLE': Kingdom('JUNGLE', 'Elephant'),
            'SEA': Kingdom('SEA', 'Shark')
        }

    @patch.object(KingdomRepositoryCsvService, 'getAllKingdoms')
    def testReturnRuler(self, mockedGetAllKingdoms):
        """
        Should return correct Ruler Object for correct messages
        """

        mockedGetAllKingdoms.return_value = self.getKingdoms()

        correctRuler = Kingdom('TheGeekTrustKingdom', 'Knight', [
            Kingdom('SPACE', 'Gorilla'),
            Kingdom('JUNGLE', 'Elephant'),
            Kingdom('SEA', 'Shark')
        ])

        messages = {
            'SPACE': {'smzsNmpkvhmkzy'},
            'JUNGLE': {'popMinlavmxgbtb'},
            'SEA': {'pifxfXffxomkfw'}
        }

        resultRuler = SoutherosRulerByMessagesService(
        ).checkSoutherosRuler('TheGeekTrustKingdom', messages)

        self.assertEqual(correctRuler, resultRuler)

    @patch.object(KingdomRepositoryCsvService, 'getAllKingdoms')
    def testReturnNone(self, mockedGetAllKingdoms):
        """
        Should return None for incorrect messages or less suppourt
        """

        mockedGetAllKingdoms.return_value = self.getKingdoms()

        correctRuler = None

        messages = {
            'SPACE': {'smzsfsdafkssvhmkzy'},
            'JUNGLE': {'popvlzdddjkclxgbtb'},
            'SEA': {'pif'}
        }

        resultRuler = SoutherosRulerByMessagesService(
        ).checkSoutherosRuler('TheGeekTrustKingdom', messages)

        self.assertEqual(correctRuler, resultRuler)