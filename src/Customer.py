
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


def saldo(pers):

    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    account = jsonObject["account"]
    #customer = jsonObject["customer"]
    transactions = jsonObject["transactions"]

    keys = account.keys()

    for key in keys:
        print(key)

        for value in account[key].values():
            print(value)
            if value == pers:
                print("Saldo: ", account[key]["saldo"], sep='')
                return True

    return False


def add_customer(name, pers):

    with open("bank.json", "w") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    #idd = str(len(customer) + 1)

    print(type(idd))
    print(jsonObject)
    jsonObject["customer"][idd]["name"] = name
    jsonObject["customer"][idd]["pers"] = pers
    jsonObject["customer"][idd]["accounts"] = 123

