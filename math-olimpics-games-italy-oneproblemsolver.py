#!/usr/bin/python3
from itertools import permutations
from math import factorial
from time import time

def main():
    cardset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    killers = [8, 9, 10, 8, 9, 10, 8, 9, 10, 8]
    defeats = 0

    cases = permutations(cardset)
    total = factorial(len(cardset))

    for case in cases:
        for card, killer in zip(case, killers):
            if card == killer:
                defeats += 1
                break

    print ('Ho perso ' + str(defeats) + ' volte e ho vinto ' + str(total - defeats) + ' volte su ' + str(total) + ' possibili mazzi.')

start_time = time()
main()
print ('Elapsed time: ' + str(time() - start_time) + ' seconds.')
