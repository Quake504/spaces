# Libraries
import os

# Main Code
def space():
  word = input("Input a word: ")
  os.system("cls")
  print("This is the result")
  print(word.replace(""," "))
  
  # Calling the function
  space()
