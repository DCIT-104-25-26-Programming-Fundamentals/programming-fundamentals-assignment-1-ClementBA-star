# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols, label=""):
    """Prompt the user to enter a matrix row by row and return it as a 2D list."""
    if label:
        print(f"\nEnter {label} ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        while True:
            raw = input(f"  Enter row {i + 1}: ").split()
            if len(raw) == cols:
                matrix.append([float(v) for v in raw])
                break
            print(f"  Please enter exactly {cols} value(s).")
    return matrix


# -----------------------------------------------------------------------------
# Helper: display a matrix in a neat, aligned grid
# -----------------------------------------------------------------------------

def print_matrix(matrix):
    """Print a 2D list as an aligned grid."""
    # Determine the widest value so every column lines up
    flat = [v for row in matrix for v in row]
    width = max(len(f"{v:g}") for v in flat) + 1
    for row in matrix:
        print("  " + "".join(f"{v:>{width}g}" for v in row))


# -----------------------------------------------------------------------------
# PART A — Transpose
# -----------------------------------------------------------------------------

def transpose(matrix):
    """Return the transpose of a 2D list (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    # Build an empty cols x rows result
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result


def part_a():
    print("\n=== PART A: Transpose ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    result = transpose(matrix)
    print("\nTransposed Matrix:")
    print_matrix(result)


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------

def add_matrices(a, b):
    """Return the element-wise sum of two same-size matrices."""
    rows = len(a)
    cols = len(a[0])
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(a[r][c] + b[r][c])
        result.append(new_row)
    return result


def part_b():
    print("\n=== PART B: Add Two Matrices ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix_a = read_matrix(rows, cols, "Matrix A")
    matrix_b = read_matrix(rows, cols, "Matrix B")

    result = add_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)
    print("\nA + B:")
    print_matrix(result)


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------

def multiply_matrices(a, b):
    """Return the matrix product A x B.

    A is M x N, B is N x P, result is M x P.
    """
    m = len(a)
    n = len(a[0])   # must equal len(b)
    p = len(b[0])

    # Initialise result with zeros
    result = []
    for r in range(m):
        result.append([0.0] * p)

    # Triple nested loop: rows of A × columns of B
    for r in range(m):
        for c in range(p):
            total = 0.0
            for k in range(n):
                total += a[r][k] * b[k][c]
            result[r][c] = total

    return result


def part_c():
    print("\n=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter rows in Matrix A: "))
    n = int(input("Enter columns in Matrix A (= rows in Matrix B): "))
    p = int(input("Enter columns in Matrix B: "))

    matrix_a = read_matrix(m, n, "Matrix A")
    matrix_b = read_matrix(n, p, "Matrix B")

    result = multiply_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)
    print("\nA x B:")
    print_matrix(result)


# -----------------------------------------------------------------------------
# Main menu
# -----------------------------------------------------------------------------

def main():
    print("Matrix Operations")
    print("-----------------")
    print("A) Transpose a matrix")
    print("B) Add two matrices")
    print("C) Multiply two matrices")

    choice = input("\nChoose a part to run (A / B / C): ").strip().upper()

    if choice == "A":
        part_a()
    elif choice == "B":
        part_b()
    elif choice == "C":
        part_c()
    else:
        print("Invalid choice. Please enter A, B, or C.")


if __name__ == "__main__":
    main()