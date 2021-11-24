#Data model for any kingdom
from globals.config import CipherTechnique
from main.utils.CipherFactory import getCipherTechnique

class Kingdom:
    """model to represent kingdom"""
    def __init__(self, name: str, emblem: str, allies= []):
        self.__name = name
        self.__emblem = emblem
        self.__cipher = getCipherTechnique(CipherTechnique)()
        self.__allies = allies

    def sendMessage(self, recieverKingdom, message: str) -> bool:
        """
        Send Message to the Reciever Kingdom and check if it is an ally
        recieverKingdom : Kingdom Object of the Kingdom to whom message is sent
        message : String message to be sent to the other country
        Returns the response sent by the Reciever Kingdom
        """

        return recieverKingdom.recieveMessage(message)

    def recieveMessage(self, message: str) -> bool:
        """
        Check if the message recived has the emblem after decryption
        : message : Recieved string message
        Returns if the kingdom can ally with the Sender kingdom
        """

        decryptedMessage = self.__cipher.decrypt(message, len(self.__emblem))

        return self.checkEmblemInMessage(decryptedMessage)

    def checkEmblemInMessage(self, message: str) -> bool:
        """
        Checks if all the letters of emblem are presnt in the message
        
        : message : Message recieved
        """

        emblemDict = {}
        for ch in self.__emblem.upper():
            if ch in emblemDict:
                emblemDict[ch] += 1
            else:
                emblemDict[ch] = 1

        for ch in message.upper():
            if ch in emblemDict:
                emblemDict[ch] -= 1
                if emblemDict[ch] == 0:
                    del emblemDict[ch]
        return len(emblemDict) == 0

    def evaluateAllies(self, kingdoms: dict, messages: dict) -> None:

        self.__allies = []

        for kingdomName in messages:
            if kingdomName != self.__name:
                if kingdomName in kingdoms:
                    for message in messages[kingdomName]:
                        if self.sendMessage(kingdoms[kingdomName],
                                                 message):
                            self.__allies.append(kingdoms[kingdomName])
                            break

    def __eq__(self, other):
        """
        Override Equality
        """

        if not type(self) is type(other):
            return False

        if self.__name != other.getName():
            return False
        if self.__emblem != other.getEmblem():
            return False
        return True

    def __str__(self):
        """
        Return String representation of the object
        """
        return self.__name + " " + ' '.join([ally.getName() for ally in self.__allies])

    """
    Getters and Setters
    """

    def getName(self):
        return self.__name

    def getEmblem(self):
        return self.__emblem

    def getAllies(self):
        return self.__allies