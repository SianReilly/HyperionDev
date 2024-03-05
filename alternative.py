# ========= Task 1.1 ===========
# This function reads alternate characters as upper and lower case string (s)

def alternate_character_case(s):
    new_str = "" 
    for i in range(len(s)): # For Loop iterates over indices of the string (len(s)) = length of string
        if i % 2 == 0:  # Used the modulus (%) to check if the index is even or odd
            new_str += s[i].upper() # If even = uppercase character, odd = lowercase character and appended to empty list (new_str)
        else:
            new_str += s[i].lower()
    return new_str

# Code inputted as string, returned alternately character cased via calling the above function.
input_str = input("Please enter a string to be alternatively character cased!")
alt_char = alternate_character_case(input_str)
print(alt_char)




# ========= Task 1.2 ===========
# This function reads alternate words as upper and lower case as upper and lower case string (s)

def alternate_word_case(s):
    words = s.split()   # Words are split into a list of words via 's.split()'
    new_words = []  # Empty list to store the alternately cased words (new_words)
    for i in range(len(words)): # For Loop iterates over indices of the string (len(s)) = length of string
        if i % 2 == 0:  # Used the modulus (%) to check if the index is even or odd
            new_words.append(words[i].lower())  # If even = uppercase word, odd = lowercase word and appended to empty list (new_words)
        else:
            new_words.append(words[i].upper())
    return " ".join(new_words)  # After all words have been appended to new_words, a join is used to combine them separated by a space " "


# Code inputted as string, returned alternatively word cased via calling the above function.
input_str = input("Please enter a string to be alternatively word cased!")
alt_word = alternate_word_case(input_str)
print(alt_word)