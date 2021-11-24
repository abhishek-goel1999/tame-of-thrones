import os

from globals.config import RulerCheckingCondition
from main.utils.MessageFileReader import readMessagesFromFile
from main.utils.SoutherosRulerServiceFactory import getSoutherosRulerService

class SoutherosRulerController:
    def __init__(self):
        """
        Initialize Controller object with a Service Object
        """
        self.__southerosRulerService = getSoutherosRulerService(
            RulerCheckingCondition)()

    def checkIfKingdomIsRuler(self, kingdomName:str, filePath: str) -> str:
        """
        Controller to accept the request
        - Uses Message Reading util to read messages
        - Uses service to find the output
        - Returns in the Suitable format
        : file_path : Absolute path to the input file 
        """

        if not os.path.isfile(filePath):
            raise FileNotFoundError('"' + filePath + '" is not a valid path')

        messages = readMessagesFromFile(filePath)

        ruler = self.__southerosRulerService.checkRulerOfSoutheros(
            kingdomName, messages)

        if ruler == None:
            return "NONE"
        else:
            return str(ruler)