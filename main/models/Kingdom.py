#Data model for any kingdom
from globals.configs import CipherTechnique
from main.utils.CipherFactory import getCipherTechnique

class Kingdom:
    def __init__(self, name: str, emblem: str, allies= []):
        self.__name = name
        self.__emblem = emblem
        self.__cipher = getCipherTechnique(CipherTechnique)()
        self.__allies = allies

    def send_message(self,)