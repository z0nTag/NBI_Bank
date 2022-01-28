
import datetime
import json
import Datasource as d


def timestamp():
    dt = datetime.datetime
    return dt.timestamp(dt.now())


def make_transaction(pers, amount):
    #write transaction
        bank = d.read_json()
        transactions = bank["transactions"]
        #keys = transactions.keys()

        idd = str(len(transactions) + 1)
        bank["transactions"][idd] = (pers, amount, timestamp())
        print(bank["transactions"][idd])

#    with open("bank.json", "w") as jsonFile:
#        json.dump(jsonObject, jsonFile)
#        jsonFile.close()

