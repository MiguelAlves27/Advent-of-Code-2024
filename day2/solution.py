# Function to parse input data from a file
def parse_reports(file_path):
    """
    Reads integer lists from a file, where each line contains space-separated integers.
    
    Args:
        file_path (str): Path to the input file.
    
    Returns:
        list: A list of lists, where each sublist represents a line of integers from the file.
    """
    reports = []  # List to store reports (each a list of integers)
    with open(file_path, 'r') as file:
        for line in file:
            # Convert each space-separated number to an integer and append to reports list
            reports.append([int(num) for num in line.split()])
    return reports


# Function to check if a list is "safe"
def is_safe(report):
    """
    Determines if a list of integers is "safe".
    A list is considered safe if:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least 1 and at most 3.

    Args:
        report (list): A list of integers to check.

    Returns:
        bool: True if the list is safe, False otherwise.
    """

    # Check if the report is either strictly increasing or strictly decreasing
    return (
        all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1)) or
        all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    )


# Function to calculate the number of safe reports (Part 1)
def count_safe_reports(reports):
    """
    Counts the number of "safe" reports in the dataset.
    
    Args:
        reports (list): A list of lists of integers.
    
    Returns:
        int: The count of safe reports.
    """
    # Apply `is_safe` function to each report and count how many are safe
    return sum(is_safe(report) for report in reports)


# Function to calculate the number of conditionally safe reports (Part 2)
def count_conditionally_safe_reports(reports):
    """
    Counts the number of "safe" or conditionally "safe" reports.
    A report is conditionally safe if removing any one element makes it safe.
    
    Args:
        reports (list): A list of lists of integers.
    
    Returns:
        int: The count of conditionally safe reports.
    """
    safe_count = 0
    for report in reports:
        # Check if the report is already safe
        if is_safe(report):
            safe_count += 1
        else:
            # Check if removing any one element makes the report safe
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    safe_count += 1
                    break  # No need to check further once a valid removal is found
    return safe_count


# Main function to execute the script
if __name__ == "__main__":
    # Specify the input file path
    input_file = 'day2/input.txt'

    # Parse the input data
    reports = parse_reports(input_file)

    # Calculate Part 1: Number of safe reports
    part1_solution = count_safe_reports(reports)

    # Calculate Part 2: Number of conditionally safe reports
    part2_solution = count_conditionally_safe_reports(reports)

    # Print results
    print("Part 1 Solution (Safe Reports Count):", part1_solution)
    print("Part 2 Solution (Conditionally Safe Reports Count):", part2_solution)
