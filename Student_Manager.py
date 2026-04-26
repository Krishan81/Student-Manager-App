student = {}

choice = input("Enter your choice: ")

while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #Add Student
    if choice == "1":
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = float(input("Enter marks: "))
        student[roll_number] = {"name": name, "marks": marks}
        print(f"{name} Successfully Added!")

    #View Students
    elif choice == "2":
        if not student:
                print("No student found!")
        else:
            print("\n--- Student List ---")
            for roll_number, info in student.items():
                print(f"Roll Number: {roll_number}, Name: {info['name']}, Marks: {info['marks']}")
 
    #Check Result
    elif choice == "3":
        roll_number = input("Enter roll number to check result: ")
        if roll_number in student:
            marks = student[roll_number]["marks"]
            if marks >= 40:
                print(f"{student[roll_number]['name']} Passed with {marks} marks.")
            else:
                print(f"{student[roll_number]['name']} Failed with {marks} marks.")
        else:
            print("Student not found!")

    #Exit
    elif choice == "4":
        print("Exiting Student Manager App. Goodbye!")
        break   