# Password Generator

This module generates a secure, random password based on user-defined constraints. It leverages the ***`secrets`*** module to ensure cryptographically secure random selections and the ***`re`*** module for pattern matching to enforce specific password requirements.

---

## How It Works

1. **Function Definition**:  
   The function `generate_password()` takes several optional arguments that specify the password's constraints:
   - `length`: The desired length of the password (default is 16).
   - `nums`: The minimum number of numeric digits required (default is 1).
   - `special_chars`: The minimum number of special characters (from `string.punctuation`) required (default is 1).
   - `uppercase`: The minimum number of uppercase letters required (default is 1).
   - `lowercase`: The minimum number of lowercase letters required (default is 1).

2. **Character Pool**:  
   The password is generated from a pool of characters that includes:
   - Uppercase letters (`A-Z`).
   - Lowercase letters (`a-z`).
   - Digits (`0-9`).
   - Special characters (e.g., `!`, `@`, `#`, etc.).

3. **Password Generation**:  
   The function generates a random password by repeatedly choosing characters from the combined pool of allowed characters. It continues to generate passwords until the generated password meets all the constraints provided by the user.

4. **Constraints Checking**:  
   After generating a password, the script checks whether the password satisfies all the specified conditions using regular expressions:
   - It checks if there are enough numeric digits (`\d`).
   - It checks if there are enough special characters from `string.punctuation`.
   - It checks if there are enough uppercase (`[A-Z]`) and lowercase (`[a-z]`) letters.

5. **Returning the Password**:  
   If the password meets all the constraints, it is returned as the final result.

6. **Main Execution Block**:  
   The script generates a password using the `generate_password()` function and prints the result. The `__name__ == '__main__'` block ensures that the password generation only occurs when the script is run directly (not imported as a module).
