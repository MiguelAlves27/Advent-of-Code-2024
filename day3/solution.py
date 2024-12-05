import re

# Function to process the input file and calculate results
def process_file(file_path):
    """
    Processes a file to evaluate specific operations based on defined patterns.

    The operations include:
    - Multiplying two numbers in "mul(a,b)" format.
    - Enabling or disabling addition of results with "do()" or "don't()".

    Args:
        file_path (str): Path to the input file.

    Returns:
        tuple: Two integers representing the results for Part 1 and Part 2.
    """
    # Regular expressions to match patterns in the input
    pattern_mul = r"mul\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)"  # Matches "mul(a,b)" and captures a and b
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"  # Matches all valid operations

    # Initialize result counters
    result_part1 = 0  # Accumulated total for Part 1
    result_part2 = 0  # Accumulated total for Part 2
    add = True  # Flag to determine if results should be added to Part 2

    # Open and read the input file line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Find all matches for valid operations in the current line
            matches = re.findall(pattern, line)

            # Process each matched operation
            for operation in matches:
                if "mul" in operation:
                    # Extract the two numbers to multiply from the "mul(a,b)" pattern
                    a, b = map(int, re.findall(pattern_mul, operation)[0])
                    product = a * b  # Calculate the product

                    # Update results for Part 1 and Part 2
                    result_part1 += product
                    if add:
                        result_part2 += product

                elif "do()" in operation:
                    add = True  # Enable addition to Part 2 results

                elif "don't()" in operation:
                    add = False  # Disable addition to Part 2 results

    return result_part1, result_part2


# Main function to execute the script
if __name__ == "__main__":
    # Specify the input file path
    input_file = 'day3/input.txt'

    # Process the file and calculate results for Part 1 and Part 2
    part1_result, part2_result = process_file(input_file)

    # Print results
    print("Result Part 1:", part1_result)
    print("Result Part 2:", part2_result)
