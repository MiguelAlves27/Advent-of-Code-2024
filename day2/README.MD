# Advent of Code 2024: Day 2 - Red-Nosed Reports

Welcome to my solution repository for **Advent of Code 2024**! This repository contains solutions for **Day 2, Part 1** and **Part 2**: *Red-Nosed Reports*. 🎄✨

---

## 📖 Problem Overview

The **Red-Nosed Reactor Engineers** need help analyzing unusual data from their reactor. The input consists of multiple reports, each containing a list of numerical levels. The goal is to determine how many of these reports are "safe."

### Part 1
A report is considered **safe** if:
1. The levels are either **strictly increasing** or **strictly decreasing**.
2. The difference between any two adjacent levels is at least `1` and at most `3`.

#### Example
- **Input**:
    ```
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    ```
- **Output**: 2 reports are safe:
    - `7 6 4 2 1`: Safe (strictly decreasing, differences of `1` or `2`).
    - `1 3 6 7 9`: Safe (strictly increasing, differences of `1` or `2`).

---

### Part 2
The **Problem Dampener** allows removing a single level from a report to make it safe. With this, more reports can be counted as safe.

#### Example
- **Input**:
    ```
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    ```
- **Output**: 4 reports are safe:
    - `7 6 4 2 1`: Safe without changes.
    - `1 3 6 7 9`: Safe without changes.
    - `1 3 2 4 5`: Safe by removing `3`.
    - `8 6 4 4 1`: Safe by removing `4`.

---

## 💡 Solution Explanation

### Part 1: Safe Reports
1. **Read Input**: Parse the input file to create a list of reports, where each report is a list of integers.
2. **Check Safety**:
    - Verify if the report is strictly increasing or decreasing.
    - Ensure the differences between consecutive levels are between `1` and `3`.
3. **Count Safe Reports**: Use the safety criteria to count the safe reports.

### Part 2: Conditionally Safe Reports
1. **Check Safety with Removals**:
    - If a report is not safe, iterate through each level and temporarily remove it.
    - Check if the modified report satisfies the safety criteria.
2. **Count Conditionally Safe Reports**: 
    - Include reports that become safe with one level removed.

---

## 🔧 How to Run

Follow these steps to execute the solution:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/MiguelAlves27/Advent-of-Code-2024.git
    cd advent-of-code-2024/day2
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