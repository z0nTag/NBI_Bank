import datetime
import json
import Customer as c
import Account as a
import Bank as b
import Transactions as t
import numpy as np


def read_json():
    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    return jsonObject


print("Welcome to The Best Bank. Please make a choice", end='\n')

while True:

    try:
        print("1. Create new customer  2. Open account for existing customer  3. Check balance 4. Make a transaction 5. View all transactions 6. Close account 7. Delete customer 0. Exit")
        choice = int(input("Enter choice: "))
    except ValueError as e:
        print("Only numbers accepted. Please enter a number\n")
        continue

    if choice == 0:
        break

    elif choice == 1:
        jsonObject = read_json()
        customers = jsonObject["customers"]
        account = jsonObject["account"]

        name = input("Please enter name: ")
        try:
            pers = int(input("Please enter ss-number: "))
        except ValueError as e:
            print("Only numbers accepted\n")
            continue

        for values in customers.values():
            for var in values.values():
                if var == pers:
                    print("Customer already exists")
                    continue

            oc = input("Would you like to open a bank account? Press y for Yes ")
            if oc.lower() == "y":
                print("y worked")
                new_account = [len(account) + 1]
                #create an account

            else:
                account = []

            trans = []
            #c.add_customer(name, pers, account, trans)

    elif choice == 3:

        while True:
            try:
                pers = int(input("Enter your ss-number: "))
                if a.saldo(pers):
                    print("found")
                else:
                    print("Customer not found")
                    break
            except ValueError as e:
                print("Only numbers accepted. Please enter a number\n")
                continue
            break

    elif choice == 4:
        jsonObject = read_json()
        accounts = jsonObject["account"]
        keys = accounts.keys()

        while True:
            try:
                account = int(input("Enter account number: "))
                withdraw = int(input("Enter amount to withdraw: "))
            except ValueError as e:
                print("Only numbers accepted", end='\n')
                continue

            for key in keys:

                if key == str(account):
                    balance = accounts[key]["saldo"]
                    if balance >= withdraw:
                        balance -= withdraw
                        print("Withdraw made, now ", balance, " left", sep='')
                        break
                    else:
                        print("Account found but now enough funds")
                    break
                else:
                    print("Account not found")
                break
            break
#if c.add_customer("Kalle", 801016):
 #   print("Customer created with success")
#else:
 #   print("Error creating customer")
#exit()





