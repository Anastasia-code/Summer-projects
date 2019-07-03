#List Challenges categorized by functions

#imports the ability to get a random number
from random import *
def challenge1():
    #Create the list of names you want to choose from.
    aList = ["Barley", "Penny", "Daisy", "Sage", "Aspen", "Bane", "Alex", "Snow", "Sugar"]
    bList = ["East", "West", "North", "South", "Compass", "Park", "Spice"]

    #Generates a random integer.
    aRandomIndex = randint(0, len(aList)-1)
    bRandomIndex = randint(0, len(bList)-1)

    print(aList[aRandomIndex] + " "+ bList[bRandomIndex]) #Make a random first and last name


def challenge2():
    #Menu order: main, sides, dessert
    sides = ["fries", "salad", "mashed potatoes", "bread"]
    main = ["Steak", "Shrimp", "Fish"]
    dessert = ["cake", "brownies", "cookies", "ice cream"]

    #Generates a random integer.
    randomInt1 = randint(0, len(sides)-1)
    randomInt2 = randint(0, len(main)-1)
    randomInt3 = randint(0, len(dessert)-1)

    print("Your Menu: " + main[randomInt2] + " with a side of " + sides[randomInt1] + " and " + dessert[randomInt3])


def challenge3():
    #American Haiku 3 syllables, 5 syllable, 3 syllables.
    Line1 = ["Waves crashing", "Stars shining", "Peace, harmony", "Let's get it"]
    Line2 = ["I don't want nothing", "Paper cuts hurting", "Hands shaking a lot", "Big brain energy"]
    Line3 = ["Hands clapping", "Need bandage", "Give some love", "This is whack"]

    #Generates a random integer.
    randomInt1 = randint(0, len(Line1)-1)
    randomInt2 = randint(0, len(Line2)-1)
    randomInt3 = randint(0, len(Line3)-1)

    print(Line1[randomInt1])
    print(Line2[randomInt2])
    print(Line3[randomInt3])

while True:
    user_input = input("Would you like a random name (1), a menu (2), or an American Haiku (3)?")

    if user_input=="1":
        challenge1()
    elif user_input=="2":
        challenge2()
    elif user_input=="3":
        challenge3()
    else:
        print("Invalid choice.")
        continue
