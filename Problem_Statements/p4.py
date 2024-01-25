def admit_student(student_id, name, age, course):
    student = {'Student ID': student_id, 'Name': name, 'Age': age, 'Course': course}
    student_list.append(student)
    print("Student admitted successfully.")

def display_student_list():
    if not student_list:
        print("No students have been admitted yet.")
    else:
        print("Student List:")
        for student in student_list:
            print(f"Student ID: {student['Student ID']} Name: {student['Name']} Age: {student['Age']} Course: {student['Course']}")

def update_student_information(student_id):
    for student in student_list:
        if student['Student ID'] == student_id:
            print("Select the information to update:")
            print("1. Name")
            print("2. Age")
            print("3. Course")
            choice = int(input("Enter the number of the information to update: "))
            if choice == 1:
                new_name = input("Enter the new Name: ")
                student['Name'] = new_name
            elif choice == 2:
                new_age = int(input("Enter the new Age: "))
                student['Age'] = new_age
            elif choice == 3:
                new_course = input("Enter the new Course: ")
                student['Course'] = new_course
            print("Student information updated successfully.")
            break
        else:
            print("Student not found.")

def search_student_by_id(student_id):
    for student in student_list:
        if student['Student ID'] == student_id:
            print("Student Details:")
            print(f"Student ID: {student['Student ID']} Name: {student['Name']} Age: {student['Age']} Course: {student['Course']}")
            break
    else:
        print("Student not found.")

def calculate_average_age():
    total_age = sum(student['Age'] for student in student_list)
    average_age = total_age / len(student_list)
    print(f"Average Age of Students: {average_age}")

def remove_student_by_id(student_id):
    global student_list
    student_list = [student for student in student_list if student['Student ID'] != student_id]
    print("Student removed from the list.")

student_list = []
while True:
    print("\n1. Admit Student")
    print("2. Display Student List")
    print("3. Update Student Information")
    print("4. Search Student by ID")
    print("5. Calculate Average Age")
    print("6. Remove Student by ID")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        admit_student(student_id, name, age, course)
    elif choice == 2:
        display_student_list()
    elif choice == 3:
        student_id = input("Enter Student ID to Update Information: ")
        update_student_information(student_id)
    elif choice == 4:
        student_id = input("Enter Student ID to Search: ")
        search_student_by_id(student_id)
    elif choice == 5:
        calculate_average_age()
    elif choice == 6:
        student_id = input("Enter Student ID to Remove: ")
        remove_student_by_id(student_id)
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")