import methods
import payment

def studentMenu():
    while True:
        print("*" * 40)
        print("\n  1. Application Form")
        print("  2. Course selection")
        print("  3. Fee pay")
        print("  4. Logout")
        print("*" * 40)
        try:
            choice = int(input("Enter the option from menu: "))
            if choice == 1:
                methods.Application()
            elif choice == 2:
                methods.courseSelection()
            elif choice == 3:
                payment.payment()
            elif choice == 4:
                print("Logging out...")
                break   
            else:
                print("Please enter a valid option according to menu")
        except:
            print("Enter only numeric options mentioned in menu")

def adminMenu():
    while True:
        print("*" * 40)
        print("\n  1. Add new Course")
        print("  2. Add new Department")
        print("  3. Remove a student")
        print("  4. Logout")
        print("*" * 40)
        try:
            choice = int(input("Enter the option from menu: "))
            if choice == 1:
                methods.new_course()
            elif choice == 2:
                methods.newDept()
            elif choice == 3:
                methods.remove_student()
            elif choice == 4:
                print("Logging out...")
                break   
            else:
                print("Please enter a valid option according to menu")
        except:
            print("Enter only numeric options mentioned in menu")
