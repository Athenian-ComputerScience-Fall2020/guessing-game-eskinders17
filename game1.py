

from random import randint
guesses = 1
number = randint(1,10)

x = int(input("Guess a number between 1 and 10: "))

while x != number:
    
    if x < number:
        print("Your number is too low.")
        x = int(input("Please guess again: "))
        guesses = guesses + 1
    elif x > number:
        print("Your number is too high.") 
        x = int(input("PLease guess again: ")) 
        guesses = guesses + 1
   
          
print()
print("Congrats, you guessed the number! ")
print("It only took you", guesses, "guesses!")
# Collaborators: none





