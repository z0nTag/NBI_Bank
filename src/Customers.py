
import json
import Datasource as d
import datetime


class Customers:

    def __init__(self, id, name, pers, accounts, trans):
        self.id = id
        self.name = name
        self.pers = pers
        self.accounts = accounts
        self.trans = trans


def check(pers):

    bank = d.read_json()
    account = bank["account"]
    customers = bank["customers"]
    transactions = bank["transactions"]

    keys = customers.keys()
    for key in keys:

        for var in customers[key]:

            if var == pers:
                print("yes")
                return True
    return False


def print_all_customers():

    bank = d.read_json()
    customers = bank["customers"]
    keys = customers.keys()

    for key in keys:
        print("\nCustomer number: ", key, sep='')
        for var in customers[key]:
            print(var, customers[key][var], sep=': ')


def add_customer(name, pers, account):

    bank = d.read_json()
    customers = bank["customers"]
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



