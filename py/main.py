import random

def init(rightAnswer):
  userInput = input('Guess the number: ')  
  userInput = int(userInput)

  if (userInput > rightAnswer):
    print("The number is smaller than {}".format(userInput))
    init(rightAnswer)

  if userInput < rightAnswer:
    print("The number is bigger than {}".format(userInput))
    init(rightAnswer)

  if userInput == rightAnswer:
    print("You win!")

init(random.randint(1, 100))
