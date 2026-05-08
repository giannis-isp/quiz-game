import json #importing json module for loading the JSON questionaire file
import random #for random choices 

#loading the json file
with open("questions.json", "r") as file:
    data  = json.load(file)


#creating a class
class Game:
    #class variable of points
    credit_score = 100

    #creating the player profile. Could add more attributes like age, gender etc
    def __init__(self, player):
        self.player = player
        
    #just testing @classmethods
    @classmethod
    def score(cls):
        if cls.credit_score >= 1000:
            print("You Won!")
            exit()
        elif cls.credit_score <= 0:
            print("You lost. Better luck next time.")
            exit()



    def questions(self):
        #taking all the keys from the data file and storing them as a list in a variable
        categories = list(data.keys())
        #enumerating each ctegory in the list for better readability 
        for i, option in enumerate(categories, start=1):
            print(f"{i}. {option}")   


        while True:
            try:#error handling in case user types something other than an integer
                category = int(input("Choose your category (1-7): "))
              
                if category >= 1 and category <=7:
                    break
                else:
                    print("Choose a category between 1 and 7")#error handling if user types an integer out of 1-7 range

            except ValueError:
                print("Incorrect input, try again")

        category = categories[category -1]#list items are stored in numbers starting from 0, so if the user chooses 1 he means the option 0 in programming langauage
        question = random.choice(data[category])#choosing a random question from the category chosen previously

        return question["question"], question["options"], question["answer"]




    def options(self, options):
        for i, opt in enumerate(options, start=1):#giving the user the options for the question, enumerated for better readability
            print(f"{i}: {opt}")
            


    def answers(self, answer, user_input, options):#user_input is a variable in the main code
            if user_input < 1 or user_input > 4: #error handling if user input is out of range 1-4
                print(">>>Incorrect option<<<\n")
                return None #return None so the function closes without giving anything back to the main code
        
            selected_option = options[user_input - 1] 

            if selected_option == answer: #if user input is the same option as the answer
                print("Correct\n")
                Game.credit_score += 100
            else:
                print(f"Incorrect, the correct answer is {answer}")
                Game.credit_score -= 100 #if user input is not the same option as the answer

            






