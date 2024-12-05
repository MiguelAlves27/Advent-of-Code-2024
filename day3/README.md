# Advent of Code 2024: Day 3 - Mull It Over

Welcome to my solution repository for **Advent of Code 2024**! This repository contains solutions for **Day 3, Part 1** and **Part 2**: *Mull It Over*. 🎄✨

---

## 📖 Problem Overview

The challenge requires us to scan through corrupted memory that contains a series of `mul(X,Y)` instructions. The goal is to compute the sum of the results of these multiplications based on the valid operations in the input. Additionally, we need to handle conditional statements that enable or disable future `mul` instructions.

### Part 1
You are given a sequence of operations in a corrupted format. The valid operations are in the form of `mul(X, Y)` where `X` and `Y` are numbers. However, there are many invalid characters, such as `mul(4*`, `mul(6,9!`, and `?(12,34)`, that need to be ignored. 

The task is to sum the results of all valid `mul(X,Y)` instructions.

#### Example
- **Input**:
    ```
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    ```
- **Output**: 
    - The valid `mul` instructions are: 
        - `mul(2,4)`: 8
        - `mul(5,5)`: 25
        - `mul(11,8)`: 88
        - `mul(8,5)`: 40
    - The sum is: `8 + 25 + 88 + 40 = 161`.

---

### Part 2
In this part, you also need to consider two additional instructions: `do()` and `don't()`. These conditional instructions enable or disable future `mul` instructions. Only the most recent `do()` or `don't()` instruction applies, and at the start, all `mul` instructions are enabled.

#### Example
- **Input**:
    ```
    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    ```
- **Output**:
    - The valid `mul` instructions are:
        - `mul(2,4)`: 8 (enabled)
        - `mul(8,5)`: 40 (enabled)
    - The sum is: `8 + 40 = 48`.

---

## 💡 Solution Explanation

### Part 1: Valid Multiplications
1. **Read Input**: Parse the input to extract the valid `mul(X, Y)` instructions.
2. **Validate and Compute Multiplications**:
    - Ignore any corrupted or malformed instructions.
    - Multiply the numbers in the valid `mul(X, Y)` instructions and accumulate the result.

### Part 2: Conditional Multiplications
1. **Handle `do()` and `don't()` Instructions**:
    - Track the current state of whether `mul` instructions are enabled or disabled.
    - Enable or disable `mul` instructions based on the most recent `do()` or `don't()` instruction.
2. **Accumulate Results for Enabled `mul` Instructions**:
    - Only sum the results of `mul(X, Y)` instructions that are enabled.

---

## 🔧 How to Run

Follow these steps to execute the solution:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/MiguelAlves27/Advent-of-Code-2024.git
    cd advent-of-code-2024/day3
    ```

2. **Ensure Python is installed**:
    ```bash
    python --version
    ```

3. **Run the program**:
    ```bash
    python solution.py
    ```
    If your system requires `python3`, use:
    ```bash
    python3 solution.py
    ```

---

## 🤝 Contribution Guidelines

- **Coding Standards**: I follow clean coding practices and use consistent formatting, so I’d appreciate it if you do the same.
- **Documentation**: If your changes require updates to the documentation, please make sure to include them.
- **Testing**: Make sure all existing tests pass and, if needed, add new tests for your changes.
- **Pull Request Description**: Please write a clear and concise description of what your changes do and why they’re valuable.

---

## Feel Free to Contribute!  

I’m excited to have you contribute to this project! Whether you’re fixing a bug, adding a feature, or improving the documentation, your help is welcome and appreciated.

Thanks for contributing, and happy coding!
