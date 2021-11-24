import csv
import os

from globals.config import ResourceDirectory
from main.models.Kingdom import Kingdom

class DataLoaderFactory:
    """factory class to generate data loaders"""
    def getDataLoader(self, sourceType):
        if sourceType == "csv":
            return _loadCsvData
        else:
            raise NotImplementedError('Data Loader with source type "' +
                                      sourceType + '" not implemented')


def _loadCsvData(kingdomCsvPath: str):
    """
    Loads Data given in the input csv file present in the resources folder
    The Format:
        Kingdom Name, Kingdom Emblem
    """

    filePath = os.getcwd() + "/" + ResourceDirectory + "/" + kingdomCsvPath

    kingdomArr = []

    with open(filePath, newline="") as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        for row in reader:
            kingdomArr.append(Kingdom(row[0], row[1]))

    return kingdomArr