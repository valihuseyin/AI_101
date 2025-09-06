# Pseudo-code:
# 1. Ask the user to input a string with multiple words.
# 2. Split the string into a list of words using space as the separator.
# 3. Reverse the list of words.
# 4. Join the reversed list back into a string with spaces.
# 5. Print the resulting string.

def reverse_words_in_string():
    user_input = input("Enter a string with multiple words: ")
    words = user_input.split(' ')
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    print(result)

if __name__ == "__main__":
    reverse_words_in_string()