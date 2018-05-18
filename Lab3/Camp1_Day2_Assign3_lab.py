import json

def getNumberfromJsonFile():
    file = open("Lab3/ListNumber.json", "r") 
    data = json.load(file)
    StrSequence = data["sequence"]
    TempSequence = StrSequence.split(",")
    print(TempInputSession)
    return TempSequence

if __name__ == '__main__':
    getNumberfromJsonFile()
