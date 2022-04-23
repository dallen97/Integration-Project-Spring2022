"""My first quiz program"""
__author__ = "Dustin Allen"


# Program Description- This program will become a short text based quiz
# adventure. basically a quiz with extra steps
# sprint 1 goal is to create basic start and  some calculations
# sprint 2 goal is to create multiple phases in the adventure
# sprint 3 goal is to have adventure complete with
# two one question quizzes and an ending quiz composed of two questions


def main():
    """This function calls upon the main function for this small
    quiz adventure program to work"""

    # Setting the variable wrongAnswers here for use later on in the program
    wrongAnswers = 0
    def gameShop():

        '''This function is the gift shop before the third encounter'''

        print("Welcome to the gift shop")
        print(
            "Here is a list of available items \n1. Health Potion - this item"
            "removes one wrong answer in the final average"
            "\n2. Recieve nothing and leave the shop")
        playerChoice = input("Please choose an option from the list above: ")
        while not (playerChoice == "2" or playerChoice == "1"):
            playerChoice = input("Invalid choice."
                                 " Please choose an option from the list")
        if playerChoice == "1":
            if wrongAnswers == 0:
                print("You have gotten no answers wrong, potion had no effect")
            else:
                wrongAnswers = wrongAnswers - 1
                print("You recieve a health potion! Leaving the store.")
        elif playerChoice == "2":
            print("You recieve nothing and leave the store.")

    playerName = input("Please enter a chosen name ")
    print("Welcome" + " " + playerName, end=" ")
    print("to a very short quiz adventure! \n")

    print("\n--------The adventure is now starting---------")

    # Below starts the adventure with some flavor dialogue
    print("\nLooking at your surroundings, you notice three paths before you."
          " There are two doors on either side of the room with a long hallway"
          " before you.")
    print(
        "Locks on the hallway door tell you that you have to "
        "explore the rooms"
        " beside you first to fully escape this situation.")
    # Each room will contain a short quiz with the
    # final room containing a 3 part
    # quiz encounter to end the adventure
    # Below is the templates for each room. Each room
    # will have two look around or
    # inspection options with the final third option being the small room quiz
    # up to two actions are allowed in the room

    print("\nYou arrive in the first room. To your left is a book"
          " on something"
          " called python.")
    print(
        "To your right is a figure holding a key to the door in the hallway.")

    # range function is to allow instant quiz option or to prevent
    # the user from
    # pressing options 1 or 2 and never reaching the quiz
    # room1 = 0
    for room1 in range(0, 1):
        choice1 = input("You decide there are three actions you can take."
                        "\n1. Open the python book "
                        "\n2. Approach the figure"
                        "\n3. Attempt to leave the room"
                        "\nChoose your action from the list above: ")
        # while not the valid choices, have the player choose again from
        # the list
        while not (choice1 == "1" or choice1 == "2" or choice1 == "3"):
            choice1 = input(
                "\nInvalid Choice. Choose an option from the list: ")

        if choice1 == "1":
            print(
                "\nYou open the book sadly realizing it is not a book"
                " on snakes"
                "but instead contains math :(\nWhile most of the"
                " text is blurred"
                " and unreadable. One section does appear to be intact."
                "\nIt talks about various operators with their corresponding"
                " symbols. One in particular catches your eye as the operator"
                " name is crossed out.\nIt is described as "
                "being the remainder"
                " of the division of two numbers.\nAs much fun as it has been"
                "reading about math you quickly grow bored and move on.")
            choice1 = input("\n1. Read the book again"
                            "\n2. Approach the figure"
                            "\n3. Leave the room"
                            "\nChoose another action from the list above: ")
            room1 = room1 + 1
        if choice1 == "2":
            print("\nYou look at the figure but notice the key is held within"
                  " the figures hands. The figure seems to be unmoving"
                  " and the key"
                  " seems to be unmoving as well.")
            choice1 = input("1. Read the python book"
                            "\n2. Look at the figure again"
                            "\n3. Leave the room"
                            "\nChoose your action from the list above: ")
            room1 = room1 + 1
        # choice 3 prints a blank statement and adds to the counter to
        # proceed the adventure
        if choice1 == "3":
            print("")
            room1 = room1 + 3

    print("\nYou decide it is time to leave and approach"
          " the door to leave the room. As you attempt to leave you"
          " are stopped by the figure in the room. "
          "The figure states 'You aren't"
          " able to leave the room that easily."
          "\nI have a little quiz and if you"
          " answer corectly you will be allowed to leave with my key'")
    print("\nThe question is: In python there are multiple shortcut operators"
          "to handle various mathematical funtions."
          " Which operator corresponds"
          "to the action of acquiring the remainder of x divided by y?")

    # Below is the first quiz in the program
    answer = str(input("1. Modulus % \n2. Exponent ** \n3. Floor Division // "
                       "\n4. Multiplication * \nPlease choose an answer from "
                       "the list above: "))
    # while not is used to contain any odd inputs that the user
    # may enter and to
    # redirect them to try again
    while not answer == "1":
        wrongAnswers = wrongAnswers + 1
        answer = str(input("Incorrect answer. Please try again: "))
    if answer == "1":
        print("Correct Answer! You may proceed.")

    print("\nAfter retrieving the key you return"
          " to the main room and prepare to"
          "enter the second room.")

    print("\nAfter entering the room you notice there is a board with some"
          "strange diagram on it.\nAnother figure is in the room this time as"
          "well.")

    for room2 in range(0, 1):
        choice2 = input("It's time to move your feet and make some choices."
                        "\n1. Inspect the diagram"
                        "\n2. Approach the figure"
                        "\n3. Leave the room"
                        "\nChoose an option from the list above: ")

        while not (choice2 == "1" or choice2 == "2" or choice2 == "3"):
            choice2 = input("\n invalid choice. choose again")
        if choice2 == "1":
            print("\n You inspect the diagram and notice that it's actually"
                  "the icon for wifi!\nAlthough there is no wifi "
                  "here you see that"
                  "the board has listed the names of"
                  " various types of networks."
                  "\nLocal Area Network - LAN"
                  "\nMetropllitan Area Network - MAN"
                  "\nWide Area Network - WAN "
                  "\nThe fourth only has the abbreviation - VPN")

            choice2 = input("\n1. Inspect the diagram again "
                            "\n2. Approach the figure"
                            "\n3. Leave the room"
                            "\nChoose an option from the list above: ")
            room2 = room2 + 1
        if choice2 == "2":
            print("\nYou approach the figure and attempt to pry the key away."
                  "Surprisingly it doesn't work so it must be time"
                  "for another quiz")
            choice2 = input("\n1. Inspect the diagram"
                            "\n2. Approach the figure once again"
                            "\n3. Leave the room"
                            "\nChoose an option from the list above: ")
            room2 = room2 + 1
        if choice2 == "3":
            print("\nYou decide that it's time to leave.")
            room2 = room2 + 3

    print("\nOnce again you are stopped and the figure"
          " arises telling you that"
          "you must pass another quiz to get the key and leave the room."
          "\nThe question is as follows: What does VPN stand for?")

    answer = str(input("\n1. Vertex processing network"
                       "\n2. Violet purple network"
                       "\n3. Virtual private network"
                       "\n4. Vegetable procesor"
                       "\nPlease choose an answer from the list above: "))
    # while not is used to contain any odd inputs that the user may enter and
    # redirect them to try again
    while not answer == "3":
        wrongAnswers = wrongAnswers + 1
        answer = str(input("Incorrect answer. Please try again: "))
    if answer == "3":
        print("Correct Answer! You may proceed.")

    print("\nAfter leaving the second room you move"
          " down the hallway and unlock"
          "the door.\nOnce you unlock the door you notice a small tent with a"
          "sign saying free gift on it. Other than that this room is empty"
          "besides the exit to the building you have been stuck in.")
    # This is to see if the player would like to enter the gift shop
    giftEnter = input("Would you like to enter the gift shop?"
                      "\nType 'y' to enter or 'n' to not enter and proceed: ")
    # This contains any invalid inputs and prompts user to input valid choices
    while not (giftEnter == "y" or giftEnter == "n"):
        input("Invalid choice. Please type 'y' to enter the gift shop or "
              "'n' to not enter and proceed: ")
    if giftEnter == "y":
        gameShop()
    elif giftEnter == "n":
        print("\nYou have chosen to skip the gift shop.")

    print("You head towards the exit but un-surprisingly you're stopped by"
          " another figure.\nOne more test is required to leave."
          " This time three"
          " questions will be asked of you.")

    print("\nThe first question is as follows: What does the abbreviation"
          " LAN stand for?")

    answer = str(input("\n1. Low amplitude network"
                       "\n2. Local access network"
                       "\n3. LAN network"
                       "\n4. Local area network"
                       "\nPlease choose an answer from the list above: "))
    # while not is used to contain any odd inputs that the user
    # may enter and redirect them to try again
    while not answer == "4":
        wrongAnswers = wrongAnswers + 1
        answer = str(input("Incorrect answer. Please try again: "))
    if answer == "4":
        print("Correct Answer! Proceeding to next question")

    print("\nYour next question is: How would you write the following math"
          " equation in python: The square of 5 divided by 5")

    answer = str(input("\n1. print('5**2 / 5')"
                       "\n2. 5*3 / 5"
                       "\n3. 5^3 / 5"
                       "\n4. 5**3 / 5"
                       "\nPlease choose an answer from the list above: "))
    # while not is used to contain any odd inputs that the user may enter and
    # redirect them to try again
    while not answer == "4":
        wrongAnswers = wrongAnswers + 1
        answer = str(input("Incorrect answer. Please try again: "))
    if answer == "4":
        print("Correct Answer! Time for the last question!")

    print(
        "\nThe final question is: Which of the would NOT result in an error.")

    answer = str(input("\n1. print('sample number ' + 85)"
                       "\n2. print('Here is a sample statement')"
                       "\n3. newNumber = 100 + randomWord"
                       "\nPlease choose an answer from the list above: "))
    # while not is used to contain any odd inputs that the user may enter and
    # redirect them to try again
    while not answer == "2":
        wrongAnswers = wrongAnswers + 1
        answer = str(input("Incorrect answer. Please try again: "))
    if answer == "2":
        print("Correct Answer! You have passed all the questions!")

    print(
        "It's finally time to leave this building. Thank you for running this"
        " program.")
    print("\nBelow you will be shown your percentage of correct answers.")
    # This is the for the end of the quiz adventure. It displays the
    # congratulations message along with number of correct
    # questions and percentage of questions that were correct

    # questionTotal variable is set here to ensure the following formula works

    questionTotal = 5
    print("Congratulations you passed the adventure!"
          " The number of questions you"
          "answered wrong is", wrongAnswers)
    # This formula calculates their quiz average based on their wrong answers.
    questionAverage = questionTotal / (questionTotal + wrongAnswers)
    print("Your question average is", questionAverage)

    # below is for integration project requirements

    print("\n----------Below are integration project requirements-----------")
    # modulus
    print("\nThe following displays modulus of"
          " 35%5 which is equal to", 35 % 5)

    # floor division
    print("The following displays floor"
          " division of 75//2 which equals", 75 // 2)

    # below is for integration project string operator requirement
    repeatString = int(
        input("\nChoose number of times to repeat the phrase Hello! "))
    print("Hello! " * repeatString)

    # below demonstrates the usage of for loops
    # using in and range by printing the the numbers 1 through 10
    counter = 0
    for count in range(0, 11):
        print(counter)
        counter += 1

    # below is a counter that prints the number
    # 1 through 10 in descending order
    counter2 = 10
    for descendingCount in range(10, 0, -1):
        print(counter2)
        counter2 -= 1

    # below is an example of a function returning
    # the difference between two digits
    # used "not" to show knowledge of usage as well,
    # even though it may not be the
    # cleanest usage of it

    def numDifference(num1, num2):
        '''This function is called on by the moreThan function
        and performs the calculation for that function.'''
        if not (num1 > num2):
            calcDiff = num2 - num1
        elif num1 == num2:
            num1 == num2
            calcDiff = 0
        elif num1 > num2:
            calcDiff = num1 - num2
        return calcDiff

    def moreThan():

        '''This function calls on the function numDifference then prints out
        the difference'''

        numberInput1 = int(input("\nPlease input a number: "))
        numberInput2 = int(input("Please input a second number: "))

        difference = numDifference(numberInput1, numberInput2)
        print("The difference between the two numbers is", difference)

    moreThan()


if __name__ == '__main__':
    main()

