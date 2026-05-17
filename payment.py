import methods
import json

def payment():
    students = methods.readstudents()
    gmail = input("Verify your gmail here : ")
    selected_courses = []
    
    for student in students:
        if student["email"] == gmail:  # ← also fix "gmail" to "email" (your key is "email")
            selected_courses = student['dept']['courses']
    
    if not selected_courses:
        print("No courses found for this email!")
        return

    total = 15000 * len(selected_courses)
    print("*" * 30)
    print("Your courses with fee are these: ")
    for course in selected_courses:
        print(f"Course Name: {course} || Price: 15000")

    print(f"Your total dues are {total}")
    
    while True:
        user = int(input(f"Pay {total} Rs here: "))
        if user == total:
            print("Fee has been paid!")
            receipt(selected_courses, total)
            break
        elif user > total:
            print("Please pay exact amount, not more!")
        else:
            print("Please pay the full fee!")
    print("*" * 30)

def receipt(selected_courses, total):
    print("\n---------Fee Receipt-------------")
    for course in selected_courses:
        print(f"Course Name: {course} || Price: 15000")
    print(f"          Total : {total}")
    print(f"          Paid  : {total}")
    print(f"          Balance : 0")
    print("------------------------------------")