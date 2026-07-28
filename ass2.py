def get_grade(score):
    """
    Determine the letter grade based on the score.
    
    Args:
        score (int): The student's score (0-100)
        
    Returns:
        str or None: The letter grade (A, B, C, D, F) or None if score is invalid
    """
    # Validate that the score is within the range 0-100
    if score < 0 or score > 100:
        return None
    
    # Determine the grade based on the scoring scale
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    """
    Main program function.
    Gets input from the user and displays the corresponding letter grade.
    """
    # Get input from user
    try:
        score = int(input("Enter student score (0-100): "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
    # Get the grade using the get_grade function
    grade = get_grade(score)
    
    # Check if the grade is valid and display the result
    if grade is None:
        print("Error: Score must be between 0 and 100.")
    else:
        print(f"Grade: {grade}")


# This ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()