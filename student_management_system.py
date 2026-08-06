# Student Management System
# Internship Assignment - Day 3

students = []


def add_student():
    """Add a new student."""

    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    for student in students:
        if student["ID"] == student_id:
            print("\nStudent ID already exists!\n")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("\nStudent added successfully!\n")


def view_students():
    """Display all students."""

    if not students:
        print("\nNo student records found.\n")
        return

    print("\n---------------- STUDENT RECORDS ----------------")

    for student in students:
        print(f"""
ID      : {student['ID']}
Name    : {student['Name']}
Age     : {student['Age']}
Course  : {student['Course']}
Marks   : {student['Marks']}
----------------------------------------------""")


def search_student():
    """Search student by ID or Name."""

    choice = input("\nSearch by (1) ID or (2) Name: ")

    if choice == "1":
        key = input("Enter Student ID: ")

        for student in students:
            if student["ID"] == key:
                print("\nStudent Found!")
                print(student)
                return

    elif choice == "2":
        key = input("Enter Student Name: ").lower()

        for student in students:
            if student["Name"].lower() == key:
                print("\nStudent Found!")
                print(student)
                return

    print("\nStudent not found.\n")


def update_student():
    """Update student details."""

    student_id = input("\nEnter Student ID to update: ")

    for student in students:

        if student["ID"] == student_id:

            print("\nLeave blank to keep existing value.\n")

            name = input(f"Name ({student['Name']}): ")
            age = input(f"Age ({student['Age']}): ")
            course = input(f"Course ({student['Course']}): ")
            marks = input(f"Marks ({student['Marks']}): ")

            if name:
                student["Name"] = name

            if age:
                student["Age"] = int(age)

            if course:
                student["Course"] = course

            if marks:
                student["Marks"] = float(marks)

            print("\nStudent updated successfully!\n")
            return

    print("\nStudent not found.\n")


def delete_student():
    """Delete student."""

    student_id = input("\nEnter Student ID to delete: ")

    for student in students:

        if student["ID"] == student_id:
            students.remove(student)
            print("\nStudent deleted successfully!\n")
            return

    print("\nStudent not found.\n")


def menu():

    while True:

        print("""
========== STUDENT MANAGEMENT SYSTEM ==========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

==============================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


menu()