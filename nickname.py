#Erik
#Nickname
#Create a food superhero nickname based on user input

def nickname():
    print("You will receive a culinary super's name!")
    kind = input("Are you a food or a drink?")
#Food options
    if kind == "food":
        choose = input("Are you a vegetable? (yes or no)")
        if choose == "yes":
            what = input("Are you good or evil?")
            if what == "good":
                print("You are the Cabbage Crusader!")
            else:
                print("You are the Radish Raider!")
        else:
            what = input("Are you evil or good?")
            if what == "good":
                print("You are the Super Sandwich!")
            else:
                print("You are the Donut Destroyer!")

#Drink options
    if kind == "drink":
        choose = input("Are you a fountain drink? (yes or no)")
        if choose == "yes":
            what = input("Are you good or evil?")
            if what == "good":
                print("You are the Soda Supreme!")
            else:
                print("You are the Tyrannical Tea!")
        else:
            what = input("Are you evil or good?")
            if what == "good":
                print("You are the Milkshake Monolith!")
            else:
                print("You are the Electrolyte Executioner!")
nickname()
