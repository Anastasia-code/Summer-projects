import json
person_dict = {"name": "Frank", "age": 39}

with open('person.txt', 'w') as json_file:   #This makes a notepad on desktop with the data
    json.dump(person_dict,json_file)

jsonanswer = json.dumps(person_dict)
print(jsonanswer)
