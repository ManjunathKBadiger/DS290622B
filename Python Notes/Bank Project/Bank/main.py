import account as act

print("-------Bank System------------")
print("-------Welcome to All------------")

while True: 
    print("Press C to create account")
    print("Press L to Login ")
    print("Press U to View users ")
    print("Press Q to Exit ")
    user_input = input("Press Key ")
    if user_input.upper() == 'C':
        name = input("Enter a user name : ")
        password = input("Enter a Password : ")
        act.create_account(name, password)
        #------------------------
    elif user_input.upper() == 'U':
        act.view_users()
    elif user_input.upper() == 'L':
        name = input("Enter a user name : ")
        pwd = input("Enter a password: ")
        if act.login(name, pwd):
            while True:
                print("Press T to Withdraw ")
                print("Press A to Add Balance ")
                print("Press V to View Balance ")
                print("Press Q to Exit ")
                user_input = input("Press Key ")
                if user_input.upper() == 'T':
                    pin = input("Enter a PIN: ")
                    act.transaction(name, pin)
                elif user_input.upper() == 'A':
                    act.add_balance(name)
                elif user_input.upper() == 'V':
                    act.view_balance(name)
                elif user_input.upper() == 'Q':
                    break
    elif user_input.upper() == 'Q':
        break