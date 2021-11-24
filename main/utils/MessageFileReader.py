def readMessagesFromFile(filePath):
    msgDict = {}
    with open(filePath) as file:
        try:
            for line in file:
                lineArr = line.strip().split()
                kingdomName = lineArr[0]
                message = ' '.join(lineArr[1:])

                if not kingdomName in msgDict:
                    msgDict[kingdomName] = set()
                    msgDict[kingdomName].add(message)
        
        except:
            raise IOError(
                "Input format not in correct format."
            )
    return msgDict
