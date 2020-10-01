

from random import randint
def game():
    guesses = 1
    Min = int(input("Enter minimum number"))
    Max = int(input("Enter maximum number"))
    number = randint(Min,Max)
    guess_limit = 5
    out_of_guesses = False

    print("Guess a number between", Min, " and", Max )
    x = int(input())

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
    



game()
while True:
    print("Would do you like to play again? ")
    a = input("Enter 'yes' or 'no' ")
    if a == 'yes':
        game()
    else:
        print("good bye")
        break
   

 





