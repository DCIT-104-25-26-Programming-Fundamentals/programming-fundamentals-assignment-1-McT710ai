def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if n is prime, False otherwise
    """
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisors from 2 to sqrt(n)
    # We only need to check up to the square root of n
    # because if n has a divisor greater than sqrt(n),
    # it must also have a divisor less than sqrt(n)
    import math
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    # If no divisors found, n is prime
    return True


def main():
    """
    Main program function.
    Gets input from the user and displays whether the number is prime.
    """
    # Get input from user
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    # Check if the number is prime
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")


# This ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()