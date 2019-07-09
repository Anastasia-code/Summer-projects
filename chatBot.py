#chatBot for experimenting with python functions.
import random
# --- Define your functions below! ---
def intro_self():  #a void function that returns nothing
    print("Hi! I'm chatBot. Write whatever you want. Type 'exit' to stop running me. Type 'game' to play rock, paper, scissors")

def greeting(response):
    # Define a list of possible ways the user might say hello.
    greetings = ["hi", "hello", "hey", "hey there", "sup"]
    if response.lower() in greetings:
        return True

def default():
    return("Sorry I don't know how to respond.")

def process_input(response):
    if response=="game":
        game()
    elif greeting(response): #if True
        print("Nice to meet you")
    elif "my" in response.lower() or "tired" in response.lower() or "sleepy" in response.lower():
        print("I hope you have a better day!")  #could make a function but unecessary since  only one print
    elif "i'm" in response.lower() or "i am" in response.lower():
        print("Good to hear")
    else:
        print(default())

def game():
    playerP = input("Type 'rock', 'paper', or 'scissors'").lower()  #.lower() converts to lowercase
    options=["rock", "paper", "scissors"]
    computerP = random.choice(options)  #either rock, paper, or scissors is chosen by psuedorandom
    print("Computer chose: " + computerP)
    #Below are situations that can occur in the game
    if "rock" in playerP.lower():
        if computerP=="rock":
            print("Tie! Try again.")
            game()
        elif computerP=="paper":
            print("You lost.")
        elif computerP=="scissors":
            print("You won!")
    elif "paper" in playerP.lower():
        if computerP=="rock":
            print("You won!")
        elif computerP=="paper":
            print("Tie! Try again.")
            game()
        elif computerP=="scissors":
            print("You lost.")
    elif "scissors" in playerP.lower():
        if computerP=="rock":
            print("You lost.")
        elif computerP=="paper":
            print("You won!")
        elif computerP=="scissors":
            print("Tie! Try again.")
            game()
    else:
        print("Invalid choice.")

# --- Put your main program below! ---
def main():
    intro_self()  #function prints an introduction about chatBot
    while True:
        print()  #empty line for format
        answer = input("(What will you say?) ")
        if answer=="exit":  #leave code if inputted 'exit'
            break
        else:
            process_input(answer)  #else process what the user inputted


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
