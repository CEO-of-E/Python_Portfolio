#Erik
#ch3
#Finishes challenge 3

#Init
import pandas as pd
data = pd.read_csv("hacker.csv")
id = data['Log_ID'].tolist()
ip = data['IP_Address'].tolist()
protocol = data['Protocol'].tolist()
kb = data['Data_KB'].tolist()
time = data['Time'].tolist()
descript = data['Description'].tolist()
filter = []

#Functions
def findprob1(fail):
    for i in range(len(id)):
        if fail in descript[i]:
            filter.append(ip[i])
    print(filter)
    filter.clear()
def findprob2(amount):
    for i in range(len(kb)):
        if amount <= kb[i]:
            filter.append(time[i])
            filter.append(kb[i])
            filter.append(descript[i])
    print(filter)
    filter.clear()
def findprob3(term):
    for i in range(len(id)):
        if term in descript[i]:
            filter.append([i])
    print(len(filter))
    filter.clear()
#Main
findprob1("Failed")
findprob2(100000)
findprob3("Force")
