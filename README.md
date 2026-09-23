Password Strength Analyzer and Custom Wordlist Generator

## Introduction

This project is a Python-based cybersecurity project that analyzes password strength and generates a custom wordlist using user-provided test information.

The project helps demonstrate basic concepts of password security and wordlist generation.

## Abstract

The Password Strength Analyzer checks a password and evaluates its strength based on factors such as length, character types, and commonly used password patterns.

The Custom Wordlist Generator creates a list of possible test words by combining inputs such as a name, pet name, and year.

This project is developed for educational and cybersecurity learning purposes.

## Objective

- To analyze the strength of passwords.
- To identify weak and strong password characteristics.
- To generate a customized wordlist from test inputs.
- To understand basic password-security concepts.
- To practice Python programming for cybersecurity applications.

## Tools Used

- Python
- Pydroid 3
- zxcvbn Python library
- GitHub

## Features

### 1. Password Strength Analyzer

The analyzer accepts a test password and displays:

- Password length
- Strength
- Score
- Suggestions or feedback

### 2. Custom Wordlist Generator

The wordlist generator accepts:

- Name
- Pet name
- Year

It generates combinations such as:

- Name
- Pet name
- Year
- Name + Year
- Pet name + Year
- Name + Pet name
- Name + 123
- Pet name + 123
- Name + @ + Year
- Pet name + @ + Year

The generated words are saved in `custom_wordlist.txt`.

## Steps Involved

1. Install Python/Pydroid 3.
2. Install the required `zxcvbn` library.
3. Create the Password Strength Analyzer.
4. Test the analyzer with sample passwords.
5. Create the Custom Wordlist Generator.
6. Generate a test wordlist.
7. Save the generated words into `custom_wordlist.txt`.
8. Test the complete project.
9. Upload the Python file, wordlist, and screenshots to GitHub.

## Project Files

- `password_analyzer.py` — Python source code.
- `custom_wordlist.txt` — Generated test wordlist.
- Project screenshots — Evidence of the project execution.

## Conclusion

This project demonstrates how Python can be used to analyze password strength and generate customized test wordlists. It provides practical experience with Python programming, password-security concepts, file handling, and basic cybersecurity techniques.
