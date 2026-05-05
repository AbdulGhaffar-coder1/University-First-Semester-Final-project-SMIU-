import json
import tkinter as tk
root = tk.Tk()
root.geometry("1000x800")


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
    nameLable = tk.Label(root,text="Name : ")
    nameLable.grid(row=0,column=0)
    name = tk.Entry(root)
    name.grid(column=1,row=0)
    emailLable = tk.Label(root,text="Email :")
    emailLable.grid(column=0,row=1)
    email = tk.Entry(root)
    email.grid(row=1,column=1)
    roleLable = tk.Label(root,text="Role : ")
    roleLable.grid(column=0,row=2)
    role = tk.Entry(root)
    role.grid(column=1,row=2)
    passwordLable = tk.Label(root,text="Password :")
    passwordLable.grid(column=0,row=3)
    password = tk.Entry(root)
    password.grid(column=1,row=3)

    result = tk.Label(root,text="")
    result.grid(column=0,row=6)

    def saveUser():
        Name = name.get()
        Email = email.get()
        Role = role.get()
        Password = password.get()
        for user in users:
           
            if Email == user["email"]:
                result.configure(text="User Already Exist by this email",fg="red")
                
                return
        users.append({
            "name" : Name,
            "email" : Email,
            "password" : Password,
            "role":Role
        })
        with open("users.json" , "w") as file:
            json.dump(users,file,indent=4)
        result.configure(text="Signup Successfuly",fg="green")
    
    btn = tk.Button(root,text="Save User",command=saveUser)
    btn.grid(row=5,column=2)
singup()
    

# def singin():
#     users = read()
#     email = input("Enter your email here : ")
#     password = input("Enter your Password here : ")
#     role = input("Are you a student or admin : ")
#     for user in users:
#         if user["email"] == email and user["password"] == password and user["role"] == role:
#             print( f"Welcome back  {user['name']}")
#             return {"logedin" : True,"role": user["role"]}
#     print("Invalid email or password")

# def change_password():
#     users = read()
#     email = input("Enter email : ")
#     password = input("Enter password : ")
#     for user in users:
#         if user["email"] == email and user["password"] == password:
#             new_password = input("Enter New password : ")
#             user["password"] = new_password
#             print("Password Changed !")
#             with open("users.json","w") as file:
#                 json.dump(users , file,indent=4)
#             return
#     print("User not Found")
   



# def menu():
#     while True:
#         print("*" * 50)
#         print(" ")
#         print(" 1. Signup")
#         print(" 2. Signin ")
#         print(" 3. Change Password")
#         print(" 4. Exit ")
#         try:
#             choice = int(input("Enter your choice "))
#             if choice == 1:
#                 singup()
#             elif choice == 2:
#                 singin()
#             elif choice == 3:
#                 change_password()
#             elif choice == 4:
#                 print("Good bye")
#                 break
#             else:
#                 print("Please Valid choice")

#         except:
#             print("Enter only numeric according to menu")


# def main():
    
#     menu()
    
# main()

root.mainloop()
