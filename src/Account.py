
import json


class Account:

    def __init__(self, id, balance, type, customer):
        self.id = id
        self.balance = balance
        self.type = type
        self.customer = customer


def read_json():
    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    return jsonObject


def balance(pers):

    bank = read_json()
    account = bank["account"]
    keys = account.keys()

    for key in keys:

        for value in account[key].values():

            if value == pers:
                print("Account: ", key, " Balance: ", account[key]["balance"], sep='')

    return False


def close_account(account_number):

    bank = read_json()
    account = bank["account"]
    keys = account.keys()

    for key in keys:
        if key == str(account_number):
            print("Balance: ", account[key]["balance"])
            account.pop(key)
            #remove the account in customer list
            #dump to bank.json
            return True
    return False


def open_account(new_account, pers):

    jsonObject = read_json()[0]
    account = read_json()[1]
    jsonObject["customer"][new_account] = {"balance": 0, "type": "deb", "customer": pers}

#    with open("bank.json", "w") as jsonFile:
#        json.dump(jsonObject, jsonFile)
#        jsonFile.close()
