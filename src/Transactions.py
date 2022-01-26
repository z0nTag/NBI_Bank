

import json
import datetime


class Transactions:

    def __init__(self, bank):
        self.bank = bank


account = dict  # id: [#balance, #type, #customer]
customers = dict  # id: [#name, #pers, #accounts[], #transactions[]]
trans = dict  # id: (#account, #diff, #timestamp)

bank = {account, customers, trans}  # master

account = {1: [111, "deb", 11], 2: [222, "deb", 22]}
customers = {11: ["Jonas", 801016, [1, 2], [1, 2, 3]]}

dt = datetime.datetime.now()
trans = {
    1: (1, 200, datetime.datetime.timestamp(dt)),
    2: (1, 100, datetime.datetime.timestamp(dt)),
    3: (1, -50, datetime.datetime.timestamp(dt))
}
bank = [account, customers, trans]

# print(bank)




def check(pers):
    for test in bank[1]:

        for var in bank[1][test]:
            if var == pers:
                print("yes")
                return True
        return False


def saldo(pers):

    for cust in bank[1]:

        for var in bank[1][cust]:
            if var == pers:
                print(bank[1][cust][0])
                accounts = bank[1][cust][2]
                print(accounts)

                for saldot in accounts:
                    print(bank[0][saldot][0])

                return True
        return False


