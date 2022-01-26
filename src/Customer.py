
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
    customers = jsonObject["customers"]
    transactions = jsonObject["transactions"]

    keys = customers.keys()
    for key in keys:

        for var in customers[key]:

            if var == pers:
                print("yes")
                return True
    return False


def add_customer(name, pers, account, trans):

    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

        customers = jsonObject["customers"]
        keys = customers.keys()
        for key in keys:

            for value in customers[key].values():

                if value == pers:
                    print("Customer with that ss already exists")
                    return False

        print("Grats ", name, " account created", sep='')

#        idd = str(len(customers) + 1)
#
        #jsonObject["customer"][idd] = {"name": "Pelle", "pers": 771016, "accounts": [], "trans": []}

#    with open("bank.json", "w") as jsonFile:
#        json.dump(jsonObject, jsonFile)
#        jsonFile.close()

    return True



