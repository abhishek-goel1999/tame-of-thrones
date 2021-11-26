
import unittest

from main.RepositoryServices.KingdomRepositoryServices import *
from main.utils.KingdomRepositoryServiceFactory import getKingdomRepositoryService


class TestKingdomRepositoryServiceFactory(unittest.TestCase):
    def testReturnCsvService(self):
        """
        Check if factory returns correct instance
        """
        service = getKingdomRepositoryService('csv')()

        self.assertIsInstance(
            service,
            KingdomRepositoryCsvService.KingdomRepositoryCsvService)