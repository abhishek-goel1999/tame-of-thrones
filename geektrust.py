import sys 

from main.controllers.SoutherosRulerController import SoutherosRulerController

def main():
    #declare instance of the controller and pass i/p file path return o/p 

    rulerController = SoutherosRulerController()

    inputPath = sys.argv[1]

    checkRulerRes = rulerController.checkIfKingdomIsRuler('SPACE',inputPath)

    print(checkRulerRes)

if __name__ == '__main__':
    main()