def add_matrices(matrix_a, matrix_b):
    """Function to perform element-wise addition of two matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Add elements corresponding to same indices
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def print_matrix(matrix):
    """Helper function to format and print a 2D matrix."""
    for row in matrix:
        print(" ".join(f"{val:4d}" for val in row))


if __name__ == "__main__":
    # Define Matrix A (3x3)
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Define Matrix B (3x3)
    matrix_b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    # Calculate Matrix Addition
    result = add_matrices(matrix_a, matrix_b)

    # Display Results
    print("Matrix A:")
    print_matrix(matrix_a)

    print("\nMatrix B:")
    print_matrix(matrix_b)

    print("\nSum of Matrix A and Matrix B:")
    print_matrix(result)
