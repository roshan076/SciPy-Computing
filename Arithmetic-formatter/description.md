# Arithmetic Formatter

This Python function, `arithmetic_arranger`, is designed to format arithmetic problems for easy readability. The function can handle simple addition and subtraction problems and display them in a neatly aligned layout. It can also optionally show the answers to the problems.

---

## Function Overview

The `arithmetic_arranger` function arranges a list of arithmetic problems into a neat and aligned format. It ensures that:
1. Each problem is displayed on a separate line.
2. The numbers, operators, and results are aligned.
3. It handles errors such as invalid operators, non-digit characters, or numbers that are too large.

### Parameters:
- `problems`: A list of strings, each containing an arithmetic problem (e.g., `"32 + 698"`, `"3801 - 2"`). The problems should involve only addition or subtraction.
- `show_answers`: A boolean flag (default `False`). If `True`, the answers to the problems are included in the output.

### Returns:
- A string representing the formatted arithmetic problems. If `show_answers` is `True`, the answers are shown below the problems.

### Error Handling:
- If more than 5 problems are provided, the function returns:  
  `'Error: Too many problems.'`
- If an operator other than `+` or `-` is present, it returns:  
  `'Error: Operator must be '+' or '-'.'`
- If any of the numbers in the problems contain non-digit characters, it returns:  
  `'Error: Numbers must only contain digits.'`
- If any of the numbers have more than 4 digits, it returns:  
  `'Error: Numbers cannot be more than four digits.'`

### Layout and Formatting:
- The problems are aligned such that the numbers, operator, and result (if shown) all align to the right.
- Each line (numbers, operators, dashes) is spaced out with 4 spaces between them for readability.