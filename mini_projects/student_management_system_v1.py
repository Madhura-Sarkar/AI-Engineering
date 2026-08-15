students = []

while True:
    print("\n===== Student Result Management =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Show Topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # -------------------- Add Student --------------------
    if choice == "1":
        name = input("Enter your name: ")
        python_marks = int(input("Enter your Python marks: "))
        html_marks = int(input("Enter your HTML marks: "))
        css_marks = int(input("Enter your CSS marks: "))

        student = {
            "name": name,
            "python_marks": python_marks,
            "html_marks": html_marks,
            "css_marks": css_marks
        }

        students.append(student)
        print(f"\nStudent '{name}' added successfully!")

    # -------------------- View All Students --------------------
    elif choice == "2":
        if not students:
            print("\nNo students found.")
        else:
            print("\n===== Student List =====")
            for student in students:
                print(f"Name: {student['name']}")
                print(f"Python Marks: {student['python_marks']}")
                print(f"HTML Marks: {student['html_marks']}")
                print(f"CSS Marks: {student['css_marks']}")
                print("-" * 30)

    # -------------------- Search Student --------------------
    elif choice == "3":
        if not students:
            print("\nNo students found.")
        else:
            search_name = input("Enter the student name to search: ")
            found = False

            for student in students:
                if student["name"].lower() == search_name.lower():
                    print("\n===== Student Found =====")
                    print(f"Name: {student['name']}")
                    print(f"Python Marks: {student['python_marks']}")
                    print(f"HTML Marks: {student['html_marks']}")
                    print(f"CSS Marks: {student['css_marks']}")
                    found = True
                    break

            if not found:
                print(f"\nNo student found with the name '{search_name}'.")

    # -------------------- Show Topper --------------------
    elif choice == "4":
        if not students:
            print("\nNo student data found for calculating the topper.")
        else:
            topper = students[0]

            highest_total = (
                topper["python_marks"] +
                topper["html_marks"] +
                topper["css_marks"]
            )

            for student in students:
                total = (
                    student["python_marks"] +
                    student["html_marks"] +
                    student["css_marks"]
                )

                if total > highest_total:
                    highest_total = total
                    topper = student

            print("\n🏆 ===== Topper ===== 🏆")
            print(f"Name         : {topper['name']}")
            print(f"Python Marks : {topper['python_marks']}")
            print(f"HTML Marks   : {topper['html_marks']}")
            print(f"CSS Marks    : {topper['css_marks']}")
            print(f"Total Marks  : {highest_total}")

    # -------------------- Exit --------------------
    elif choice == "5":
        print("\nThank you for using the Student Result Management System!")
        break

    # -------------------- Invalid Choice --------------------
    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")