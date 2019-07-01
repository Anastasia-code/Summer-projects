start = '''
You are in Fablehaven forest and need to find the core of the forest in order to escape.
A trustworthy wizard told you before you entered, "Select the path that feels the most wrong in order to continue or else you'll be stuck forever."
You arrive at your first choice: A sunny path along the river on the left or A dark tangled path along the trees on the right.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decided left and were almosot drowned by a siren. Luckily with your strong lung capacity, you escaped. Now soaking wet, you must choose how to survive the rest of the time.")
    print("You scold yourself for forgetting what the wizard told you. You know that you won't be as lucky next time.")
    print("You meet your next choice: A warm fire on the left to dry yourself or A stormy path to your right")
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        print("While drying by the fire a centuar attacked you and left you unable to move. GAME OVER.")
    elif user_input == "right":
        print("Good job, you made the right choice even though you are now freezing from your previous mistake by the river.")
        print("You think about going to sleep and see a shelter nearby. Do you go to left toward the shelter or continue your cold path?")
        print("Type 'left' to go left or 'continue' to continue.")
        user_input = input()
        if user_input == "left":
            print("While sleeping in the shelter, it flooded and your lungs couldn't save you. GAME OVER.")
        elif user_input == "continue":
            print("Although you made the right choice by the wizard's words, hypothermia has taken over. GAME OVER.")

elif user_input == "right":
    print("You chose the right, or should you say wrong path. You hear scary noises and want to go home.")
    print("You hear a rustling in the bushes on your left and dread fills you inside. You look to your right and hear a pleasant melody.")
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        print("A scream erupts from the rustling bushes but then realize it is your own. You take a deep breath and meet your next choice.")
        print("You see a lively fairy who offers her assistance to you. Do you accept?")
        print("Type 'yes' or 'no'.")
        user_input = input()
        if user_input == "yes":
            print("The fairy turns into a witch and curses you. GAME OVER.")
        elif user_input == "no":
            print("Aww you missed out on the help...or maye you saved yourself an unpleasant death. You finally find the core of the forest. You're elated, but now have to find a way back.")
            print("Unfortunately the game creator has not finished that part yet, so have fun with that. :)")
    elif user_input == "right":
        print("The melody turn out to be a satyr with a flute. Unfortunately you get too close to close his hind legs and he kicks you. GAME OVER.")
