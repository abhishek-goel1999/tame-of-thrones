from main.RepositoryServices import KingdomRepositoryServices
from main.RepositoryServices.KingdomRepositoryServices import *

def getKingdomRepositoryService(SourceType):
    """Returns Kingdom Repository Service
    Source Type: Type of repository source"""

    if SourceType == "csv":
        return KingdomRepositoryCsvService.KingdomRepositoryCsvService
    
    else:
        raise NotImplementedError(
            'Kingdom repository service not implemented for "' + SourceType + " source type"
        )