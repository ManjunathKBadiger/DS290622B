import json
import getpass
class Store:

    def __init__(self, name):
        self.store_name = name
        self.fruits = {}
        self.fruit_id = 0
        self.user_details = {}
        self.user_json = "user.json"
        self.ordered_item=[]

    # admin functionality

    def add_fruit(self):
        try:
            name = input("Enter the fruit name :")
            quantity = float(input("Enter the quantity : "))
            price = float(input("Enter the price : "))
            stock =  float(input("Enter the available stock : "))
            fruit_item = {"Name": name, "Quantity":quantity, "Price":price,"Stock":stock}
            self.fruit_id = len(self.fruits) + 1
            self.fruits[self.fruit_id] = fruit_item

            print("Successfully Added")
        except Exception as e:
            print("\n Something went wrong please try again ")
    
    def edit_fruit_item(self):
        id = int(input("Enter the fruit ID"))
        print("1.Food Name\n2. Update Food item")
        y = input("Enter the number ")
        if id in self.fruits.keys(): 
            if y == '1':
                self.fruits[id]["Name"] = input("Update Food name")
        else:
            print("Sorry invalid keys")
    
    def view_fruits(self):
        if len(self.fruits)!= 0:
            for i in self.fruits:
                print(f"Fruit Id {i}")
                for j in self.fruits[i]:
                    print(j, ":", self.fruits[i][j])
                print()
        else:
            print("Sorry No Fruit item")
    
    def user_reg(self):
        name = input("Enter a name: ")
        phone_number = input("Enter a Phone: ")
        # email = input("Enter email : ")
        # password = input("Enter a password : ")

        user_reg = {"Name": name, "mobile":phone_number}
        # user_id = "{ 1 : " + user_reg + " }"

        try:

            json_obj = json.dumps(user_reg, indent=4)
            file = open("user.json", "w", newline="")
            content = json.dump(json_obj,file)

            
        except Exception:
            # content = []
            # content.append(user_reg)
            print("Json error")

        
           



def main():
    try:
        obj = Store("Fruit Shop")
        print("Welcome to the Fruit Shop ")
        while True:
            print("1. Admin \n2. User \n3. Exit")
            key = input("Enter :")
            if key =='1':
                fp = open("admin.json", "r")
                content = json.load(fp)
                username = input("Enter Username: ")
                password = getpass.getpass("Enter Password: ")
                if content["username"]==username and content["password"]==password:
                    while True:
                        print("1. Add New item \n2. Edit Item\n3.View Fruits\n Exit q")
                        key_a = input("Enter :")
                        if key_a == '1':
                            obj.add_fruit()
                        elif key_a == '2':
                            obj.edit_fruit_item()
                        elif key_a == '3':
                            obj.view_fruits()
                        elif key_a == 'q':
                            break
            elif key == "2":
                obj.user_reg()
            elif key == '3':
                break
    except Exception:
        print("Something went wrong please try again ")

if __name__ == '__main__':
    main()