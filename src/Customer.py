
import json
import datetime


class Customer:

    def __init__(self, bank):
        self.bank = bank


with open("bank.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

account = jsonObject["account"]
customer = jsonObject["customer"]
transactions = jsonObject["transactions"]


def check(pers):

    keys = customer.keys()
    for key in keys:

        for var in customer[key]:

            if var == pers:
                print("yes")
                return True
    return False


def saldo(pers):

    keys = account.keys()
    size = len(account) + 1
    print("len: ", size, sep='')
    for key in keys:
        print(key)

        for value in account[key].values():
            print(value)
            if value == pers:
                print("Saldo: ", account[key]["saldo"], sep='')
                return True

    return False

def add_customer(name, pers):

    id = len(customer) + 1


