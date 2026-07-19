student={}

while True:
    print("\nStudent Result Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Student Result")
    print("5. Exit")

    choice = input("Enter your choice: ")
    #Add Student
    if choice == "1":
        name = input("Enter student name: ")
        marks=int(input("Enter student marks: "))
        student[name] = marks
        print(f"Student {name} added successfully.")

    #View Student
    elif choice == "2":
        if not student:
            print("No Student Found")
        else:
            for name,marks in student.items():
                print(name,":",marks)
            

    #check result
    elif choice == "3":
        name=input("Enter Student Name:")
        if name in student:
            marks=student[name]

            if marks>=40:
                print("Pass")
            else:
                print("Fail")
           
        else:
            print(f"Student {name} not found.")
       
   #exit
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")



