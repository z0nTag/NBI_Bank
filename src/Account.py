
import json

class Account:

    def __init__(self, id, balance, type, customer):
        self.id = id
        self.balance = balance
        self.type = type
        self.customer = customer


def saldo(pers):

    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

        account = jsonObject["account"]
        keys = account.keys()

        for key in keys:

            for value in account[key].values():

                if value == pers:
                    print("Saldo: ", account[key]["saldo"], sep='')
                    return True

    return False

