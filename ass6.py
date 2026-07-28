def print_single_table():
    """
    PART A: Ask user for a number and print its multiplication table from 1 to 12.
    """
    try:
        number = int(input("Enter a number: "))
        
        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 13):
            result = number * i
            print(f"{number}  x  {i:2d}  =  {result}")
            
    except ValueError:
        print("Error: Please enter a valid integer.")


def print_tables_up_to_n():
    """
    PART B: Ask user for N and print multiplication tables for numbers 1 to N.
    """
    try:
        n = int(input("Enter a number N: "))
        
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
        
        for num in range(1, n + 1):
            print(f"\nMultiplication Table for {num}:")
            for i in range(1, 13):
                result = num * i
                print(f"{num}  x  {i:2d}  =  {result}")
            
            # Add separator line between tables (but not after the last one)
            if num < n:
                print("-" * 27)  # 27 dashes to match the width of the table
                
    except ValueError:
        print("Error: Please enter a valid integer.")


def main():
    """
    Main function to run both parts.
    """
    print("PART A - Single Table:")
    print_single_table()
    
    print("\n" + "=" * 50)
    print("\nPART B - Tables from 1 to N:")
    print_tables_up_to_n()


# Run the program
if __name__ == "__main__":
    main()