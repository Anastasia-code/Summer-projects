import json

# Creates an empty dictionary to store responses.
answers = {}

'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''
def dictionary():
    print(answers) # Prints the context of the dictionary.

# def edit():   #Currently can't edit specific parts of the code, but can delete previous entry and try again by recalling survey()
#     input1=input("Would you like to edit your 'name', 'netflix' show, 'movie', 'app', or 'sleep'?").lower().strip()
#     if input1=="name":
#         realName=input("Type your name:")
#     # # elif input1=="netflix":
#     # #     netflix =
#     # answers[name] = ["Fixed name":]

def survey():
    name = input("What is your name?")
    # age = input("What is your age?")
    netflix = input("What is your favorite netflix show?")
    movie = input("What is your favorite movie?")
    # city = input("What city do you live in?")
    # people = input("How many people live in your home more than 50% of the time?")
    # hours = input("How many hours per week do you spend on the phone?")
    app = input("What app do you use most frequently?")
    sleep = input("How many hours of sleep do you get on average?")

    answers[name] = [{"netflix": netflix, "movie": movie, "app": app, "sleep":sleep}]    #adds this to the empty dictionarys

    input3 = input("Would you like to edit your answers? Type 'yes' or 'no'")
    if input3.lower().strip()=="yes":   #makes input all lower case and without white spaces.
        del answers[name]  #deleted that entry
        survey()  #user redoes everything
    elif input3.lower().strip()=="no":
        return #goes back to main function
    else:
        print("Invalid choice.")
        input3 = input("Would you like to edit your answers? Type 'yes' or 'no'")

def main():
    while True:
        user_input = input("Would you like to take the survey(1), see the data(2), or exit (3)?")
        if user_input == "1":
            survey()
        elif user_input =="2":
            dictionary()
        elif user_input == "3":
            break
        else:
            print("Invalid choice.")
            continue


if __name__ =="__main__":
    main()


jsonanswer = json.dumps(answers)
# print(jsonanswer)

with open('survey.txt','w') as json_file:
    json.dump(jsonanswer, json_file)
