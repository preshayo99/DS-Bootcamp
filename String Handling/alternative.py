""" This code asks users to input a sentence, it will produce a modified sentence with each alternate character as
 uppercase and the other character as lowercase.
 """

# Ask the user to input a sentence
sentence = input("Please enter your sentence: ")

modified_sentence = ""

# Loop iterates through each character of sentence along with its index
for i, char in enumerate(sentence):
    # To check if index is even
    if i % 2 == 0:
        # If the index is even, the character will be converted to lowercase and join the new sentence
        modified_sentence += char.lower()
    else:
        # If the index is odd, the character will be converted to uppercase and join the new sentence
        modified_sentence += char.upper()

# Print the modified sentence
print("Modified Sentence:", modified_sentence)
