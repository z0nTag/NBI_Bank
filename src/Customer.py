
import json
import datetime


class Customer:

    def __init__(self, bank):
        self.bank = bank


def check(pers):

    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    account = jsonObject["account"]
    customer = jsonObject["customer"]
    transactions = jsonObject["transactions"]

    keys = customer.keys()
    for key in keys:

        for var in customer[key]:

            if var == pers:
                print("yes")
                return True
    return False


def add_customer(name, pers):

    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)

        customer = jsonObject["customer"]
        idd = str(len(customer) + 1)

        jsonObject["customer"][idd]["name"] = name
        jsonObject["customer"][idd]["pers"] = pers
        jsonObject["customer"][idd]["accounts"] = 123
        #json.dump(jsonObject, jsonFile)

        return True



