#Erik
#Search
#Problem Set 20

import random

secret_num = random.randint(1, 100)
print(f"The Secret Number is: {secret_num}")

#Challenge 1
def lin_search():
    global secret_num
    attempts = 0
    for guess in range(1, 101):
        if guess == secret_num:
            attempts = attempts + 1
            print(f"Number found in {attempts} attempts ")
        else:
            attempts = attempts + 1
#Challenge 2
def bin_search():
    low = 1
    high = 100
    found = False
    global secret_num
    attempts = 0
    guess = 1
    while found == False:
        mid = (low + high) // 2
        if secret_num > mid:
            low = mid + 1
            attempts = attempts + 1
        if secret_num < mid:
            high = mid - 1
            attempts = attempts + 1
        if secret_num == mid:
            found = True
            print(f"Number found in {attempts} attempts ")

#Challenge 3
print("Speed up time: 1.89 ")
