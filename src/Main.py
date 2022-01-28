import datetime
import json
import Customers as c
import Account as a
import Bank as b
import Transactions as t
import numpy as np


def read_json(): #läser in jsonfil, laddar det till jsonObject/banken, retunerar jsonObject. Kommer läggas i egen klass
    with open("bank.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    return jsonObject


print("Welcome to The Best Bank. Please make a choice", end='\n')

while True:

    try:
        print("\n1. Create new customer  2. Open account for existing customer  3. Check balance 4. Make a transaction 5. View all transactions 6. Close account 7. Delete customer 0. Exit 999. View all customers")
        choice = int(input("Enter choice: "))
    except ValueError as e:
        print("Only numbers accepted. Please enter a number\n")
        continue

    if choice == 0:
        input("Goodbye! Please come again!\n")
        exit()

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
                new_account = [len(account) + 1]
                #create an account
                a.open_account(new_account, pers)

            else:
                account = []

            trans = []
            #c.add_customer(name, pers, account)

    elif choice == 2:
        #a.open_account
        break

    elif choice == 3:

        while True:
            try:
                pers = int(input("Enter your ss-number: "))
                if a.balance(pers):
                    print("found")
                else:
                    print("No accounts found")
                    break
            except ValueError as e:
                print("Only numbers accepted. Please enter a number\n")
                continue
            break

    elif choice == 4:
        jsonObject = read_json()
        accounts = jsonObject["account"]
        keys = accounts.keys()
        action = 0
        while True:
            try:
                account = int(input("Enter account number: "))
                action = int(input("Choose 1. Withdraw or 2. Deposit: "))
                while action != 1 and action != 2:
                    print("Only the number 1 or 2 accepted")
                    action = int(input("Choose 1. Withdraw or 2. Deposit: "))

                amount = int(input("Enter amount: "))
            except ValueError as e:
                print("Only numbers accepted", end='\n')
                continue

            for key in keys:

                if key == str(account):
                    balance = accounts[key]["balance"]

                    if action == 1:
                        if balance >= amount:
                            balance -= amount
                            print("Withdraw made, new balance ", balance, sep='')
                            pers = accounts[key]["customer"]
                            amount -= (amount * 2)
                            b.make_transaction(pers, amount)
                            break
                        else:
                            print("Account found but now enough funds")
                        break
                    elif action == 2:
                        balance += amount
                        print("Deposit made, new balance: ", balance, sep='')
                        pers = accounts[key]["customer"]
                        b.make_transaction(pers, amount)
                        break
                else:
                    print("Account not found")
                break
            break

    elif choice == 6:
        while True:
            try:
                account_number = int(input("Number of account to close: "))
            except ValueError as e:
                print("Only numbers accepted. Please enter a number\n")
                continue

            if a.close_account(account_number):
                print("Account closed")
            else:
                print("Something went wrong closing the account")
            break

    elif choice == 999:
        c.print_all_customers()


#if c.add_customer("Kalle", 801016):
 #   print("Customer created with success")
#else:
 #   print("Error creating customer")
#exit()





