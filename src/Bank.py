
import datetime
import json
import Datasource as d
from Customers import Customers

def timestamp():
    dt = datetime.datetime
    return dt.timestamp(dt.now())


def make_transaction(pers, amount, account):

    try:
        bank = d.read_json()
        transactions = bank["transactions"]
        f_account = bank["account"]
        customers = bank["customers"]

        idd = str(len(transactions) + 1)

        transactions[idd] = (pers, amount, timestamp())
        balance = f_account[account]["balance"]

        new_balance = balance + amount
        f_account[account]["balance"] = new_balance

        keys = customers.keys()
        for key in keys:
            value = customers[key]["pers"]

            if value == pers:
                customers[key]["trans"].append(int(idd))

        d.write_json(bank)

        return True
    except Exception as e:
        print("Error making transaction: ", e, sep=' ')
        return False


def new_customer(id, name, pers, account, trans):
    return Customers(id, name, pers, account, trans)

