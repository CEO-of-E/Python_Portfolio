#Erik and Brian
#Slots
#Runs a simulated slot machine

#Init
import random
import time
symbols = ["♠", "♡ ", "♢ ", 7]
weight = [0.40, 0.30, 0.20, 0.1]
score = 0
score2 = 0
#Functions
#Prob_test checks probability of spins
def prob_test():
    ask = input("Which size stake? (50/100/500)")
    stake2 = ask
    global score2
    wins = 0
    jack = 0
    losses = 0
    for i in range(1000):
                        spin2 = []
                        for i in range(3):
                            slot1 = random.choices(symbols, weights=weight, k=1)[0]
                            spin2.append(slot1)
                        if spin2[0] == spin2[1] == spin2[2]:
                            win = stake2 * 3
                            score2 = score2 + win
                            wins = wins + 1
                        if spin2[0] == 7 and spin2[1] == 7 and spin2[2] == 7:
                            win = stake2 * 7
                            score2 = score2 + win
                            jack = jack +1
                        elif spin2[0] != spin2[1] != spin2[2] or spin2[0] == spin2[1] != spin2[2] or spin2[0] != spin2[1] == spin2[2]:
                            loss = stake2/2
                            score2 = score2 - loss
                            losses = losses + 1

    print(f"Score: {score2}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Jackpots: {jack}")
#Machine handles spins
def machine():
    global score
    while True:
        print(f"Slot Machine Symbols: {symbols}")
        print(f"You have {score} in chips")
        stake = input("Please set spin bet (50/100/500) ")
        try:
            stake = int(stake)
            if True:
                if stake > score:
                    print("Insufficient chips.")
                    time.sleep(1.5)
                    break
                else:
                    if stake == 50 or stake == 100 or stake == 500:
                        spin = []
                        for i in range(3):
                            slot1 = random.choices(symbols, weights=weight)
                            spin.append(slot1)
                        print("Spinning")
                        time.sleep(2.5)
                        print(spin)
                        if spin[0] == spin[1] == spin[2]:
                            print("Win!")
                            win = stake * 3
                            score = score + win
                            print(f"+ {win} points.")
                        if spin[0] == 7 and spin[1] == 7 and spin[2] == 7:
                            print("Jackpot!")
                            win = stake * 7
                            score = score + win
                            print(f"+ {win} points.")
                        elif spin[0] != spin[1] != spin[2] or spin[0] == spin[1] != spin[2] or spin[0] != spin[1] == spin[2]:
                            print("Loss")
                            loss = stake/2
                            score = score - loss
                            print(f"- {loss} points.")
                        break
        except:
            print("Invalid bet.")
            time.sleep(1.5)
#Bal handles the entry of chips into the slot machine
def bal():
    global score
    while True:
        balance = input("Please enter chips (Increments of 50) ")
        try:
            balance = int(balance)
            if True:
                score = balance + score
                break
        except:
            print("Invalid amount.")
            time.sleep(1.5)
#Main streamlines the process in a simplified menu
def main():
    global score
    bal()
    while True:
        start = input("Enter 'S' to spin or 'E' to exit ")
        if start == "E":
            print("$$$ Thank you for entering! $$$")
            break
        if start == "S":
            machine()
            retry = input("Spin again or cash out? (Y/N) ")
            if retry == "Y":
                if score == 0:
                    print("You are out of chips. :(")
                    bal()
                else:
                    machine()
            if retry == "N":
                print("$$$ Thank you for playing! $$$")
                print(f"You end with {score} points")
                break
            else:
                print("Please try again.")
        else:
            print("Please try again.")
#Main
print("$$$ Welcome to E & B's Slot Machine! $$$")
main()

