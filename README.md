# Python_Portfolio
search (1).py — Linear vs. Binary Search Demonstration
Function:
This program generates a random secret number between 1 and 100 and compares two search algorithms: a linear search (lin_search) and a binary search (bin_search). The goal is to show how many attempts each method would take to locate the secret number.
Interesting Features:
Uses Python's random.randint() to create a different target number each run.
Implements both linear search (checking numbers one-by-one) and binary search (repeatedly halving the search range).
Demonstrates the efficiency advantage of binary search over linear search.
Includes a printed "Speed up time" statistic, suggesting the author compared the performance of the two methods.

simulation_cont (1).py — Tortoise and Hare Race Simulation
Function:
This program simulates multiple races between a tortoise and a hare based on random movement rules. The tortoise moves steadily each turn, while the hare can either sleep or move much farther, creating an element of chance.
Interesting Features:
Uses probability to model the classic fable's characters.
Runs many races (race_super(100)) to gather statistical results.
Tracks total wins for both competitors and calculates the tortoise's win rate using Python's Fraction class.
Demonstrates a simple Monte Carlo simulation approach, where repeated random trials reveal long-term outcomes.
Note: There appears to be a bug where hare_asleep == True and hare_asleep == False use comparison operators (==) instead of assignment (=), meaning the sleep state never actually changes.

slots.py — Interactive Slot Machine Game
Function:
This is a text-based casino slot machine where players deposit chips, place bets, spin reels, and win or lose points based on symbol combinations. It also includes a probability-testing mode to simulate many spins automatically.
Interesting Features:
Uses weighted random selection (random.choices) so some symbols appear more often than others.
Features multiple betting levels (50, 100, or 500 chips).
Includes a jackpot system where three 7s award a larger payout.
Uses time.sleep() delays to create a more realistic slot-machine experience.
Contains a separate prob_test() function that can simulate 1,000 spins to analyze the game's odds.
Tracks player balance and allows repeated play through a menu system.
Potential Issues:
In prob_test(), user input is stored as a string, which would cause errors when multiplying payouts.
The jackpot check occurs after the regular win check, potentially awarding both payouts.
Symbols in the main game are stored as lists (random.choices(...)) rather than direct values, which can make comparisons less intuitive.

Overall Theme
All three files are educational projects focused on probability, simulation, and algorithmic thinking:
search (1).py → Algorithm efficiency (linear vs. binary search).
simulation_cont (1).py → Probability simulation and statistics.
slots.py → Randomized game design with weighted probabilities and user interaction.
They show a progression from basic algorithms to simulations and finally a complete interactive game.
