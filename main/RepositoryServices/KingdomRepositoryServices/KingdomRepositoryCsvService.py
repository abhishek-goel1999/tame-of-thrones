from globals.config import DataLoadingSource, KingdomCsvPath
from main.RepositoryServices.KingdomRepositoryServices.KingdomRepositoryService import KingdomRepositoryService
from main.utils.DataLoadFactory import DataLoaderFactory

class KingdomRepositoryCsvService(KingdomRepositoryService):
    """
    Kingdom Repository Service to get Kingdom Data from CSV file
    """
    def __init__(self):
        """
        Initialize Object by loading repository information
        """

        self.__dataLoader = DataLoaderFactory().getDataLoader(
            DataLoadingSource)

    def getAllKingdoms(self):
        """
        Return Dictionary of Kingdoms loaded from csv file
        """

        kingdomArr = self.__dataLoader(KingdomCsvPath)
        kingdomData = dict(
            (kingdom.getName(), kingdom) for kingdom in kingdomArr)

        return kingdomData