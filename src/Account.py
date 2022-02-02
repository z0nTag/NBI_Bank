
import json
import Datasource as d


class Account:

    def __init__(self, id, balance, type, customer):
        self.id = id
        self.balance = balance
        self.type = type
        self.customer = customer


def balance(pers):

    bank = d.read_json()
    account = bank["account"]
    keys = account.keys()
    found = 0
    for key in keys:
        value = account[key]["customer"]
        if value == pers:
            print("Account: ", key, " Balance: ", account[key]["balance"], sep='')
            found = 1

    if found == 1:
        return True
    else:
        return False


def close_account(account_number):

    bank = d.read_json()
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

    try:
        bank = d.read_json()
        account = bank["account"]

        account[new_account] = {"balance": 0, "type": "deb", "customer": pers}

        d.write_json(bank)
        return True
    except Exception as e:
        print("error: ", e)
        return False
