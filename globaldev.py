import global_development
import matplotlib.pyplot as plt

listOfReport = global_development.get_reports()

UnitedStates = []
China = []
Indonesia = []
Ethiopia = []
Jordan = []
Years = []

for list in listOfReport:
    if list["Country"] == "United States":
        UnitedStates.append(list["Data"]["Health"]["Birth Rate"])
    elif list["Country"] == "China":
        China.append(list["Data"]["Health"]["Birth Rate"])
    elif list["Country"] == "Indonesia":
        Indonesia.append(list["Data"]["Health"]["Birth Rate"])
    elif list["Country"] == "Ethiopia":
        Ethiopia.append(list["Data"]["Health"]["Birth Rate"])
    elif list["Country"] == "Jordan":
        Jordan.append(list["Data"]["Health"]["Birth Rate"])
    elif list["Country"] == "Germany":
        Years.append(list["Year"])


#x and y + title
plt.xlabel('Year')
plt.ylabel('Birth Rate Percentage')
plt.title('Birth rate each year by country')
#countries legend
x1 = Years
y1= UnitedStates
plt.plot(x1, y1, color = 'purple', label = "United States")
x2 = Years
y2= China
plt.plot(x2, y2, label = "China")
x3 = Years
y3= Indonesia
plt.plot(x3, y3, label = "Indonesia")
x4 = Years
y4 = Ethiopia
plt.plot(x4, y4, label = "Ethiopia")
x5 = Years
y5 = Jordan
plt.plot(x5, y5, label = "Jordan")
plt.legend()
plt.show()




# for list in listOfReport:
#
# UnitedStates.append(listOfReport["Data"]["Health"]["Birth Rate"])
#
# print(UnitedStates)
