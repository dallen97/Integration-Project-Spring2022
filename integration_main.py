##Dustin Allen
##Program Description- This program will become a short text based adventure
##sprint 1 goal is to create basic start and  some calculations
##sprint 2 goal is to create multiple phases in the adventure
##sprint 3 goal is to have adventure complete with
##one battle and an ending


playerName=input('Please enter a chosen name ')
print("Welcome" + " " + playerName, end=" ")
print("to an unnamed text based adventure game \n")

print("insert story stuff here \n")

##Menu of starting choices for the player to choose
print("1.Sword - increases weapon damage by 3")
print("2.Bag of gold - starting gold increased by 10")
print("3.Armor - increases armor value by 3")
print("4.Nothing - Not sure why you would select this but here \n")
##Below is a list containing the valid options.
validChoices = ["1","2","3","4"]

##if statements for player starting choices
##added while loop to contain invalid choices
CharBonus = input("Please select a character bonus from the list above. ")
while CharBonus < "1" or CharBonus > "4":
    CharBonus = input("Invalid choice. Please try again. ")
if CharBonus == "1" :
    print("You have chosen the Sword starting bonus")
    WeaponDamage = int(3)
elif CharBonus == "2" :
    print("You have chosen the Bag of gold starting bonus")
elif CharBonus == "3" :
    print("You have chosen the Armor starting bonus")
    armorUpgrade = int(3)
elif CharBonus == "4" :
    print("You have chosen nothing for the starting bonus")

print("\nHere are your starting stats:")

##stats at the start of the adventure
health = int(10)
strength = int(5)
armor = int(2)
money = int(15)
CurrentMoney = money
print("Your starting health is", health)
print("Your starting strength is", strength)
print("Your starting armor is", armor)
##sep= command used to remove space between $ and money value
print("Your starting money is $", CurrentMoney, sep="")

print("\nLooking at your surroundings, you notice three paths before you."
      "There are two doors on either side of the room you are in while in front"
      "of you is a long dark corridor. Your intution tells you that it would be"
      "best to inspect the rooms to your side before pushing ahead.")

##Below is the first choice for player movement. A while loop has been
##implemented to contain invalid inputs. if statments will be added to reflect
##the players choice via their inputs

#below may be copied into a def statement or the structure copied for future
#movement
playerChoice = input("\n1.Left Room.\n2.Right Room."
                     "\n3.Head down the corridor\nChoose your path: ")

while playerChoice > "3" or playerChoice < "1":
    playerChoice = input("\nA strange thought appears in your head and you are"
                         " unable to figure out which way to go. Choose again.")

#a variable named "room" may be added to allow for next phase of the adventure
#unsure of whether to add this or to take a different route to make this work
if playerChoice == "1":
    print("\nYou have chosen to enter the room on the left.")
if playerChoice == "2":
    print("\nYou have chosen to enter the room on the right.")
if playerChoice == "3":
    print("\nYou have chosen to proceed down the dark hallway ignoring your"
          " inuition.")


##stat modifiers that might be implemented
##these lines will be revised
##and updated as the adventure developes

##Health System 
#newHealth = (health * HealthUpgrades)
#CurrentHealth = (newHealth - DamageTaken)

##Strength System - affects damage done in final encounter
#newStrength = (strength + WeaponDamage)

##Armor System (Armor blocks .5 Damage per Armor Value)
##(1 armor is .5 damage negated)
#newArmor = (armor + armorUpgrade)
##Damage System
#DamageTaken = (damage - (newArmor * 0.5))
#CriticalHit = ((damage**1.25) - (newArmor * 0.5))

##Currency System - moneyBonus refers to start
##newMoney refers to money pickup in adventure
moneyBonus = 0
newMoney = 0
CurrentMoney = (money + moneyBonus + newMoney)

##below is for integration project requirements

#modulus
print("\nThe following displays modulus of 35%5 which is equal to", 35%5)

##floor division
print("The following displays floor division of 75//2 which equals", 75//2)

##below is for integration project string operator requirement
repeatString= int(input("\nChoose number of times to repeat the phrase Hello! "))
print("Hello! " * repeatString)

##below is a defined statement for the one-time shop that will be implemented
##this will be moved to a line above to ensure the call will work when needed
def gameShop():
    print("Welcome to the shop")
    print("Here is a list of available items \n1. Health Potion")
    print("2. Sword Upgrade \n3. Nothing and leave the shop")
    playerChoice = input("Please choose an option from the list above: ")
    while playerChoice > "3" or playerChoice < "1":
        playerChoice = input("Please choose an option from the list")
    if playerChoice == "1":
        print("You recieve a health potion! Leaving the store.")
    elif playerChoice == "2":
        print("You recieved a sword upgrade! Leaving the store.")
    elif playerChoice == "3":
        print("You recieve nothing and leave the store.")

gameShop()

##below demonstrates the usage of for loops using in and range by printing the
##the numbers 1 through 10
counter = 0
for count in range(0,11):
    print(counter)
    counter += 1

##this is to print a new line between both counters for clarity
print("\n")

##below is a counter that prints the number 1 through 10 in descending order
counter2 = 10
for descendingCount in range(10,0,-1):
    print(counter2)
    counter2 -= 1

#below is an example of a function returning the difference between two numbers
#used "not" to show knowledge of usage as well, even though it may not be the
#cleanest usage of it

def numDifference(num1, num2):
    if not (num1 > num2):
        calcDiff = num2 - num1
    elif num1 == num2:
        num1 == num2
        calcDiff = 0
    elif num1>num2:
        calcDiff = num1 - num2
    return calcDiff


def moreThanTen():
    numberInput1 = int(input("\nPlease input a number: "))
    numberInput2 = int(input("Please input a second number: "))

    difference = numDifference(numberInput1, numberInput2)
    print("The difference between the two numbers is", difference)


moreThanTen()
