

from random import randint
guesses = 1
number = randint(1,10)
guess_limit = 5
out_of_guesses = False

x = int(input("Guess a number between 1 and 10: "))

while x != number and not(out_of_guesses):

    if guesses < guess_limit:

     if x < number:
        print("Your number is too low.")
        x = int(input("Please guess again: "))
        guesses = guesses + 1
     elif x > number:
        print("Your number is too high.") 
        x = int(input("PLease guess again: ")) 
        guesses = guesses + 1
    else:
        out_of_guesses = True  
   
if out_of_guesses:
    print()
    print("Game over, you are out of guesses")
else:
 print()
 print("Congrats, you guessed the number! ")
 print("It only took you", guesses, "guesses!")
# Collaborators: none





