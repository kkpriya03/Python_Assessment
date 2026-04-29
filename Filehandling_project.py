"""
BANKING LEDGER SYSTEM

Customer (CID, Name, Mobile)
Account  (ACC_NO, CID, Balance)
Transaction (ACC_NO, Type, Amount)

1- Add Customer
2- View Customers
3- Delete Customers
4- Open Account
5- View Accounts
6- Delete Accounts
7- Deposit Money
8- Withdraw Money
9- View Transactions
0- Exit

"""


import pickle
import os

# ---------------- CUSTOMER ----------------
def addCustomer():
    file = open('customer.bin','ab')
    cid = input("\n\tEnter Customer ID: ")
    name = input("\tEnter Name: ")
    mob = input("\tEnter Mobile: ")

    pickle.dump(cid,file)
    pickle.dump(name,file)
    pickle.dump(mob,file)

    file.close()
    print("\tCustomer Added Successfully!")
    input("\tPress Enter To Continue...") 

def viewCustomer():
    file = open('customer.bin','rb')
    found = False

    try:
        while True:
            cid = pickle.load(file)
            name = pickle.load(file)
            mob = pickle.load(file)

            found = True

            print("\n\tCustomer ID:", cid)
            print("\tName:", name)
            print("\tMobile:", mob)
            print("\t----------------------")

    except EOFError:
        if found:
            print("\tAll Customer Data Displayed Successfully!")
        else:
            print("\tNo Customer Data Found!")

    file.close()
    input("\tPress Enter To Continue...")

def deleteCustomer():
    file1 = open('customer.bin','rb')
    file2 = open('temp.bin','ab')

    cid = input("\n\tEnter Customer ID To Delete: ")
    found = 0

    try:
        while True:
            c = pickle.load(file1)
            name = pickle.load(file1)
            mob = pickle.load(file1)

            if c == cid:
                print("\tCustomer Name:", name)
                found = 1
            else:
                pickle.dump(c, file2)
                pickle.dump(name, file2)
                pickle.dump(mob, file2)

    except:
        pass

    file1.close()
    file2.close()

    os.remove('customer.bin')
    os.rename('temp.bin','customer.bin')

    if found:
        print("\n\tCustomer Deleted Successfully!")
    else:
        print("\n\tCustomer Not Found!")

    input("\tPress Enter To Continue...")    

# ---------------- ACCOUNT ----------------
def openAccount():
    acc = input("\n\tEnter Account No: ")
    cid = input("\tEnter Customer ID: ")
    bal = input("\tEnter Initial Balance: ")

    found = False

    try:
        file = open('account.bin','rb')

        while True:
            a = pickle.load(file)
            pickle.load(file)
            pickle.load(file)

            if a == acc:
                found = True
                break

        file.close()

    except:
        pass

    if found:
        print("\tAccount Already Exists!")
    else:
        file = open('account.bin','ab')
        pickle.dump(acc,file)
        pickle.dump(cid,file)
        pickle.dump(bal,file)
        file.close()

        print("\tAccount Created!")

    input("\tPress Enter To Continue...")

def viewAccount():
    file = open('account.bin','rb')
    try:
        while True:
            print("\n\tAcc No:",pickle.load(file))
            print("\tCustomer ID:",pickle.load(file))
            print("\tBalance:",pickle.load(file))
            print("\t----------------------")
    except:
        pass
    file.close()
    input("\tPress Enter To Continue...")

def deleteAccount():
    file1 = open('account.bin','rb')
    file2 = open('temp.bin','ab')

    acc = input("\n\tEnter Account No To Delete: ")
    found = 0

    try:
        while True:
            a = pickle.load(file1)
            cid = pickle.load(file1)
            bal = pickle.load(file1)

            if a == acc:
                print("\tAccount Found - Balance:", bal)
                found = 1
            else:
                pickle.dump(a, file2)
                pickle.dump(cid, file2)
                pickle.dump(bal, file2)

    except:
        pass

    file1.close()
    file2.close()

    os.remove('account.bin')
    os.rename('temp.bin','account.bin')

    if found:
        print("\n\tAccount Deleted Successfully!")
    else:
        print("\n\tAccount Not Found!")

    input("\tPress Enter To Continue...")

# ---------------- TRANSACTION ----------------
def saveTransaction(acc, ttype, amt):
    file = open('trans.bin','ab')
    pickle.dump(acc,file)
    pickle.dump(ttype,file)
    pickle.dump(amt,file)
    file.close()

def viewTransaction():
    file = open('trans.bin','rb')
    try:
        while True:
            print("\n\tAcc No:",pickle.load(file))
            print("\tType:",pickle.load(file))
            print("\tAmount:",pickle.load(file))
            print("\t----------------------")
    except:
        pass
    file.close()
    input("\tPress Enter To Continue...") 

# ---------------- DEPOSIT ----------------
def deposit():
    file1 = open('account.bin','rb')
    file2 = open('temp.bin','ab')

    acc = input("\n\tEnter Account No: ")
    amt = int(input("\tEnter Amount: "))
    found = 0

    try:
        while True:
            a = pickle.load(file1)
            cid = pickle.load(file1)
            bal = int(pickle.load(file1))

            if a == acc:
                bal += amt
                found = 1
                saveTransaction(acc, "Deposit", amt)

            pickle.dump(a,file2)
            pickle.dump(cid,file2)
            pickle.dump(bal,file2)

    except:
        pass

    file1.close()
    file2.close()

    os.remove('account.bin')
    os.rename('temp.bin','account.bin')

    if found:
        print("\tMoney Deposited Successfully!")
    else:
        print("\tAccount Not Found!")
    input("\tPress Enter To Continue...") 

# ---------------- WITHDRAW ----------------
def withdraw():
    file1 = open('account.bin','rb')
    file2 = open('temp.bin','ab')

    acc = input("\n\tEnter Account No: ")
    amt = int(input("\tEnter Amount: "))
    found = 0

    try:
        while True:
            a = pickle.load(file1)
            cid = pickle.load(file1)
            bal = int(pickle.load(file1))

            if a == acc:
                if bal >= amt:
                    bal -= amt
                    saveTransaction(acc, "Withdraw", amt)
                    print("\tWithdrawal Successful!")
                else:
                    print("\tInsufficient Balance!")
                found = 1

            pickle.dump(a,file2)
            pickle.dump(cid,file2)
            pickle.dump(bal,file2)

    except:
        pass

    file1.close()
    file2.close()

    os.remove('account.bin')
    os.rename('temp.bin','account.bin')

    if not found:
        print("\tAccount Not Found!")
    input("\tPress Enter To Continue...") 

# ---------------- MENU ----------------
while True:
    print("\n\t===== BANKING LEDGER SYSTEM =====")
    print('''
            1- Add Customer
            2- View All Customer
            3- Delete Customers
            4- Open Account
            5- View Accounts
            6- Delete Accounts
            7- Deposit Money
            8- Withdraw Money
            9- View Transactions
            0- Exit
        ''')

    ch = int(input("Enter Choice: "))

    if  ch == 1:
        addCustomer()
    elif ch == 2:
        viewCustomer()
    elif ch == 3:
        deleteCustomer()
    elif ch == 4:
        openAccount()
    elif ch == 5:
        viewAccount()
    elif ch == 6:
        deleteAccount()
    elif ch == 7:
        deposit()
    elif ch == 8:
        withdraw()
    elif ch == 9:
        viewTransaction()
    elif ch == 0:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
