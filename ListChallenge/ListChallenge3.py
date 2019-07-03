#imports the ability to get a random number (we will learn more about this later!)
from random import *

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
