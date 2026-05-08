import json
import random
from game import Game #importing the backend code for the game


with open("questions.json", "r") as file:
    data  = json.load(file) #again loading the json file

#introduction
print("Welcome to 'Who wants to be a GAZILLIONAIRE!'")
print()
print("Here are the categories of the questions: ")
print("------------------")

#player attribute from the __init__ function
gaming = Game(player=input("Enter your name: ").title())
print(f"Hello {gaming.player}")


print("Your credits: ")
print(Game.credit_score)
print()

#using a while loop so the program does not end after a single question
while True:
    q, o, a = gaming.questions() #loading all questions, options and answers in gaming.questions()
    print()
    print(q) #printing a question
    print("----------------------")
    gaming.options(o) #giving the options for that specific question
    print()

    while True:
        try: #error handling in case of an input other than an integer
            user_input = int(input("Enter your answer: "))
            break
        except ValueError:
            print("Please enter a valid number")

    gaming.answers(a, user_input, o)#calling the answer function to check if the players answer is correct or not
    Game.score() #calling the score function after every question to update the credit score and check if the player won or lost

    #showing the player his current credit score
    print("Your credits: ")
    print(Game.credit_score)
    print()

