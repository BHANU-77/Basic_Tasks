import random
import time

def greet_player():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def play_game():
    guesses_taken = 0
    while guesses_taken < 6:
        time.sleep(0.25)
        user_input = input("Guess: ")
        try:
            guess = int(user_input)
            if 1 <= guess <= 200:
                guesses_taken += 1
                if guesses_taken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(0.5)
                        print("Try Again!")
                if guess == number:
                    break
            elif guess > 200 or guess < 1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")
        except ValueError:
            print("I don't think that " + user_input + " is a number. Sorry")

    if guess == number:
        guesses_taken = str(guesses_taken)
        print('Good job, ' + name + '! You guessed my number in ' + guesses_taken + ' guesses!')
    elif guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    greet_player()
    play_game()
    print("Do you want to play again?")
    play_again = input()
