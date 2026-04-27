import json

def read():
    try:
        with open("users.json","r") as file:
            users = json.load(file)
            return users
    except (FileNotFoundError,json.JSONDecodeError):
        users = []
        return users



def singup():
    users = read()
    name = input("Enter your name : ")
    email = input("Enter your email here : ")
    role = input("Are you student or Admin: ")
    password = input("Enter your Password here : ")

    
    for user in users:
        if email == user["email"]:
            print("User already exist")
            return
    users.append({
        "name" : name,
        "email" : email,
        "password" : password,
        "role":role
    })
    with open("users.json" , "w") as file:
        json.dump(users,file,indent=4)
    print("Signup Successfuly")
    

def singin():
    users = read()
    email = input("Enter your email here : ")
    password = input("Enter your Password here : ")
    role = input("Are you a student or admin : ")
    for user in users:
        if user["email"] == email and user["password"] == password and user["role"] == role:
            print( f"Welcome back  {user['name']}")
            return {"logedin" : True,"role": user["role"]}
    print("Invalid email or password")

def change_password():
    users = read()
    email = input("Enter email : ")
    password = input("Enter password : ")
    for user in users:
        if user["email"] == email and user["password"] == password:
            new_password = input("Enter New password : ")
            user["password"] = new_password
            print("Password Changed !")
            with open("users.json","w") as file:
                json.dump(users , file,indent=4)
            return
    print("User not Found")
   



def menu():
    while True:
        print("*" * 50)
        print(" ")
        print(" 1. Signup")
        print(" 2. Signin ")
        print(" 3. Change Password")
        print(" 4. Exit ")
        try:
            choice = int(input("Enter your choice "))
            if choice == 1:
                singup()
            elif choice == 2:
                singin()
            elif choice == 3:
                change_password()
            elif choice == 4:
                print("Good bye")
                break
            else:
                print("Please Valid choice")

        except:
            print("Enter only numeric according to menu")


def main():
    
    menu()
    
main()