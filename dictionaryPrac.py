names_ages={
  "A" : [10,20,30],  #key can be any data type
  'B' : "12",
  "C" : 15==15,
  'D' : 18
}

print(names_ages)  #prints out whole dictionary

# ageOfA=names_ages['A']  #accesses the value for the key
# print(ageOfA[1])  #prints 20

for name in names_ages:
    age = names_ages[name]
    # print(age)  #prints out the value (which is the age)
    # print(name) #prints out all the keys (the first part before the colon)
    print(name, age)  #prints out "name #"

for num in names_ages.values():
    print(num)  #prints out the values (ex: [10,20,30]  12   True   18)

users={}  #new empty dictionary
users['D'] = 30  #Adds a key and value pair to the dictionary
users['E'] = 20
users['D'] = 40  #replaces the 30 from previous entry
print(users)  #prints out entire dictionary
