import json

# def readDept():
#     try:
#         with open("departments.json","r") as file:
#             departments = json.load(file)
#             return departments
#     except FileNotFoundError:
#         return {}
    



# def addDept():
#     try:
#         with open("departments.json","w") as file:
#             departments = json.load(file)
#             return departments
#     except FileNotFoundError:
#         return {}

import json

def readDept():
    try:
        with open("departments.json","r") as file:
            departments = json.load(file)
            return departments
    except FileNotFoundError:
        return []

def newDept():
    departments = readDept()
    depart_name = input("Enter the name of department: ")
    for deaprtment in departments:
        if deaprtment['Depart'] == depart_name:
            print("Department Already Exist add new one ")
            return

    numberCourse = int(input("How many course will you add : "))
    courses = []

    for i in numberCourse:
        course = input(f"Enter course no {i}: ")
        courses.append(course)
    with open("departments.json","w") as file:
        json.dump({"Depart": depart_name,"Courses": courses},file, indent=4)

        
import json
def read():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return []
    


def new_course():
  departments = readDept()
  dept = input("Enter department name to add new course : ")
  course = input("Enter course name : ")
  for department in departments:
    if department["Depart"] == dept:
      department["courses"].append(course)
  print(f'New course {course} added successfully')

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



    