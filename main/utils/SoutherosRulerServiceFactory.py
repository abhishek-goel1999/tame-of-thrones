from main.services.SoutherosRulerServices import *

def getSoutherosRulerService(conditionType):
    """returns southeros ruler service 
        ConditionType: condition to be used (eg: messages)"""

    if conditionType == "messages":
        return SoutherosRulerByMessagesService.SoutherosRulerByMessagesService
    
    else:
        raise NotImplementedError(
            'Southeros ruler service with condition type "' + conditionType + '" not implemented'
        )
