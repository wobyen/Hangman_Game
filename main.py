
import random

wordList = ["aardvark", "poop", "stupid"]

#picks a random number from the list
chosenWord = wordList[random.randint(0,2)]
print(chosenWord)

#finds out how many letters are in the word
lettersInWord = len(chosenWord)

#creates the game
def createWord(numOfLetters):

  hangMan = "_" * numOfLetters
  print(hangMan)
  print("") 
  return hangMan

validGuess = False

newWord = createWord(lettersInWord)

while newWord.count("_") > 0:

  while validGuess == False:
      guess = input("Guess a letter: ")
    
      if len(guess) > 1:
        print("You can only guess one letter.\n")

      else:
        print("\nYou guessed " + guess)
        validGuess = True

  newLetters = []
  i = 0


  for letter in chosenWord:
    if letter == guess:
     # print(guess)
      newLetters.append(guess)
      i += 1
    else:
     # print(newWord[i])
      newLetters.append(newWord[i])
      i += 1

  #print(newLetters)

  newword = ""
  fart = ""
  newWord = fart.join(newLetters)

  print(newWord + "\n\n")

  validGuess = False

print("You Win!")












