#Erik
#4/1
#Tortoise & the hare simulation ()

#Init
import random
from fractions import Fraction
#Functions
def race_super(times):
    tortoise_wins = 0
    hare_wins = 0
    for i in range(times):
        finish_line = 50
        tortoise_pos = 0
        hare_pos = 0
        hare_asleep = False
        while tortoise_pos < finish_line and hare_pos < finish_line:
            tort_move = random.randint(1,3)
            tortoise_pos = tortoise_pos + tort_move
            sleep = random.randint(1,100)
            if sleep <= 80:
                hare_asleep == True
            else:
                hare_asleep == False
                hare_move = random.randint(1,10)
                hare_pos = hare_pos + hare_move
        if tortoise_pos >= finish_line:
            tortoise_wins = tortoise_wins + 1
        else:
            hare_wins = hare_wins + 1
    print(f"🐢 Tortoise Wins: {tortoise_wins}")
    print(f"🐇 Hare Wins: {hare_wins}")
    print(Fraction(tortoise_wins, times))
#Main
race_super(100)
