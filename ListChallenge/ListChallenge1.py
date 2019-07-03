#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of names you want to choose from.
aList = ["Barley", "Penny", "Daisy", "Sage", "Aspen", "Bane", "Alex", "Snow", "Sugar"]
bList = ["East", "West", "North", "South", "Compass", "Park", "Spice"]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
bRandomIndex = randint(0, len(bList)-1)


print(aList[aRandomIndex] + " "+ bList[bRandomIndex]) #Make a random first and last name
