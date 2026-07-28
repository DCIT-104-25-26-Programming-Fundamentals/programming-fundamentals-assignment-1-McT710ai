def calculate_sum(numbers):
    """
    Calculate the sum of all numbers in the list.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        int or float: The sum of all numbers
    """
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """
    Calculate the average of all numbers in the list.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        float: The average of all numbers
    """
    if len(numbers) == 0:
        return 0
    
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_maximum(numbers):
    """
    Find the maximum number in the list.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        int or float: The maximum value in the list
    """
    if len(numbers) == 0:
        return None
    
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def calculate_minimum(numbers):
    """
    Find the minimum number in the list.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        int or float: The minimum value in the list
    """
    if len(numbers) == 0:
        return None
    
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def main():
    """
    Main program function.
    Gets input from the user, collects numbers, and displays statistics.
    """
    # Get the number of values from the user
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
    # Validate that N is a positive integer
    if n <= 0:
        print("Error: Number of values must be positive.")
        return
    
    # Collect the numbers from the user
    numbers = []
    for i in range(1, n + 1):
        try:
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)
        except ValueError:
            print("Error: Please enter a valid number.")
            return
    
    # Calculate statistics using the functions
    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_maximum(numbers)
    minimum = calculate_minimum(numbers)
    
    # Display the results
    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


# This ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()