import school_scores
list_of_scores = school_scores.get_all()

# print(list_of_scores[0])

# for i in list_of_scores:
#     print(i)

# print(list_of_scores[0]["GPA"])
# print(list_of_scores[0]["State"])

# for row in list_of_scores:
#     print(row['State']["Name"], row["Year"])

for row in list_of_scores:
    print(row['Gender'], row["GPA"])
