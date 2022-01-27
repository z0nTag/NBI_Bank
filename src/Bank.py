
import datetime
import json


def timestamp():
    dt = datetime.datetime
    return dt.timestamp(dt.now())


def make_transaction(pers, amount):
    #write transaction
    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

        transactions = jsonObject["transactions"]
        keys = transactions.keys()

        idd = str(len(transactions) + 1)
        jsonObject["transactions"][idd] = (pers, amount, timestamp())

#    with open("bank.json", "w") as jsonFile:
#        json.dump(jsonObject, jsonFile)
#        jsonFile.close()

