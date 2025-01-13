# Case Converter

This Python module provides a function to convert strings in ***PascalCase*** or ***camelCase*** format to ***snake_case*** format. The conversion involves inserting underscores before uppercase letters and converting them to lowercase.

---

## Features

- Converts strings from **PascalCase** or **camelCase** to **snake_case**.
- Supports both PascalCase (e.g., `PascalCaseString`) and camelCase (e.g., `camelCaseString`).
- Cleans up the string by removing unnecessary leading or trailing underscores.

---

## How It Works

The `convert_to_snake_case` function processes the given string by:
1. Iterating over each character in the input string.
2. Checking if the character is uppercase. If it is, it prepends an underscore (`_`) and converts it to lowercase.
3. Joining the characters into a single string and ensuring there are no leading or trailing underscores.