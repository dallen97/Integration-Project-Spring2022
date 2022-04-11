# Dustin Allen
# Program Description- This program will become a short text based quiz
# adventure. basically a quiz with extra steps
# sprint 1 goal is to create basic start and  some calculations
# sprint 2 goal is to create multiple phases in the adventure
# sprint 3 goal is to have adventure complete with
# one battle and an ending


playerName = input("Please enter a chosen name ")
print("Welcome" + " " + playerName, end=" ")
print("to an unnamed text based adventure game \n")

print("insert story stuff here \n")

# Menu of difficulty choices for the player to choose
1.Easy - Allowed to get 3 questions wrong.
2.Medium - You are allowed to get 2 questions wrong.
3.Hard - You are allowed to get 1 question wrong

# if statements for quiz difficulty choices
# added while loop to contain invalid choices

# lives below refers to amount of wrong answers a player can get if lives hit 0
# during a quiz then the game terminates with a Game Over
lives = 0

DifficultySelect = input("\n1.Easy - Allowed to get 3 questions wrong."
                  "\n2.Medium - You are allowed to get 2 questions wrong."
                  "\n3.Hard - You are allowed to get 1 question wrong"
                  "\nPlease select a character bonus from the list above. ")
while DifficultySelect < "1" or DifficultySelect > "4":
    DifficultySelect = input("Invalid choice. Please try again. ")
if DifficultySelect == "1":
    print("You have chosen easy difficulty.")
    lives = int(3)
elif DifficultySelect == "2":
    print("You have chosen medium difficulty.")
    lives = int(2)
elif DifficultySelect == "3":
    print("You have chosen hard difficulty.")
    lives = int(1)

print("\nThe adventure is now starting")
print("\nYour number of lives is", lives)

# Below starts the adventure with some flavor dialogue
print("\nLooking at your surroundings, you notice three paths before you."
      "There are two doors on either side of the room you are in while "
      "in front of you is a long dark corridor with a locked door at the end."
      " Your intution tells you that it would be"
      "best to inspect the rooms to your side before pushing ahead.")
print("\nBased on the door locks you decide that it would be best to"
      "investigate the room on your left first and then the room on the right"
      "before attempting to unlock the door.")
# Each room will contain a short quiz with the final room containing a 3 part
# quiz encounter to end the adventure
# Below is the templates for each room. Each room will have two look around or
# inspection options with the final third option being the small room quiz
# up to two actions are allowed in the room
print('\n insert first room stuff here')
room1 = 0
# range function is to allow instant quiz option or to prevent the user from
# only pressing options one and two thus softlocking themselves into not
# proceeding into the quiz
for room1 in range(0, 1):
    choice1 = input("choose 1. 2. or 3.")

    while not (choice1 == "1" or choice1 == "2" or choice1 == "3"):
        choice1 = input("\n invalid choice. choose again")
    if choice1 == "1":
        print("\n choice 1")
        choice1 = input("choose 1. 2. or 3.")
        room1 = room1 + 1
    if choice1 == "2":
        print("\n choice 2")
        choice1 = input("choose 1. 2. or 3.")
        room1 = room1 + 1
    if choice1 == "3":
        print("\n choice 3")
        room1 = room1 + 3

print("\nroom 1 quiz here")

print('\n insert first room stuff here')
room2 = 0

for room2 in range(0, 1):
    choice2 = input("choose 1. 2. or 3.")

    while not (choice2 == "1" or choice2 == "2" or choice2 == "3"):
        choice2 = input("\n invalid choice. choose again")
    if choice2 == "1":
        print("\n choice 1")
        choice2 = input("choose 1. 2. or 3.")
        room2 = room2 + 1
    if choice2 == "2":
        print("\n choice 2")
        choice2 = input("choose 1. 2. or 3.")
        room2 = room2 + 1
    if choice2 == "3":
        print("\n choice 3")
        room2 = room2 + 3

print("\nroom 2 quiz here")

print('\n insert first room stuff here')
room3 = 0

for room3 in range(0, 1):
    choice3 = input("choose 1. 2. or 3.")

    while not (choice3 == "1" or choice3 == "2" or choice3 == "3"):
        choice3 = input("\n invalid choice. choose again")
    if choice3 == "1":
        print("\n choice 1")
        choice3 = input("choose 1. 2. or 3.")
        room3 = room3 + 1
    if choice3 == "2":
        print("\n choice 2")
        choice3 = input("choose 1. 2. or 3.")
        room3 = room3 + 1
    if choice3 == "3":
        print("\n choice 3")
        room3 = room3 + 3

print("\nroom 3 quiz here")

#below is the quiz template

# This is the for the end of the quiz adventure. It displays the
# congratulations message along with number of correct questions and percentage
# of questions that were correct 
correctQuestions= 6
questionTotal = 6
# the loop is to test to make sure it works with multiple numbers
for loop in range (0,5):
    if quizQuestions > 0:
        quiz_average = quizQuestions / questionTotal
        quiz_averages = "{:.0%}".format(quiz_average)
        print("Congratulations you passed the quiz adventure! Your number of correct answers is", quizQuestions)
        print("Your percentage of correct answers is", quiz_averages)
    else:
        print("You have failed the adventure. Game Over")
    quizQuestions = quizQuestions - 1
    loop += 1

# below is for integration project requirements

# modulus
print("\nThe following displays modulus of 35%5 which is equal to", 35 % 5)

# floor division
print("The following displays floor division of 75//2 which equals", 75 // 2)

# below is for integration project string operator requirement
repeatString = int(
    input("\nChoose number of times to repeat the phrase Hello! "))
print("Hello! " * repeatString)


# below is a defined statement for the gift shop that will be implemented
# this will be moved to a line above to ensure the call will work when needed
#before the first room
def gameShop():
    print("Welcome to the gift shop")
    print("Here is a list of available items \n1. Health Potion - this item"
          "adds one life to your lives counter")
    print("\n2. Recieve nothing and leave the shop")
    playerChoice = input("Please choose an option from the list above: ")
    while not(playerChoice == "2" or playerChoice == "1"):
        playerChoice = input("Invalid choice."
                             "Please choose an option from the list")
    if playerChoice == "1":
        lives = lives + 1 
        print("You recieve a health potion! Leaving the store.")
    elif playerChoice == "2":
        print("You recieve nothing and leave the store.")

gameShop()

# below demonstrates the usage of for loops using in and range by printing the
# the numbers 1 through 10
counter = 0
for count in range(0, 11):
    print(counter)
    counter += 1

# this is to print a new line between both counters for clarity
print("\n")

# below is a counter that prints the number 1 through 10 in descending order
counter2 = 10
for descendingCount in range(10, 0, -1):
    print(counter2)
    counter2 -= 1


# below is an example of a function returning the difference between two digits
# used "not" to show knowledge of usage as well, even though it may not be the
# cleanest usage of it

def numDifference(num1, num2):
    if not (num1 > num2):
        calcDiff = num2 - num1
    elif num1 == num2:
        num1 == num2
        calcDiff = 0
    elif num1 > num2:
        calcDiff = num1 - num2
    return calcDiff


def moreThanTen():
    numberInput1 = int(input("\nPlease input a number: "))
    numberInput2 = int(input("Please input a second number: "))

    difference = numDifference(numberInput1, numberInput2)
    print("The difference between the two numbers is", difference)


moreThanTen()
