def print_fibonacci_sequence():
    """
    PART A: Ask user for N and print the first N Fibonacci numbers.
    """
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
        
        # Generate the first n Fibonacci numbers
        if n == 1:
            sequence = [0]
        elif n == 2:
            sequence = [0, 1]
        else:
            sequence = [0, 1]
            for i in range(2, n):
                next_term = sequence[i-1] + sequence[i-2]
                sequence.append(next_term)
        
        # Print the sequence on one line
        print("Fibonacci sequence:", " ".join(map(str, sequence)))
        
    except ValueError:
        print("Error: Please enter a valid integer.")


def check_fibonacci_number():
    """
    PART B: Ask user for a number and check if it belongs to the Fibonacci sequence.
    """
    try:
        num = int(input("Enter a number to check: "))
        
        # Handle small numbers
        if num == 0 or num == 1:
            print(f"{num} is a Fibonacci number.")
            return
        
        # Generate Fibonacci numbers until we reach or exceed the input
        a, b = 0, 1
        while b < num:
            a, b = b, a + b
        
        # Check if we found the number
        if b == num:
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is NOT a Fibonacci number.")
            
    except ValueError:
        print("Error: Please enter a valid integer.")


def main():
    """
    Main function to run both parts.
    """
    print("PART A:")
    print_fibonacci_sequence()
    
    print("\nPART B:")
    check_fibonacci_number()


# Run the program
if __name__ == "__main__":
    main()