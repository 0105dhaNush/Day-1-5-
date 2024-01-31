def most_frequent_character(input_str):
    char_count = {}

    # Count the occurrences of each character in the string
    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the character with the maximum count
    most_frequent_char = max(char_count, key=char_count.get)

    return most_frequent_char

# Example usage:
input_string = "programming is fun"
result = most_frequent_character(input_string)
print("Most frequent character:", result)