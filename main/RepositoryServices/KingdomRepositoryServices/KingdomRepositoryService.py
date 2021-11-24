import abc

from main.models.Kingdom import Kingdom

class KingdomRepositoryService(metaclass=abc.ABCMeta):

    """
    Kingdom Repository Service Interface to build any Repository Services
    """

    @abc.abstractmethod
    def getAllKingdoms(self) -> dict:

        """
        Get Kingdoms from the Data Repository
        return Dictionary(key: Kingdom Name, value: Kingdom Object)
        """

        pass