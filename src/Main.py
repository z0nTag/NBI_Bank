
import json
import Account as a
import Bank as b
import Customers as c
import Datasource as d

import Transactions as t


print("Welcome to The Best Bank. Please make a choice", end='\n')

while True:

    try:
        print("\n1. Create new customer  2. Open account for existing customer  3. Check balance 4. Make a transaction 5. View all transactions 6. Close account 7. Delete customer 0. Exit 999. View all customers")
        choice = int(input("Enter choice: "))
    except ValueError as e:
        print("Only numbers accepted. Please enter a number\n")
        continue

    if choice == 11:

        test = "json write test"

        if d.write_json(test):
            print("Hurra!")
        else:
            print("Nooooo...:(")

        continue

    elif choice == 0:
        input("Goodbye! Please come again!\n")
        exit()

    elif choice == 1:
        bank = d.read_json()
        customers = bank["customers"]
        account = bank["account"]

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
        if a.open_account(123, 123):
            print("Account created")
        else:
            print("Account could not be created")
        continue

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
        continue

    elif choice == 4:
        bank = d.read_json()
        accounts = bank["account"]
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

                            pers = accounts[key]["customer"]
                            amount -= (amount * 2)
                            if b.make_transaction(pers, amount, str(account)):
                                print("Withdraw made, new balance ", balance, sep='')
                            else:
                                print("Unknown error making transaction")
                            break
                        else:
                            print("Account found but now enough funds")
                        break
                    elif action == 2:
                        balance += amount
                        pers = accounts[key]["customer"]

                        if b.make_transaction(pers, amount, str(account)):
                            print("Deposit made, new balance: ", balance, sep='')
                        else:
                            print("Unknown error making transaction")
                        break
                else:
                    print("Account not found")
                break
            break
        continue
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
        continue
    elif choice == 999:
        c.print_all_customers()
        continue

#if c.add_customer("Kalle", 801016):
 #   print("Customer created with success")
#else:
 #   print("Error creating customer")
#exit()





