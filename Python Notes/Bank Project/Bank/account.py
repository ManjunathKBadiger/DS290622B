import random
dict_account = {}


def create_account(uname, pwd):
    dict_account[uname] = {}
    dict_account[uname][uname] = pwd
    print("Account created successfully!....")
    account_number = str(round(random.random(), 10))[2:]
    pin_number = str(round(random.random(), 4))[2:]
    dict_account[uname]["account_number"] = account_number
    dict_account[uname]["balance"] = 0.0
    dict_account[uname]["pin"] = pin_number
    # print("Account number is ",account_number)
    print("pin number is ",pin_number)


def transaction(uname, pin):
    if dict_account[uname]["pin"] == pin:
        amount = float(input("Enter a amount to withdraw: "))
        balance = dict_account[uname]["balance"]
        if balance > amount:
            print("Balance is ", (balance-amount))
            balance = dict_account[uname]["balance"]
            dict_account[uname]["balance"] = balance - amount
        else:
            print("Your balance is ", balance)
    else:
        print("Entered Pin is wrong")

def add_balance(uname):
        amount = float(input("Enter a amount to Add: "))
        balance = dict_account[uname]["balance"]
        dict_account[uname]["balance"] = balance + amount

def login(uname, pwd):
    if uname in dict_account and dict_account[uname][uname] == pwd:
        print("User exist Welcome ")
        return True
    else:
        print("User Does not exist Please create account ")
        return False

def view_balance(uname):
    balance = dict_account[uname]["balance"]
    print("Balance is ", balance)

def view_users():
    print(dict_account)
