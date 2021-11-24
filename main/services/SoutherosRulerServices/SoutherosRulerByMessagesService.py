from globals.config import DataLoadingSource
from main.models.Kingdom import Kingdom
from main.services.SoutherosRulerServices.SoutherosRulerService import SoutherosRulerService
from main.utils.KingdomRepositoryServiceFactory import getKingdomRepositoryService

class SoutherosRulerByMessagesService(SoutherosRulerService):
    """Service to check if a kingdom can be a ruler of southeros by sending msgs and find how many allies"""


    def __init__(self):
        """
        Initialize object by getting the Repository Service Object
        """

        self.__kingdomRepositoryService = getKingdomRepositoryService(
            DataLoadingSource)()

    def checkSoutherosRuler(self, currKingdomName: str,
                                 messages: dict) -> Kingdom:
        """
        Send messages to all the kingdoms and check the allies
        Return Kingdom for the current kingdom if it is the Ruler else send None
        """

        kingdoms = self.__kingdomRepositoryService.getAllKingdoms()

        currKingdom = kingdoms[currKingdomName]

        currKingdom.evaluateAllies(kingdoms, messages)

        if len(currKingdom.getAllies()) >= 3:
            return currKingdom
        else:
            return None