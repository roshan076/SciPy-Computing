# Sudoku Solver

This Python code implements a backtracking algorithm to solve a Sudoku puzzle. The main components of the solution are as follows:

---
## Board Class
- **Constructor**: The `Board` class is initialized with a 9x9 Sudoku board, represented as a 2D list (`board`).
- **__str__()**: This method converts the board into a string for easy printing. Empty cells are represented by `*` and other numbers are displayed as they are.
- **find_empty_cell()**: This method scans the board for the first empty cell, marked by `0`. It returns the coordinates (row, column) of the empty cell or `None` if no empty cells are found.
- **valid_in_row(row, num)**: This method checks if the number `num` can be placed in the specified `row` without violating Sudoku rules.
- **valid_in_col(col, num)**: This method checks if the number `num` can be placed in the specified `col` without violating Sudoku rules.
- **valid_in_square(row, col, num)**: This method checks if the number `num` can be placed in the 3x3 square containing the specified cell `(row, col)` without violating Sudoku rules.
- **is_valid(empty, num)**: This method checks if placing `num` in the given empty cell `(row, col)` is valid according to the Sudoku rules (row, column, and square constraints).
- **solver()**: This is the backtracking method that tries to solve the puzzle recursively. It first finds an empty cell, then attempts to fill it with valid numbers (from 1 to 9). If placing a number leads to a valid solution, it continues to solve the rest of the puzzle. If no number works, it backtracks and tries a different number.

---
## solve_sudoku Function
- This function is the main entry point for solving a Sudoku puzzle. It:
  1. Initializes a `Board` object with the provided Sudoku puzzle.
  2. Prints the initial puzzle.
  3. Calls the `solver()` method of the `Board` class to attempt solving the puzzle.
  4. If the puzzle is solvable, it prints the solved puzzle; otherwise, it indicates that the puzzle is unsolvable.
