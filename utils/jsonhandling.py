import json


def jsonData(path):
    with open(path) as data:
            formattedData = json.load(data)
            return formattedData