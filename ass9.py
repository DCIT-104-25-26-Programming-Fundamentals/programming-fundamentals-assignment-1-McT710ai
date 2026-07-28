def display_menu():
    """
    Display the calculator menu.
    """
    print("\n" + "=" * 30)
    print("     SIMPLE CALCULATOR")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
    print("-" * 30)


def get_numbers():
    """
    Helper function to get two numbers from the user.
    Returns a tuple (num1, num2) or (None, None) if input is invalid.
    """
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None, None


def addition():
    """Perform addition: num1 + num2"""
    num1, num2 = get_numbers()
    if num1 is not None and num2 is not None:
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")


def subtraction():
    """Perform subtraction: num1 - num2"""
    num1, num2 = get_numbers()
    if num1 is not None and num2 is not None:
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")


def multiplication():
    """Perform multiplication: num1 * num2"""
    num1, num2 = get_numbers()
    if num1 is not None and num2 is not None:
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")


def division():
    """Perform division: num1 / num2"""
    num1, num2 = get_numbers()
    if num1 is not None and num2 is not None:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result:.2f}")


def modulus():
    """Perform modulus: num1 % num2"""
    num1, num2 = get_numbers()
    if num1 is not None and num2 is not None:
        if num2 == 0:
            print("Error: Cannot divide by zero for modulus operation.")
        else:
            result = num1 % num2
            print(f"Result: {num1} % {num2} = {result}")


def exponentiation():
    """Perform exponentiation: num1 ** num2"""
    num1, num2 = get_numbers()
    if num1 is not None and num2 is not None:
        result = num1 ** num2
        print(f"Result: {num1} ** {num2} = {result}")


def main():
    """
    Main program loop.
    """
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()
        
        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            division()
        elif choice == "5":
            modulus()
        elif choice == "6":
            exponentiation()
        elif choice == "7":
            print("\nGoodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 7.")


# Run the program
if __name__ == "__main__":
    main()