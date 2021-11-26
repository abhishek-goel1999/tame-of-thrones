import unittest

from main.models.Kingdom import Kingdom
from main.utils.DataLoadFactory import DataLoaderFactory


class TestDataLoaderFactory(unittest.TestCase):

    __KINGDOM_CSV_FILE = 'kingdoms.csv'

    def testReturnCorrectDict(self):
        """
        Should Load Correct Data and return
        """
        correctData = [
            Kingdom('SPACE', 'Gorilla'),
            Kingdom('LAND', 'Panda'),
            Kingdom('WATER', 'Octopus'),
            Kingdom('ICE', 'Mammoth'),
            Kingdom('AIR', 'Owl'),
            Kingdom('FIRE', 'Dragon'),
        ]

        dataLoader = DataLoaderFactory().getDataLoader('csv')

        resultData = dataLoader(self.__KINGDOM_CSV_FILE)

        self.assertEqual(correctData, resultData)