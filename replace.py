# ========= Task 2 ===========
# Pseudocode:
# Save the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog." as a string
# Replace ! exclamation mark with " " a blank space and print
# Use the function .upper() and reprint out the sentence in UPPERCASE
# Use the extended slice [begin:end:step] to reprint the sentence in reverse [::-1]


# Practical Task 2:
# Assigning the text to the variable sentence
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

replace_sentence= sentence.replace("!" , " ") # new sentence replacing ! exclamatation marks with spaces
print(replace_sentence) # prints out The quick brown fox jumps over the lazy dog.

upper_sentence = replace_sentence.upper() # converts replace_sentence into upper case
print(upper_sentence) # prints out THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

print(upper_sentence[::-1]) # prints out .GOD YZAL EHT REVO SPMUJ XOF NWORB KCIUQ EHT (sentence in reverse)