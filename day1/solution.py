# Function to calculate the minimum sum of absolute differences (Part 1)
def calculate_minimum_difference(file_path):
    """
    Reads integer pairs from a file, sorts them, and calculates 
    the sum of absolute differences between corresponding values 
    in two sorted lists.

    Args:
        file_path (str): Path to the input file containing pairs of integers.

    Returns:
        int: The calculated sum of absolute differences (Part 1).
    """
    # Initialize lists for left and right values
    left_list = []
    right_list = []

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into two integers
            left, right = map(int, line.split())
            # Append to respective lists
            left_list.append(left)
            right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the sum of absolute differences
    part1_solution = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return part1_solution, left_list, right_list


# Function to calculate the sum of weighted occurrences (Part 2)
def calculate_weighted_occurrences(left_list, right_list):
    """
    Calculates the sum of weighted occurrences for numbers in left_list 
    that also exist in right_list.

    Args:
        left_list (list): The list of integers from the left column.
        right_list (list): The list of integers from the right column.

    Returns:
        int: The calculated weighted sum (Part 2).
    """
    solution = 0
    for e in left_list:
        if e in right_list:
            occur = right_list.count(e)
            solution += abs(e * occur)
    return solution


# Main function to execute the script
if __name__ == "__main__":
    # Specify the input file path
    input_file = 'day1/input.txt'

    # Calculate Part 1 solution and retrieve sorted lists
    part1_solution, left_list, right_list = calculate_minimum_difference(input_file)

    # Calculate Part 2 solution
    part2_solution = calculate_weighted_occurrences(left_list, right_list)

    # Print results
    print("Part 1 Solution (Sum of Absolute Differences):", part1_solution)
    print("Part 2 Solution (Weighted Occurrences):", part2_solution)
