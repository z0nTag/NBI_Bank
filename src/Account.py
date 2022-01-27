
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

        account = jsonObject["account"]
        keys = account.keys()
    return jsonObject, account, keys


def balance(pers):

    account = read_json()[1]
    keys = read_json()[2]

    for key in keys:

        for value in account[key].values():

            if value == pers:
                print("Balance: ", account[key]["balance"], sep='')
                return True

    return False


def close_account(account_number):

    account = read_json()[1]
    keys = read_json()[2]

    for key in keys:
        if key == str(account_number):
            account.pop(key)
            print(account)
            return True
    return False



