import csv
import os
import unittest
from unittest.mock import patch

from main.models.Kingdom import Kingdom
from main.RepositoryServices.KingdomRepositoryServices.KingdomRepositoryCsvService import KingdomRepositoryCsvService
from main.utils.DataLoadFactory import DataLoaderFactory

KINGDOM_CSV_PATH = 'tests/resources/Kingdoms.csv'


def mockDataLoader(csv_path):
    """
    Mock Data loader that loads Data from our testing Repository
    """
    filePath = KINGDOM_CSV_PATH

    kingdomArr = []

    with open(filePath, newline="") as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        for row in reader:
            kingdomArr.append(Kingdom(row[0], row[1]))

    return kingdomArr


class TestKingdomRepositoryCsvService(unittest.TestCase):
    @patch.object(DataLoaderFactory, 'getDataLoader')
    def testReturnCorrectData(self, mockedDataLoader):
        """
        Check if the repository returns correct data
        """

        mockedDataLoader.return_value = mockDataLoader

        correctKingdoms = {
            'SPACE': Kingdom('SPACE', 'Gorilla'),
            'LAND': Kingdom('LAND', 'Panda'),
            'WATER': Kingdom('WATER', 'Octopus'),
            'ICE': Kingdom('ICE', 'Mammoth'),
            'AIR': Kingdom('AIR', 'Owl'),
            'FIRE': Kingdom('FIRE', 'Dragon')
        }

        resultKingdoms = KingdomRepositoryCsvService().getAllKingdoms()

        for i in correctKingdoms:

            self.assertEqual(correctKingdoms[i], resultKingdoms[i])