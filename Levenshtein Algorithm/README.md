# Weighted Levenshtein Distance Calculator

This Python project calculates the similarity between two words using a **Q keyboard layout-based weighted Levenshtein algorithm**. It provides a more realistic spelling similarity assessment based on the physical distance between letters.

## Features

- **Q keyboard** map-based letter distance calculation
- Weighted distance evaluation for letter substitutions
- Standard deletion and insertion operations (cost: 1)
- Lower substitution costs for smaller distances:
  - Same letter → 0.0
  - Nearby letters → 0.25 or 0.5
  - Distant letters → 1.0

## Usage

When you run the program, it will ask you to enter two words. The **weighted Levenshtein distance** and **similarity ratio** between the entered words will be calculated and displayed.

### Example:

word: word

word: wrod

Weighted Levenshtein Distance: 0.50
Similarity Ratio: 0.92

## Requirements

- Python 3.x  
- NumPy

To install the required library:

pip install numpy

## License

This project is open source. You can use, modify, and share it as you wish.