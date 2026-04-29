# import json

# def readDept():
#     try:
#         with open("departments.json","r") as file:
#             departments = json.load(file)
#             return departments
#     except FileNotFoundError:
import json
def read():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return []
def remove_student():
    users = read()
    found = False
    stu_name = input("Enter student name to remove: ")
    stu_email = input("Enter student email: ")
    for user in users:
     if stu_name == user["name"] and stu_email == user["email"]:
            print("\n Student Record Found")
            print(f"Student Name: {stu_name}")
            print(f"Student email: {stu_email}")

            print("\nSelect Remove Reason")
            print("1. Admission Withdrawn")
            print("2. Duplicate Record")
            print("3. Expelled")
            print("4. Dropout")
            print("5. Other")

            choice = int(input("Enter choice: "))
            if choice == 1:
                reason = "Admission withdrawn"
            elif choice == 2:
                reason = "Duplicate Record"
            elif choice == 3:
                reason = "Expelled"
            elif choice == 4:
                reason = "Dropout"
            elif choice == 5:
                reason = "other"
            
            confirm = input("Are you sure you want to remove student (yes/no):").lower()
            if confirm == "yes":
                users.remove(user)
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                print("\n Student Removed Successfully")
            else:
                print("\nRemove cancelled.")

            found = True
            break

    if not found:
        print("Student not found or already removed.")
remove_student()



    