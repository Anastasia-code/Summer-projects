import health
import matplotlib.pyplot as plt

healthData = health.get_all_reports()

diseases=[]
year=[]

for row in healthData:
    diseases.append(row["disease"])
    year.append(row["year"])

plt.scatter(diseases,year)
plt.title('Diseases found over the years')
plt.show()

#For testing if there is a jump between 1955 and 1970s in the graph
# for row in healthData:
#     if row["disease"]=="PERTUSSIS":
#         print(row["year"])




#----------------------NOTES--------------------------------------
#For a line graph
# plt.plot(disease, year)
# plt.plot()
# plt.legend([])
# plt.xlabel()
# plt.show()

#Attempts at Seaborn until realizing that don't know know how to access my own data set.
# # Installed in command prompt: pip install git+https://github.com/mwaskom/seaborn.git
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set(style="ticks", color_codes=True)
# tips = sns.load_dataset("tips")               #How to get own data?
# sns.catplot(x="day", y="total_bill", data=tips);
