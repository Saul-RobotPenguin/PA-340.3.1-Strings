userWord = input("Please give me a word: ");
print(len(userWord));
print(userWord.upper())
print(userWord.lower())
letterToLookFor = input("Is there a letter that you want to look for in your word? ")

print("The letter " + letterToLookFor + " appears " + str(userWord.count(letterToLookFor)))


wordToLookFor = input("Now is there a word that you want to look for?")

print("The word " + wordToLookFor + " appears " + str(userWord.count(wordToLookFor)))


startingIndex = input("Please give me a starting index : ")

endingIndex = input ("Please give me an ending index: ")

print(userWord[startingIndex, endingIndex])

ubstring = input("Enter a substring: ")
print(f"'{substring}' appears {word.count(substring)} time(s) in '{word}'")

# Reversing the word
reverse_word = word[::-1]
print("Reverse:", reverse_word)

# Slicing the word
start_index = int(input("Enter a starting index: "))
end_index = int(input("Enter an ending index: "))
sliced_word = word[start_index:end_index]
print("Sliced word:", sliced_word)

# Replacing a character
char_to_replace = input("Enter a character to replace: ")
replacement_char = input("Enter the replacement character: ")
new_word = word.replace(char_to_replace, replacement_char, 1)
print("Replaced:", new_word)

# Concatenating with another word
second_word = input("Enter a second word: ")
concatenated_word = word + second_word
print("Concatenated:", concatenated_word)

# Checking for palindrome and valid identifier
is_palindrome = word == reverse_word
is_valid_identifier = word.isidentifier()

print("Is a palindrome?", is_palindrome)
print("Is a valid Python identifier?", is_valid_identifier)
