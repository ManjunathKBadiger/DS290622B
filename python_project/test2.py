import json
from json.decoder import JSONDecodeError

# ---------------------------ADD FOOD ITEMS------------------------>>>
def add_food(filename, food_name, quantity, price, discount, stock):
    
    food = {}
    food_ID = len(food) + 1
    food_items = {'Food_Name' : food_name,
                  'Quantity' : quantity,
                  'Price': price,
                  'Discount' : discount,
                  'Stock': stock}
    
    try:
        file = open(filename, 'r+')
        data = json.load(file)
        
        for i in data:
            if data[i]['Food_Name'] == food_name:
                file.close()
                return 'Food already exists'
            
            else:
                food_ID = len(data) + 1
                food[food_ID] = food_items
                data.update(food)
            
    except json.decoder.JSONDecodeError:
        data = {}
        food[food_ID] = food_items
        data.update(food)
    file.seek(0)
    file.truncate()
    json.dump(data, file, indent=4)
    file.close()
    return 'Success'
        
# -------------------------EDIT FOOD----------------------->>>  
def edit_food(filename, food_ID):
    
    with open(filename) as file:
        content = json.load(file)
        if food_ID in content.keys():
            print("What you want to update in food item??")
            print("1) Food name")
            print("2) Food Quantity")
            print("3) Food price")
            print("4) Discount on food")
            print("5) Stock availability")

            y = input('Enter your choice : ')
            if y == "1":
                content[food_ID]["Food_Name"] = input('Enter Updated name :')
                print("\n Updated Successfully \n")
            elif y == "2":
                content[food_ID]["Quantity"] = input('Enter Updated quantity :')
                print("\n Updated Successfully \n")
            elif y == "3":
                content[food_ID]["Price"] = input('Enter Updated price :')
                print("\n Updated Successfully \n")
            elif y == "4":
                content[food_ID]["Discount"] = input('Enter Updated discount value :')
                print("\n Updated Successfully \n")
            elif y == "5":
                content[food_ID]["Stock"] = input('Enter Updated stock :')
                print("\n Updated Successfully \n")
            else:
                print('Invalid selection')
        else:
            print('Invalid Food ID') 
    file = open(filename, 'w')
    json.dump(content, file, indent=4)
    file.close()
    return 'Success'
    
    
#------------------------------REMOVE FOOD ITEM-------------------->>>
def remove_food(filename):
    file = open(filename, 'r+')
    data = json.load(file)
    
    for i in data:
        if i == input('Enter food ID : '):
            del data[i]
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)
            file.close()
            return 'Success'
    return 'Please enter valid food ID'

#------------------------SHOW FOOD--------------------->>>
def show_food(filename):
    try:
        file = open(filename)
        content = json.load(file)
        print("-------------Menu------------")
    
        for i in content:
            print(f'Food ID : {i}')
            print(f"Food Name : {content[i]['Food_Name']}")
            print(f"Quantity : {content[i]['Quantity']}")
            print(f"Price : {content[i]['Price']}")
            print(f"Discount : {content[i]['Discount']}")
            print(f"Stock : {content[i]['Stock']}")
            print('----------------------------------------')
        file.close()
        return True
    except json.JSONDecodeError:
        content = {}
        return 'No food available'

# -----------------------REGISTER NEW USERS------------------------------->>>
def register_user(user_file, username, email, password, address, phn_number):
    
    user = {'Full_name': username, 
           'Email': email, 
           'Password' : password,
           'Address': address,
           'Phone Number' : phn_number,
           'Order History' : []
           }
    try:
        file = open(user_file, 'r+')
        content = json.load(file)
        for i in range(len(content)):
            if content[i]['Email'] == email:
                return 'User already exists'
            
            else:
                content.append(user)
    except json.decoder.JSONDecodeError:
        content = []
        content.append(user)
        
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    return 'Registered successfully!'
    
    
# ---------------------PLACE ORDERS-------------------->>>>
def place_order(foodfile, userfile):
    file = open(foodfile, 'r+')
    content = json.load(file)
    if len(content) != 0:
        menu = []
        for items in content:
            menu.append([items, content[items]['Food_Name'], content[items]['Quantity'], content[items]['Price']])
        for menu_list in menu:
            print(menu_list)
            
        while True:
            with open(userfile) as file1:
                content1 = json.load(file1)
                
            for i in content1:
                print("Enter 1 to place order \nEnter 2 to Exit")
                x = input('Enter your choice : ')
                if x == '1':
                    print('Enter the food ID you want to ordered separated by the comma')
                    y = input().split(",")
                    for j in y:
                        z = int(j)
                        if z <= len(menu):
                            i['Order History'].append(menu[z-1])
                        else:
                            print("We don't have this food item")
                    print('List of food you selected : \n')
                    for k in i['Order History']:
                        print(k)

                # elif x == '2':
                #     break
                # else:
                #     print("Invalid Selection\n")
            file1 = open(userfile, 'w')
            json.dump(content1, file1, indent=4)
            file1.close()
            break
        
    else:
        print("Sorry! no food available")

    file.close()
    return "Success"
            

# -------------------ORDER HISTORY-------------------->>>
def order_history(filename, email):
    file = open(filename, 'r+')
    content = json.load(file)
    
    for i in content:
        if i["Email"] == email:
            if len(i["Order History"]) != 0:
                print("------------ORDER HISTORY------------\n")
                print(*i["Order History"])
            else:
                print(f"You haven't ordered yet")
            return True
    file.close()
    return False
        

#----------------------------UPDATE USER PROFILE------------->>>>
def update_user_profile(filename):
    file = open(filename, 'r+')
    content = json.load(file)
    
    for i in content:
        print('What you want to update??')
        print("1) Update Name")
        print("2) Update password")
        print("3) Update address")
        print("4) Update Phone number")
        print("5) Exit")
        val = input('Enter your choice : ')
        
        if val == "1":
            i["Full_name"] = input('Enter updated name : ')
            print("Updated successfully")
        elif val == "2":
            i["Password"] = input("Enter updated password : ")
        elif val == "3":
            i["Address"] = input("Enter new address : ")
        elif val == "4":
            i["Phone Number"] = input("Enter new phone number : ")
        else:
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return True
        

    
while True:
    print("1) Admin")
    print("2) User")
    print("3) Exit")

    val = input("Enter your selction : ")

# -------------ADMIN PLACE------------------->>>>
    if val == "1":
        fp = open('admin.json', 'r+')
        content = json.load(fp)
        username = input("Enter username : ")
        password = input("Enter password : ")
        if content["username"] == username and content["password"] == password:
            while True:
                print("---------ADMIN---------")
                print("1) Add food items")
                print("2) Edit food items")
                print("3) View food list")
                print("4) Remove food item")
                print("5) Logout as admin")

                val2 = input("Enter your selection : ")
                if val2 == "1":
                    food_name = input("Enter food name : ")
                    quantity = input("Enter quantity : ")
                    price = float(input("Enter food price : "))
                    discount = float(input("Enter discount value : "))
                    stock = int(input("Enter stock availability : "))
                    add_food("food.json", food_name, quantity, price, discount, stock)
                    print(f"Food named {food_name} added successfully")

                elif val2 == "2":
                    food_ID = input("Enter food ID : ")
                    edit_food("food.json", food_ID)
                    print(f"Food ID {food_ID} updated successfully\n")
                elif val2 == "3":
                    show_food("food.json")
                elif val2 == "4":
                    remove_food('food.json')
                    print(f"Food ID {i} removed successfully\n")
                elif val2 == "5":
                    print("-------Admin logout successfully!--------\n")
                    break
                    
                else:
                    print("------Invalid selection!!!-----\n")
        else:
            print("--------Wrong username and password-----------\n")
        fp.close()

# ---------------USER PLACE------------>>>>>

    elif val == "2":
        print("\n1) Register new user")
        print("2) Login User")
        print("3) Exit\n")

        val3 = input("Enter your choice : ")

        if val3 == "1":
            username = input("Enter fullname : ")
            email = input("Enter email ID : ")
            password = input("Enter password : ")
            address = input("Enter address : ")
            phn_number = int(input("Enter Phone number : "))
            register_user("user.json", username, email, password, address, phn_number)
            print(f"User registered successfully!!")
        elif val3 == "2":
            email = input("Enter user email ID : ")
            password = input("Enter user password : ")
            file = open("user.json", 'r+')
            content = json.load(file)

            for i in range(len(content)):
                if content[i]['Email'] == email and content[i]["Password"] == password:
                    while True:
                        print(f"\n-------------Hello {content[i]['Full_name']}-----------")
                        print("1) Place order")
                        print("2) Order History")
                        print("3) Update profile")
                        print("4) Logout")

                        val4 = input("Enter your choice : ")

                        if val4 == "1":
                            place_order("food.json", "user.json")
                        elif val4 == "2":
                            order_history('user.json', email)
                        elif val4 == "3":
                            update_user_profile('user.json')
                        elif val4 == "4":
                            print("User logout successfully\n")
                            break

                        else:
                            print("Invalid selection\n")
                else:
                    print("Worng username and password!!!\n")
        elif val3 == "3":
            break
        else:
            print("Invalid selection!!!\n")

    elif val == "3":
        print("Visit again!!!!!")
        break
# <<<<<<-------------------END LINE---------------------<<<<<<<<