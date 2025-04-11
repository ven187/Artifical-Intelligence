import numpy as np

# QWERTY keyboard map (x: horizontal, y: vertical)
qwerty_map = {
    'q': (0, 0), 'w': (1, 0), 'e': (2, 0), 'r': (3, 0), 't': (4, 0), 'y': (5, 0), 'u': (6, 0), 'i': (7, 0), 'o': (8, 0), 'p': (9, 0),
    'a': (0.5, 1), 's': (1.5, 1), 'd': (2.5, 1), 'f': (3.5, 1), 'g': (4.5, 1), 'h': (5.5, 1), 'j': (6.5, 1), 'k': (7.5, 1), 'l': (8.5, 1),
    'z': (1, 2), 'x': (2, 2), 'c': (3, 2), 'v': (4, 2), 'b': (5, 2), 'n': (6, 2), 'm': (7, 2)
}

def letter_distance(l1, l2):
    if l1 == l2:
        return 0.0
    l1 = l1.lower()
    l2 = l2.lower()
    if l1 not in qwerty_map or l2 not in qwerty_map:
        return 1.0  # unknown character → max penalty
    x1, y1 = qwerty_map[l1]
    x2, y2 = qwerty_map[l2]
    distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    if distance < 1:
        return 0.25
    elif distance < 2:
        return 0.5
    else:
        return 1.0

def weighted_levenshtein(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = np.zeros((len1 + 1, len2 + 1))

    for i in range(len1 + 1):
        dp[i][0] = i  # deletion = 1 point
    for j in range(len2 + 1):
        dp[0][j] = j  # insertion = 1 point

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = letter_distance(s1[i - 1], s2[j - 1])
            dp[i][j] = min(
                dp[i - 1][j] + 1,         # deletion
                dp[i][j - 1] + 1,         # insertion
                dp[i - 1][j - 1] + cost   # substitution (weighted)
            )

    return dp[len1][len2]


if __name__ == "__main__":
    word1 = input("1st word: ")
    word2 = input("2nd word: ")

    distance = weighted_levenshtein(word1, word2)
    max_len = max(len(word1), len(word2))
    similarity = (max_len - distance) / max_len

    print(f"\nWeighted Levenshtein Distance: {distance:.2f}")
    print(f"Similarity Ratio: {similarity:.2f}")
