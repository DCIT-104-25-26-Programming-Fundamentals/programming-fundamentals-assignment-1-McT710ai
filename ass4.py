def read_matrix(rows, cols, matrix_name="Matrix"):
    """
    Read a matrix from the user.
    
    Args:
        rows (int): Number of rows
        cols (int): Number of columns
        matrix_name (str): Name of the matrix for display purposes
        
    Returns:
        list: A 2D list representing the matrix
    """
    matrix = []
    print(f"\nEnter {matrix_name}:")
    for i in range(rows):
        while True:
            try:
                row_input = input(f"  Row {i+1}: ").strip()
                row_values = row_input.split()
                
                # Check if we have exactly the right number of values
                if len(row_values) != cols:
                    print(f"Error: Row must have exactly {cols} values.")
                    continue
                
                # Convert to numbers (integers or floats)
                row = []
                for val in row_values:
                    # Try integer first, then float
                    if '.' in val:
                        row.append(float(val))
                    else:
                        row.append(int(val))
                
                matrix.append(row)
                break
                
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue
    
    return matrix


def display_matrix(matrix, title="Matrix"):
    """
    Display a matrix in a neat, aligned grid format.
    
    Args:
        matrix (list): A 2D list representing the matrix
        title (str): Title to display before the matrix
    """
    if not matrix:
        print(f"{title}: Empty matrix")
        return
    
    print(f"\n{title}:")
    
    # Find the maximum width needed for alignment
    max_width = 0
    for row in matrix:
        for value in row:
            # Handle both integers and floats
            if isinstance(value, float):
                width = len(f"{value:.2f}")
            else:
                width = len(str(value))
            if width > max_width:
                max_width = width
    
    # Add some padding
    max_width += 2
    
    # Display the matrix
    for row in matrix:
        for value in row:
            if isinstance(value, float):
                print(f"{value:.2f}".rjust(max_width), end="")
            else:
                print(str(value).rjust(max_width), end="")
        print()


def transpose_matrix(matrix):
    """
    Compute the transpose of a matrix.
    
    Args:
        matrix (list): A 2D list representing the matrix
        
    Returns:
        list: The transposed matrix
    """
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with cols x rows
    transposed = [[0] * rows for _ in range(cols)]
    
    # Fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed


def add_matrices(matrix1, matrix2):
    """
    Add two matrices element-wise.
    
    Args:
        matrix1 (list): First matrix
        matrix2 (list): Second matrix
        
    Returns:
        list: The sum of the two matrices
    """
    if not matrix1 or not matrix2:
        return []
    
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Create result matrix
    result = [[0] * cols for _ in range(rows)]
    
    # Add matrices element by element
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result


def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices.
    
    Args:
        matrix1 (list): First matrix (M x N)
        matrix2 (list): Second matrix (N x P)
        
    Returns:
        list: The product of the two matrices (M x P)
        
    Raises:
        ValueError: If the matrices cannot be multiplied
    """
    if not matrix1 or not matrix2:
        return []
    
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Check if multiplication is possible
    if cols1 != rows2:
        raise ValueError(f"Cannot multiply: columns of A ({cols1}) must equal rows of B ({rows2})")
    
    # Create result matrix (rows1 x cols2)
    result = [[0] * cols2 for _ in range(rows1)]
    
    # Multiply matrices using nested loops
    for i in range(rows1):
        for j in range(cols2):
            # Calculate dot product of row i of matrix1 and column j of matrix2
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result


def part_a():
    """
    Part A: Matrix Transpose
    """
    print("\n" + "="*50)
    print("PART A: Matrix Transpose")
    print("="*50)
    
    # Get matrix dimensions
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    
    if rows <= 0 or cols <= 0:
        print("Error: Rows and columns must be positive.")
        return
    
    # Read matrix
    matrix = read_matrix(rows, cols, "Original Matrix")
    
    # Display original matrix
    display_matrix(matrix, "Original Matrix")
    
    # Compute and display transpose
    transposed = transpose_matrix(matrix)
    display_matrix(transposed, "Transposed Matrix")


def part_b():
    """
    Part B: Matrix Addition
    """
    print("\n" + "="*50)
    print("PART B: Matrix Addition")
    print("="*50)
    
    # Get matrix dimensions
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    
    if rows <= 0 or cols <= 0:
        print("Error: Rows and columns must be positive.")
        return
    
    # Read two matrices
    matrix1 = read_matrix(rows, cols, "Matrix A")
    matrix2 = read_matrix(rows, cols, "Matrix B")
    
    # Display input matrices
    display_matrix(matrix1, "Matrix A")
    display_matrix(matrix2, "Matrix B")
    
    # Add matrices
    result = add_matrices(matrix1, matrix2)
    display_matrix(result, "A + B Result")


def part_c():
    """
    Part C: Matrix Multiplication
    """
    print("\n" + "="*50)
    print("PART C: Matrix Multiplication")
    print("="*50)
    
    # Get dimensions for matrix A
    try:
        m = int(input("Enter rows for Matrix A (M): "))
        n = int(input("Enter columns for Matrix A (N): "))
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    
    if m <= 0 or n <= 0:
        print("Error: All dimensions must be positive.")
        return
    
    # Read matrix A
    matrix_a = read_matrix(m, n, "Matrix A")
    
    # Get dimensions for matrix B
    # Matrix B must have N rows (same as columns of A)
    try:
        p = int(input(f"Enter columns for Matrix B (P): "))
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    
    if p <= 0:
        print("Error: Columns must be positive.")
        return
    
    # Read matrix B (will automatically have N rows)
    matrix_b = read_matrix(n, p, "Matrix B")
    
    # Display input matrices
    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    
    try:
        # Multiply matrices
        result = multiply_matrices(matrix_a, matrix_b)
        display_matrix(result, f"A × B Result ({m} x {p})")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    """
    Main program function.
    """
    print("MATRIX OPERATIONS PROGRAM")
    print("This program performs three matrix operations:")
    print("  1. Transpose a matrix")
    print("  2. Add two matrices")
    print("  3. Multiply two matrices")
    
    # Run all three parts
    part_a()
    part_b()
    part_c()
    
    print("\n" + "="*50)
    print("Program completed successfully!")


# This ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()
