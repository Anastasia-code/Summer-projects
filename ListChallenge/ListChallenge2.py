#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Menu order: main, sides, dessert
sides = ["fries", "salad", "mashed potatoes", "bread"]
main = ["Steak", "Shrimp", "Fish"]
dessert = ["cake", "brownies", "cookies", "ice cream"]

#Generates a random integer.
randomInt1 = randint(0, len(sides)-1)
randomInt2 = randint(0, len(main)-1)
randomInt3 = randint(0, len(dessert)-1)

print("Your Menu: " + main[randomInt2] + " with a side of " + sides[randomInt1] + " and " + dessert[randomInt3])
