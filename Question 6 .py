def longest_common_substring(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    # Create a matrix to store lengths of the common suffixes
    matrix = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

    # Variables to keep track of the length and end position of the longest common substring
    max_length = 0
    end_position = 0

    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_position = i
            else:
                matrix[i][j] = 0

    # Extract the longest common substring
    longest_common_substring = str1[end_position - max_length: end_position]

    return longest_common_substring

# Example usage:
str1 = "abcdef"
str2 = "abxyzef"
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)