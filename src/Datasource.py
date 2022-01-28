
import json


class Datasource:

    def __init__(self, TBD):
        self.TBD = TBD


def read_json():

    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    return jsonObject

