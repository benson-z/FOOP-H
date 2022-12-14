import json

def importData(fileName):
    try:
        f = open(fileName)
        data = json.load(f)
        f.close()
        return data
    except:
        return {"people": {}}

def saveData(fileName, data):
    f = open(fileName, "w")
    formattedData = json.dumps(data, sort_keys=True, indent=4)
    f.write(formattedData)
    f.close()