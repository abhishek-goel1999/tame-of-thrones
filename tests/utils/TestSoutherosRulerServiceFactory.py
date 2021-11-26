
import unittest

from main.services.SoutherosRulerServices import *
from main.utils.SoutherosRulerServiceFactory import getSoutherosRulerService


class TestSoutherosRulerServiceFactory(unittest.TestCase):
    def testReturnMessagesService(self):
        """
        Check if factory returns correct instance
        """
        service = getSoutherosRulerService('messages')()

        self.assertIsInstance(
            service, SoutherosRulerByMessagesService.
            SoutherosRulerByMessagesService)