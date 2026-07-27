# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Return the sum of all numbers in the list."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of all numbers in the list."""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def calculate_maximum(numbers):
    """Return the largest number in the list."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def calculate_minimum(numbers):
    """Return the smallest number in the list."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def main():
    # Get how many numbers the user wants to enter
    n = int(input("How many numbers? "))

    # Validate that n is a positive integer
    if n <= 0:
        print("Error: please enter a positive integer greater than 0.")
        return

    # Collect the numbers from the user
    numbers = []
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)

    # Compute statistics using our functions
    total   = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_maximum(numbers)
    minimum = calculate_minimum(numbers)

    # Display results
    print("\nResults:")
    # Print whole numbers without a decimal point, fractions with one decimal
    print(f"Sum:     {total:g}")
    print(f"Average: {average:g}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")


if __name__ == "__main__":
    main()