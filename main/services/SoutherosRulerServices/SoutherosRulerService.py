import abc

from main.models.Kingdom import Kingdom

class SoutherosRulerService (metaclass = abc.ABCMeta):
    """service interface to build services in future"""
    @abc.abstractmethod
    def checkSoutherosRuler(self, currentKingdomName: str, messages: dict) -> Kingdom:
        """logic and return kingdom object"""
        pass