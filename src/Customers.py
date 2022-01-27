
import json
import datetime


class Customers:

    def __init__(self, id, name, pers, accounts, trans):
        self.id = id
        self.name = name
        self.pers = pers
        self.accounts = accounts
        self.trans = trans


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


def print_all_customers():

    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
        customers = jsonObject["customers"]
        keys = customers.keys()

        for key in keys:
            print("\nCustomer number: ", key, sep='')
            for var in customers[key]:
                print(var, customers[key][var], sep=': ')


def add_customer(name, pers, account):

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
        #jsonObject["customer"][idd] = {"name": name, "pers": pers, "accounts": account, "trans": []}

#    with open("bank.json", "w") as jsonFile:
#        json.dump(jsonObject, jsonFile)
#        jsonFile.close()

    return True



