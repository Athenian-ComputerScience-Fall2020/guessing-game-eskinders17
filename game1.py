#collaboraters - https://www.youtube.com/watch?v=KdMAj8Et4xk
# Megan Leich

from random import randint
def game():

    guesses = 1 #guessing starts from 1
    guess_limit = 5 #user can only try 5 times
    out_of_guesses = False #

    try:
        Min = int(input("Enter minimum number: "))
        Max = int(input("Enter maximum number: "))
        number = randint(Min,Max)
        print("Guess a number between", Min, " and", Max )
    except:
        print()
        print("Invalid Input, Please start again")
        print()
        game()

    try:
        x = int(input("Gueess Here: "))
    except:
        print()
        print("Invalid Input, please start again")
        print()
        game()
    #while x != number and not(out_of_guesses):
            #print("try again")
            #game()
        #else:
            #print("congratttts")     
    #except:
        #print("Invalid Input, Please try again")
        #print()
        #game()
        #while guesses < guess_limit:
    while x != number and not(out_of_guesses):
        if x < number:
            try:
                if guesses < guess_limit:
                    print("Your number is too low.")
                    x = int(input("Please guess again: "))
                    guesses = guesses + 1
                else:
                    out_of_guesses = True
            except:
                print("Invalid Input, Please try again")
                print()
        elif x > number:
            try:
                if guesses < guess_limit:
                    print("Your number is too high.") 
                    x = int(input("PLease guess again: ")) 
                    guesses = guesses + 1
                else:
                    out_of_guesses = True
            except:    
                print("Invalid Input, Please try again")
                print()
        #else:
            #out_of_guesses = True 
        #if out_of_guesses:
            #print("Game over, you are out of guesses")
            
    if out_of_guesses:
        print()
        print("Sorry, you are out of guesses!!")
        print()
        game()
    else:
        print()
        print("Congrats, you guessed the number! ")
        print("It only took you", guesses, "guesses!")

    
    #if out_of_guesses:
    #        print("Game over, you are out of guesses")
    #        game()
        
game()
while True:
    print("Would do you like to play again?: ")
    a = input("Enter 'yes' or 'no': ")
    if a == 'yes':
        game()
    else:
        print("good bye")
        break
        
            

 





