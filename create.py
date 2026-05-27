#CREATE task
#World Democracy Index
#This program provides specific information from a country democracy data set based on user input

#Initialize
import webbrowser
import random
import pandas as pd
data = pd.read_csv("w_democracy_index.csv")
id = data['id'].tolist() #Numbers the countries for storage
rank = data['Rank'].tolist() #Stores the global rankings of countries
country = data['Country'].tolist() #Lists the names of the countries
scoring = data['Score'].tolist() #Captures the overall score of the country
elect = data['Electoral process and pluralism'].tolist() #Scores the country on how they elect
gov_funct = data['Functioning of government'].tolist() #Scores the country on how stable their government processes are
pol_particip = data['Political partici­pation'].tolist() #Scores the country on how active voters and political parties are
pol_culture = data['Political culture'].tolist() #Scores the country on how diverse their political beliefs are
liberty = data['Civil liberties'].tolist() #Scores the country on civil rights and protections
regime = data['Regime type'].tolist() #Labels the government type of the nation
region = data['Region'].tolist() #Stores the geographic region of the country
filter = [] #All data searched by the functions will be stored in this array
regime_info = ["https://tinyurl.com/cnpyajjw", "https://tinyurl.com/yeytxkrv", "https://tinyurl.com/efhhupd7", "https://tinyurl.com/44snpdxv"]

#Functions
def continent(cont): #This function searches for countries in a specific region
        if cont.lower() == "americas": #Result of being in the Americas
            special1 = "america"
            for i in range(len(id)):
                if special1.lower() in region[i].lower():
                    filter.append(country[i])
            try:
                print(random.choice(filter))
            except:
                print("No countries were found. Try again.")
            filter.clear()
        elif cont.lower() == "europe": #Result of being in Europe
            for i in range(len(id)):
                if cont.lower() in region[i].lower():
                    filter.append(country[i])
            try:
                print(random.choice(filter))
            except:
                print("No countries were found. Try again.")
            filter.clear()
        elif cont.lower() == "africa": #Result of being in Africa
            for i in range(len(id)):
                if cont.lower() in region[i].lower():
                    filter.append(country[i])
            try:
                print(random.choice(filter))
            except:
                print("No countries were found. Try again.")
            filter.clear()
        elif cont.lower() == "middle east": #Result of being in the Middle East
            for i in range(len(id)):
                if cont.lower() in region[i].lower():
                    filter.append(country[i])
            try:
                print(random.choice(filter))
            except:
                print("No countries were found. Try again.")
            filter.clear()
        elif cont.lower() == "asia & oceania": #Result of being in Asia or Oceania
            special = "asia"
            for i in range(len(id)):
                if special.lower() in region[i].lower():
                    filter.append(country[i])
            try:
                print(random.choice(filter))
            except:
                print("No countries were found. Try again.")
            filter.clear()
        else:
            print("Invalid region.")

def government(type): #This function searches countries based on government type
    for i in range(len(id)):
        if type.lower() == regime[i].lower():
            filter.append(country[i])
    try:
        print(random.choices(filter))
    except:
        print("Invalid government type. Try again.")
    filter.clear()

def nation(name): #This function provides additional information on a specific country mentioned by the user
    for i in range(len(id)):
        if name.lower() == country[i].lower():
            filter.append(f"Global ranking: {rank[i]}")
            filter.append(f"Election process: {elect[i]}")
            filter.append(f"Government function: {gov_funct[i]}")
            filter.append(f"Political participation: {pol_particip[i]}")
            filter.append(f"Political culture: {pol_culture[i]}")
            filter.append(f"Liberty: {liberty[i]}")
            filter.append(f"Overall score: {scoring[i]}")
            filter.append(f"Government type: {regime[i]}")
    for i in range(len(filter)):
        print(filter[i])
    if len(filter) == 0:
        print("No country was found. Try again.")
    filter.clear()

def main(): #This function operates the menu and serves the user with the previous functions
    print("====Welcome to the Democracy Index!====")
    while True:
        start = input("Would you like to begin a search? (yes/no) ") #
        if start.lower() == "no":
            print("Thank you for your time. I hope you enjoyed!")
            break
        if start.lower() == "yes":
            print("")
            print("***Search Options***")
            print("Choose how you want to search for countries:")
            print("Regime type")
            print("Name")
            print("Region")
            how = input("Choice: ")
            if how.lower() == "regime type":
                print("")
                print("Choose a regime to search for: ")
                print("Full democracy")
                print("Flawed democracy")
                print("Hybrid regime")
                print("Authoritarian")
                reg = input("Choice: ")
                government(reg)
                if reg.lower() == "full democracy":
                    print(webbrowser.open(regime_info[0]))
                if reg.lower() == "flawed democracy":
                    print(webbrowser.open(regime_info[1]))
                if reg.lower() == "hybrid regime":
                    print(webbrowser.open(regime_info[2]))
                if reg.lower() == "authoritarian":
                    print(webbrowser.open(regime_info[3]))
            elif how.lower() == "name":
                print("")
                nm = input("What is the name of the country? ")
                nation(nm)
            elif how.lower() == "region":
                print("")
                print("Choose a specific region to search:")
                print("Americas")
                print("Europe")
                print("Africa")
                print("Middle East")
                print("Asia & Oceania")
                where = input("Choice: ")
                continent(where)
            elif how.lower != "regime type" or how.lower != "name" or how.lower != "region":
                print("Try again.")
        else:
            print("Try again.")

#Main
main()

#Sources
#Dataset info:
#URL of dataset: https://www.eiu.com/n/campaigns/democracy-index-2020/

#Additional info from Wikipedia:
#URL of regime info: https://en.wikipedia.org/wiki/The_Economist_Democracy_Index
