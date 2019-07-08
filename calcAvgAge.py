#Calculate average of ages

list = [5,12,3,56,24,78,1,15,44]
sumAges=0
for i in range(len(list)):   #another way: for i in list:
  sumAges+=list[i]                        #     sumAges+=i
print(sumAges/len(list))
