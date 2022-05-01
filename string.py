# 1. Write a Python program to calculate the length of a string.
print(len("Hello World"))

# 2. Write a Python program to count the number of characters (character frequency) in a string

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from
# a given a string. If the string length is less than 2, return instead of the empty string.

# 4. Write a Python program to get a string from a given string where all occurrences of
# its first char have been changed to '$', except the first char itself.

# 5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
# given string is less than 3, leave it unchanged.

sample6 = input("Enter word: ")
if not len(sample6) < 3:
    if sample6.__contains__("ing"):
        print(sample6 + "ly")
    else:
        print(sample6 + "ing")
else:
    print(sample6)


# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
sample7 = "They lyrics is not tha poor. The lyrics is poor."

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
sample8 = ["Leigh", "Inna", "Jamolin", "BSCS", "Random", "Pneumonoultra", "Programming", "Do"]

# 9. Write a Python program to remove the nth index character from a nonempty string.
sample9 = input("Enter word: ")

# 10. Write a Python program to change a given string to a new string
# where the first and last chars have been exchanged.


# 11. Write a Python program to remove the characters which have odd index values of a given string.


# 12. Write a Python program to count the occurrences of each word in a given sentence.
sample12 = "It was getting dark, and we weren’t there yet. " \
           "No matter how beautiful the sunset, it saddened her knowing she was one day older." \
           "The miniature pet elephant became the envy of the neighborhood."
sample12 = list[sample12]
print(sample12)