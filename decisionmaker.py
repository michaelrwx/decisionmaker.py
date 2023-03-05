import random

def decision_maker(): #defining the decision making function
    choices = input("Enter your choices separated by commas: ")
    choices_list = choices.split(",") #Splitting the commas will allow the program to read the input without commas
    decision = random.choice(choices_list)
    print("That's it! Your decision is:",decision)

print("Let's make a decision...") #create suspense
decision_maker()
