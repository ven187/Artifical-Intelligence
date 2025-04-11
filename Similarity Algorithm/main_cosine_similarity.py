import numpy as np
import re

def hex_to_rgb(hex_code):
    """Converts HEX color code to (R, G, B) format."""
    hex_code = hex_code.strip("\"[]")  # Clean quotes and square brackets
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def load_colors(filename):
    """Loads named colors from file."""
    colors = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                match = re.match(r'\[\"([0-9A-Fa-f]{6})\", \"(.+?)\"\]', line.strip())
                if match:
                    hex_code, name = match.groups()
                    colors[name] = hex_to_rgb(hex_code)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return colors

def arrange(item, dim, min_val, max_val):
    """Compresses RGB values to 0-100 range."""
    item = list(item)
    for i in range(dim):
        item[i] = item[i] / ((max_val - min_val) / 100)  # Convert to percentage value
    return item

def cosine_similarity(A, B):
    """Calculates the cosine similarity between two colors."""
    dot_product = sum(a*b for a, b in zip(A, B))  # Dot product between vectors
    norm_a = sum(a**2 for a in A) ** 0.5  # Norm of A
    norm_b = sum(b**2 for b in B) ** 0.5  # Norm of B
    return dot_product / (norm_a * norm_b)  # Cosine Similarity

def find_closest_color(input_color, colors):
    """Returns the name of the closest color to the input RGB value and its similarity ratio."""
    if not colors:
        return None
    
    input_normalized = arrange(input_color, 3, 0, 255)
    closest_color = None
    highest_similarity = -1
    
    for name, color in colors.items():
        color_normalized = arrange(color, 3, 0, 255)
        similarity = cosine_similarity(input_normalized, color_normalized)
        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_color = (name, color, similarity)
    
    return closest_color

# Get color input from user
r = int(input("R (0-255): "))
g = int(input("G (0-255): "))
b = int(input("B (0-255): "))

# Load color list
colors = load_colors("colors.txt")

# Find closest color and similarity ratio
result = find_closest_color((r, g, b), colors)

if result:
    closest_name, closest_rgb, similarity = result
    print(f"Closest color: {closest_name} - RGB: {closest_rgb} - Similarity: {similarity * 100:.2f}%")
else:
    print("No suitable color found or color file is invalid.")