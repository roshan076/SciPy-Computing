# Luhn Algorithm

This module contains a Python implementation to validate credit card numbers using the ***Luhn Algorithm***, a checksum formula used to validate various identification numbers, such as credit card numbers. The program checks if a given card number is valid or not based on the Luhn algorithm.

---

## Features

- **Card Number Input**: The program accepts credit card numbers with or without dashes (`-`) or spaces (` `).
- **Luhn Algorithm**: It implements the Luhn algorithm, which involves reversing the digits, summing odd digits and processing even digits with a doubling and checksum step to determine if the number is valid.

---

## How It Works

### Algorithm Details:
1. **Reversal of Card Number**: The digits of the card number are reversed for easier processing.
2. **Sum Odd Digits**: The digits at odd positions (after reversing) are summed.
3. **Sum Even Digits**: The digits at even positions (after reversing) are doubled. If doubling results in a number greater than 9, the digits of that number are added together.
4. **Checksum Calculation**: The final checksum is calculated by adding the sums of the odd and even digits.
5. **Validation**: If the total sum is divisible by 10, the card number is considered valid.