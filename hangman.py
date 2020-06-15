#  /--\
#  O  |
# -|- |
# / \ |
#_____/

import random
import re
import json

decision = input("Welcome to Hangman! Would you like to write your own phrases? If so, type o. If not, type r and play with one of 770 phrases: ")
if decision == "r":
  f = open('C:/Users/amias/OneDrive/Documents/Programming/Python/Hangman/phrases.json')
  data = json.load(f)
  phrases = data["phrases"]
  f.close()
  chosenPhraseIndex = random.randint(0,len(phrases)-1)
  chosenPhrase = phrases[chosenPhraseIndex].lower()
elif decision == "o":
  chosenPhrase = input("Type your phrase: ")
  chosenPhrase = chosenPhrase.lower()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def createBlank(charList):
  arr = []
  for char in charList:
    tester = re.match("\w", char)
    if tester:
      arr.append("_")
    else:
      arr.append(char)
  return arr

def joinList(blankCharList):
  string = ""
  for char in blankCharList:
    string = string + str(char)
    string = string + " "
  return string

charList = list(chosenPhrase) # split the word into chars
#print(charList)
blankCharList = [] # creates empty list
blankCharList = createBlank(charList) # fills blank list with underscores
#print(blankCharList)

info = {
  "lettersGuessed": "",
  "isHead": " ", # O      #  O
  "isBody": " ", # |      # -|-
  "isLeftArm": " ", # -   # / \
  "isRightArm": " ", # -
  "isLeftLeg": " ", # /
  "isRightLeg": " ", # \
  "incorrectIndex": 0,
  "finished": False,
  "failed": False,
  "correctness": ""
}


def hangman(info):
  if info["correctness"]:
    print("Correct!")
  elif info["correctness"] == False:
    print("Incorrect!")
  printOut = "  /--\ " + "Letters Guessed: " + info["lettersGuessed"] + "\n" + "  " + info["isHead"] + "  | " + "\n" + " " + info["isLeftArm"] + info["isBody"] + info["isRightArm"] + " | " + "\n" + " " + info["isLeftLeg"] + " " + info["isRightLeg"] + " | " + "\n" + "_____/ "
  print(printOut)
  hangmanWord = joinList(blankCharList) # concatenate the list into the blank hangman word
  print(hangmanWord)

  if info["finished"] == False:
    guess = input("Guess a Letter: ")
    correct = False
    info["correctness"] = False
    for i in range(len(charList)):
      letter = charList[i]
      if letter == guess:
        blankCharList[i] = letter
        correct = True
        info["correctness"] = True
    
    if correct == False:
      info["incorrectIndex"] += 1
      info["lettersGuessed"] += guess
      if info["incorrectIndex"] >= 1:
        info["isHead"] = "O"
      if info["incorrectIndex"] >= 2:
        info["isBody"] = "|"
      if info["incorrectIndex"] >= 3:
        info["isLeftLeg"] = "/"
      if info["incorrectIndex"] >= 4:
        info["isRightLeg"] = "\\"
      if info["incorrectIndex"] >= 5:
        info["isLeftArm"] = "-"
      if info["incorrectIndex"] >= 6:
        info["isRightArm"] = "-"
        info["finished"] = True
        info["failed"] = True

    for char in blankCharList:
      if char == "_":
        break
      else:
        pass
    else:
      info["finished"] = True

    hangman(info)

  else:
    if info["failed"]:
      print("You failed!\nThe phrase was: " + chosenPhrase)
    else:
      print("You did it! You got " + str(info["incorrectIndex"]) + " wrong.")

hangman(info)
