def count_words(input_string):
    words = input_string.split()
    return len(words)

# Example usage:
input_str = "Hello, this is a sample string."
word_count = count_words(input_str)
print(f"The number of words in the string is: {word_count}")