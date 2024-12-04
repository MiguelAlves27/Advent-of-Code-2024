# Advent of Code 2024: Day 1 - Historian Hysteria

Welcome to my solution repository for **Advent of Code 2024**! This repository contains solutions for **Day 1, Part 1** and **Part 2**: *Historian Hysteria*. 🎄✨

---

## 📖 Problem Overview
The **Senior Historians** of the North Pole are on a mission to locate the missing **Chief Historian**. Their first step is reconciling two mismatched lists of historically significant location IDs found in the Chief's office. Your tasks are:

### Part 1
1. Sort the two lists of location IDs.
2. Pair the smallest numbers from each list, then the second smallest, and so on.
3. Compute the sum of the absolute differences between each pair.

#### Example
- **Left List**: `[1, 2, 3, 3, 3, 4]`
- **Right List**: `[3, 3, 3, 4, 5, 9]`
- **Sorted and Paired Differences**:
  - Pair (1, 3): Distance = 2
  - Pair (2, 3): Distance = 1
  - Pair (3, 3): Distance = 0
  - Pair (3, 4): Distance = 1
  - Pair (3, 5): Distance = 2
  - Pair (4, 9): Distance = 5

**Total Distance** = `2 + 1 + 0 + 1 + 2 + 5 = 11`.

---

### Part 2
For each number in the **Left List**, if it also exists in the **Right List**, calculate its weighted sum by multiplying the number by its count of occurrences in the **Right List**. Then sum all these weighted values.

### Example

- **Left List**: `[3, 4, 2, 1, 3, 3]`  
- **Right List**: `[3, 3, 3, 4, 5, 9]`  

#### **Calculation of Weighted Occurrences**:

1. **Number `3`**  
   - Appears **3 times** in the **Right List**.  
   - Weighted Sum = `3 * 3 = 9`.  

2. **Number `4`**  
   - Appears **1 time** in the **Right List**.  
   - Weighted Sum = `4 * 1 = 4`.  

3. **Number `2`**  
   - Appears **0 times** in the **Right List**.  
   - Weighted Sum = `2 * 0 = 0`.  

4. **Number `1`**  
   - Appears **0 times** in the **Right List**.  
   - Weighted Sum = `1 * 0 = 0`.  

5. **Number `3` (again)**  
   - Appears **3 times** in the **Right List**.  
   - Weighted Sum = `3 * 3 = 9`.  

6. **Number `3` (again)**  
   - Appears **3 times** in the **Right List**.  
   - Weighted Sum = `3 * 3 = 9`.  

---

### **Total Similarity Score**  
`9 + 4 + 0 + 0 + 9 + 9 = 31`.


---

## 💡 Solution Explanation

### Part 1: Sum of Absolute Differences
- **Step 1**: Read the input file to extract two lists of integers.
- **Step 2**: Sort both lists.
- **Step 3**: Use Python's `zip` function to pair sorted values.
- **Step 4**: Compute the absolute difference for each pair and sum up the results.

### Part 2: Weighted Occurrences
- **Step 1**: For each value in the **Left List**, check if it exists in the **Right List**.
- **Step 2**: Multiply the value by its count of occurrences in the **Right List**.
- **Step 3**: Sum all these weighted values.

---

## 🔧 How to Run

Follow these steps to execute the solution:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MiguelAlves27/Advent-of-Code-2024.git
   cd advent-of-code-2024/day1

2. **Ensure Python is installed: Run the following command to check your Python version:**
    ```bash
    python --version

3. **Run the program: Execute the script with:**
    ```bash
    python solution.py
    ```
    If your system requires python3, use:
    ```bash
    python3 solution.py

## 🤝 Contribution Guidelines

- **Coding Standards**: I follow clean coding practices and use consistent formatting, so I’d appreciate it if you do the same.
- **Documentation**: If your changes require updates to the documentation, please make sure to include them.
- **Testing**: Make sure all existing tests pass and, if needed, add new tests for your changes.
- **Pull Request Description**: Please write a clear and concise description of what your changes do and why they’re valuable.

---

## Feel Free to Contribute!  

I’m excited to have you contribute to this project! Whether you’re fixing a bug, adding a feature, or improving the documentation, your help is welcome and appreciated.

Thanks for contributing, and happy coding!
