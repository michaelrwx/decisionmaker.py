import time
import random


print("Let's make a decision...\n") #create suspense

number = int(input("How many things are you comparing? \n")) #user input 

strnum = str(number) #puts this decision in a variable

print("You are deciding between " +strnum+ " things. The last thing is your decision.")
time.sleep(1)

print("Calculating Decision: ")

for i in range(number):
    decision = str(random.randrange(number) + 1) #We don't want 0's because that makes no sense to anyone else lol
    print(decision) #honestly this is here to create more suspense
    time.sleep(0.5) #makes the program look neat

print("That's it! Your decision is: " +decision)