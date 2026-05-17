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
    dept = input("Enter the name of department: ")
    for department in departments:
        if department['Depart'] == dept:
            print("Department Already Exist add new one ")
            return
    numberCourse = int(input("How many course will you add : "))
    courses = []

    for i in range(numberCourse):
        course = input(f"Enter course no {i+1}: ")
        courses.append(course)
    departments.append({
        "Depart": dept,
        "courses":courses
           })
    with open("departments.json","w") as file:
        json.dump(departments,file, indent=4)

     
def read():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return []
    


def new_course():
  departments = readDept()
  dept = input("Enter department name to add new course: ")
  course = input("Enter course name: ")
    
  for department in departments:
        if department["Depart"] == dept:
            if course in department['courses']:
                
                print("Course Already Exist add other course")
                return
            department["courses"].append(course)
            print(f'New course {course} added successfully')
            break
  else:
    print("Department not Available")
            
  with open("departments.json", "w") as file:
        json.dump(departments, file, indent=4)

import methods
import json

def Application():
    print("Application Form")
    name = input("Enter your name : ")
    F_name = input("Enter your Father's name : ")
    email = input("Enter your email address : ")
    Dob = input("Enter your DOB (DD|MM|YYYY) : ")
    gender = input("Enter (Male/Female) : ")
    departments = readDept()
    num = 1
    
    for department in departments:
        print(f" {num}. Department Name : {department['Depart']}")
        num += 1
        
    department = input("Enter Department you want choose : ")
    student = {
        "name": name,
        "Fname": F_name,
        "email": email,
        "DOB": Dob,
        "gender": gender,
        "dept": {
            "dept": department,
        }
    }
    students = readstudents()
    students.append(student)
    
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=5)
    print("Successfully Registered")


def readstudents():
    try:
        with open('students.json', 'r') as file:
          students = json.load(file)
          return students
    except (FileNotFoundError,json.JSONDecodeError):
        return []



def courseSelection():
    departments = readDept()
    dept = input("Enter Your department name : ")
    gmail = input("Enter your gmail to verify : ")
    for department in departments:
       if  department["Depart"] == dept:
           number = 1
           for course in department["courses"]:
               print(f'{number}. {course}')
               number += 1
    courses = []
    print("Enter 5 courses from above One by one ")
    for i in range(1,6):
        course = input("Enter Course name to select : ")
        courses.append(course)
    students = readstudents()
    for student in students:
        if gmail == student['email']:
            print("Yes")
            student['dept']['courses'] = courses

    
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=5)
    print("Successfully Registered")

def remove_student():
    students = readstudents()
    found = False
    stu_name = input("Enter student name to remove: ")
    stu_email = input("Enter student email: ")
    for student in students:
     if stu_name == student["name"] and stu_email == student["email"]:
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
                students.remove(student)
                with open("students.json", "w") as file:
                    json.dump(students, file, indent=4)
                print("\n Student Removed Successfully")
            else:
                print("\nRemove cancelled.")

            found = True
            break

    if not found:
        print("Student not found or already removed.")



    