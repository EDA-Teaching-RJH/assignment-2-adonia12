### Part Two -- your code goes here. 
import random 
guessnum = random.randint(1,100)
usernumber = None
while usernumber != guessnum:
    usernumber = int(input("Guess a number between 1 and 100   "))
    if usernumber < guessnum:
        print("Too low! Try again.")
    elif usernumber  > guessnum:
        print("Too high! Try again.")
    else:
        print("You've guessed the correct number.")
