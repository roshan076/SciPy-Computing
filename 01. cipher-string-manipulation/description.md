# Cipher String Manipulation

---

This module contains Python implementations of two classic cryptographic algorithms: ***Caesar Cipher*** and ***Vigenère Cipher***. These algorithms are used to encrypt and decrypt text by shifting letters in the alphabet.

---

## Features

- **Caesar Cipher**: A substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.
  - Supports encryption with a specified shift value.
  - Encrypts lowercase alphabetic text and maintains spaces.

- **Vigenère Cipher**: A more complex substitution cipher that uses a keyword to determine the shift for each letter.
  - Supports both encryption and decryption.
  - Handles messages with non-alphabetic characters (they are preserved).
  - Supports case-insensitive text and cyclic key usage.


---

## Usage

### Caesar Cipher
The Caesar cipher is used by calling the `caesar()` function. It takes two arguments:
- `message`: The text to be encrypted.
- `offset`: The number of positions to shift the alphabet.

### Vigenère Cipher
The Vigenère Cipher is used by calling the `vigenere()` function. It takes three arguments:
- `message`: The text to be encrypted/decrypted.
- `key`: Key used to encrypt/decrypt the message.
- `direction`: Default value 1 for straight process.