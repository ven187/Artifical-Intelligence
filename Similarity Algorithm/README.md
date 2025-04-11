# RGB Color Similarity Calculation Project

This repository contains two Python algorithms that calculate RGB color similarity using **two different methods**:
- **Euclidean Distance** based method
- **Cosine Similarity** based method

Both methods aim to match a user-input RGB value with the closest color from a predefined list of colors in a file and calculate the similarity ratio (percentage).

---

## Project Content

### 1. Euclidean Distance Based Method
- **Purpose:** Evaluates RGB colors spatially and calculates the difference between two colors using Euclidean distance.
- **Calculation:**  
  \[
  d(A, B) = \sqrt{(R_A - R_B)^2 + (G_A - G_B)^2 + (B_A - B_B)^2}
  \]
- **Normalization:** Normalized against maximum distance to obtain **similarity ratio**:
  
similarity = 1 - (distance / max_distance)

### 2. Cosine Similarity Based Method
- **Purpose:** Measures the angle (orientation) between two color vectors to determine their **directional similarity**.
- **Calculation:**  
\[
\text{Cosine Similarity}(A, B) = \frac{A \cdot B}{||A|| \cdot ||B||}
\]
- **Feature:** This method focuses on the **direction** of color vectors rather than their magnitude.

---

## File Structure

/repo_root │ ├── euclidean_color_similarity.py # Color similarity calculation using Euclidean Distance ├── cosine_color_similarity.py # Color similarity calculation using Cosine Similarity ├── colors.txt # File containing color HEX codes and names └── README.md # This file

**colors.txt** file example format:
["FF5733", "Red"] ["33FF57", "Green"] ["3357FF", "Blue"]

Each line contains a color code (6-digit HEX) and color name.

---

## Features and Functions

Common helper functions used in both methods:

- **hex_to_rgb(hex_code):**  
  Converts HEX color code to (R, G, B) format.
  
- **load_colors(filename):**  
  Loads colors with their names from the specified file.
  
- **arrange(item, dim, min_val, max_val):**  
  Normalizes RGB values to 0-100 range. This step provides a common scale for comparison.

### Additional Functions in Euclidean Method:
- **kokal(x):**  
  Performs square root calculation.
  
- **usal(x, level):**  
  Performs power calculation.
  
- **vectorSimilarity(A, B):**  
  Calculates Euclidean distance between two color vectors and converts it to similarity ratio.
  
- **find_closest_color(input_color, colors):**  
  Compares input color with each color in the list and returns the closest color and similarity ratio.

### Additional Functions in Cosine Method:
- **cosine_similarity(A, B):**  
  Calculates dot product and norms to provide Cosine Similarity result.
  
- **find_closest_color(input_color, colors):**  
  Compares normalized input color with normalized colors from file and returns color with highest Cosine Similarity ratio.

---

## Usage Steps

1. **Prepare Color File:**  
   Create your `colors.txt` file in the format above or check the format of existing file.

2. **Install Required Libraries:**  
   Python 3.x and NumPy are required. To install NumPy:
pip install numpy

3. **Run the Codes:**

- **For Euclidean Method:**  
  ```
  python euclidean_color_similarity.py
  ```

- **For Cosine Method:**  
  ```
  python cosine_color_similarity.py
  ```

4. **Provide Color Inputs:**  
The program will ask for R, G, B values (between 0-255).  
Example:
R (0-255): 150 G (0-255): 75 B (0-255): 200

5. **Results:**  
The program will display the closest color name, RGB value, and similarity ratio as percentage.

---

## Example Outputs

### Euclidean Distance Method:
R (0-255): 150 G (0-255): 75 B (0-255): 200

Closest color: SkyBlue - RGB: (135, 206, 235) - Similarity: 85.43%

### Cosine Similarity Method:
R (0-255): 150 G (0-255): 75 B (0-255): 200

Closest color: SkyBlue - RGB: (135, 206, 235) - Similarity: 92.10%

*Note: Similarity ratios may vary depending on the method used, normalization, and dataset.*

---

## Comparison: Euclidean Distance vs Cosine Similarity

| Criterion              | Euclidean Distance                                   | Cosine Similarity                          |
|------------------------|---------------------------------------------------|--------------------------------------------|
| **Definition**         | Measures straight-line distance between two points  | Measures angle between two vectors         |
| **Calculation**        | Square root of sum of squared differences          | Ratio of dot product to product of norms   |
| **Feature**            | Measures physical distance, magnitude matters      | Focuses on directional similarity, scale-independent|
| **Use Cases**          | Physical location, k-means clustering              | Text similarity, direction-focused vector comparison|

---

## License

This project is open source and can be freely used, modified, and shared by developers. You can freely use the code in your own projects.