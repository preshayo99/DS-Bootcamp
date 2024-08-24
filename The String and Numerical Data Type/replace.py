# Assign given sentence to variable called sentence
sentence = 'The!quick!brown!fox!jumps!over!the!lazy!dog.'

# Replace every '!' with a blank space using the replace() function, then print
replaced_sentence = sentence.replace('!', ' ')
print(replaced_sentence)

# Change sentence to all capitals using the upper function (), then print
uppercase_sentence = replaced_sentence.upper()
print(uppercase_sentence)

# Reverse sentence using slicing, then print
reversed_sentence = uppercase_sentence[::-1]

# Print the sentence in reverse
print(reversed_sentence)

