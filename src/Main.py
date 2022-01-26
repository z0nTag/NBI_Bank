import datetime
import json
import Customer as c
import Account as a
import Bank as b

import Transactions as t

import numpy as np



#if c.check(pers):
 #   print("found")
#else:
 #   print("not found")


while True:

    try:
        pers = int(input("Enter number: "))
        if c.saldo(pers):
            print("found")
        else:
            print("not found")
    except ValueError as e:
        print("Only numbers accepted. Please enter a number\n")
        continue
    break







