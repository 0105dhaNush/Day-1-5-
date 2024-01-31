def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    total_vowels = 0
    vowel_counts = { vowel:0 for vowel in vowels}

    for char in input_string:
        if char in vowels:
            total_vowels+=1
            vowel_counts[char.upper()]+=1



