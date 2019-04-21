"""

This is a Codecademy project!

Pig Latin is a language game, where you move the first letter of the word to the end and add ay. So Python becomes ythonpay. To write a Pig Latin translator in Python, here are the steps well need to take:

Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English to Pig Latin.
Display the translation result.

"""

print('\nWelcome to the Pig Latin Translator!\n')

# Start coding here!

pyg = "ay"

original = input("Enter a word: ")

if len(original) > 0 and original.isalpha():
  #print(original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print("\n" + new_word + "\n")
else:
  print("\nString is empty or contains numeric characters\n")
