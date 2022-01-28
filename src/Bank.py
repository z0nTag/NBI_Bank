
import datetime
import json
import Datasource as d


def timestamp():
    dt = datetime.datetime
    return dt.timestamp(dt.now())


def make_transaction(pers, amount, account):

    try:
        bank = d.read_json()
        transactions = bank["transactions"]
        f_account = bank["account"]
        print("f_account: ", f_account)
        idd = str(len(transactions) + 1)
        print("idd: ", idd)
        transactions[idd] = (pers, amount, timestamp())
        balance = f_account[account]["balance"]
        print("balance: ", balance)
        new_balance = balance + amount
        f_account[account]["balance"] = new_balance
        print(new_balance)
        print(bank["transactions"][idd])
        d.write_json(bank)
        return True
    except Exception as e:
        print("Error making transaction: ", e, sep=' ')
        return False


