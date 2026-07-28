def display_menu():
    """
    Display the main menu options.
    """
    print("\n" + "=" * 32)
    print("   STUDENT RECORD SYSTEM MENU")
    print("=" * 32)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    print("-" * 32)


def add_student(students):
    """
    Ask user for student details and add to the records.
    """
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: ID must be a number.")
        return
    
    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print(f"Error: Student with ID {student_id} already exists.")
            return
    
    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be positive.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    scores = []
    for i in range(1, num_scores + 1):
        try:
            score = float(input(f"Enter score {i}: "))
            if score < 0 or score > 100:
                print("Warning: Score should be between 0 and 100.")
            scores.append(score)
        except ValueError:
            print(f"Error: Invalid score. Skipping score {i}.")
    
    # Create student record
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """
    Display all student records in a formatted table.
    """
    if not students:
        print("No students have been added yet.")
        return
    
    print("\n" + "-" * 68)
    print(f"{'Name':<15} {'ID':<12} {'Scores':<25} {'Average':<10}")
    print("-" * 68)
    
    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores = student["scores"]
        
        # Format scores as comma-separated string
        scores_str = ", ".join(str(s) for s in scores)
        
        # Calculate average
        if scores:
            avg = sum(scores) / len(scores)
            avg_str = f"{avg:.2f}"
        else:
            avg_str = "N/A"
        
        print(f"{name:<15} {student_id:<12} {scores_str:<25} {avg_str:<10}")
    
    print("-" * 68)


def calculate_average(students):
    """
    Ask for student ID and display their average score.
    """
    if not students:
        print("No students have been added yet.")
        return
    
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Please enter a valid ID number.")
        return
    
    # Search for the student
    found_student = None
    for student in students:
        if student["id"] == student_id:
            found_student = student
            break
    
    if found_student is None:
        print(f"Error: Student with ID {student_id} not found.")
        return
    
    scores = found_student["scores"]
    if not scores:
        print(f"{found_student['name']} has no scores to average.")
        return
    
    avg = sum(scores) / len(scores)
    print(f"{found_student['name']}'s average score: {avg:.2f}")


def main():
    """
    Main program loop.
    """
    students = []  # List to store all student records
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


# Run the program
if __name__ == "__main__":
    main()