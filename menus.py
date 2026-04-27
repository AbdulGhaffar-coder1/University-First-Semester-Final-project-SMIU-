def adminMenu():
    print("*"*40)
    print("\n  1.Add new Course")
    print("  2.Add new Department")
    print("  3.Remove a student")
    print('')
    print("*" * 40)
    try:
        choice = int(input("Enter the option from menue : "))
        if choice == 1:
            newCourse()
        elif choice == 2:
            newDepartment()
        elif choice == 3:
            removeStudent()
        else:
            print("Please Enter valid option according to menue")
    except:
        print("Enter only numeric options mentioned in menue")







def studentMenu():
    print("*" * 40)
    print("\n  1.Application Form")
    print("  2. Department Selection")
    print("   3.Course selection")
    print("  4.Fee pay")
    try:
        choice = int(input("Enter the option from menue : "))
        if choice == 1:
            applicationForm()
        elif choice == 2:
            departmentSelection()
        elif choice == 3:
            courseSelection()
        elif choice == 4:
            payment()
        else:
            print("Please Enter valid option according to menue")
    except:
        print("Enter only numeric options mentioned in menue")
