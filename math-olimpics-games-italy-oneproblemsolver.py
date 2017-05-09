#!/usr/bin/python3
from itertools import permutations
from math import factorial
from time import time

def main():
    cardset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    killers = [8, 9, 10, 8, 9, 10, 8, 9, 10, 8]
    defeats = [0] * 10

    

    cases = permutations(cardset)
    total = factorial(len(cardset))

    for case in cases:
        for card, killer, count in zip(case, killers, range(0, 10)):
            if card == killer:
                defeats[count] += 1
                break

    #print ('Ho perso ' + str(defeats) + ' volte e ho vinto ' + str(total - defeats) + ' volte su ' + str(total) + ' possibili mazzi.')
    
    defeats_tot = 0

    for sub_defeats, count in zip(defeats, range(1, 11)):
        print('Ho perso ' + str(sub_defeats) + ' volte per la ' + str(count) + '^ carta')
        defeats_tot += sub_defeats
    print('Ho perso in tutto ' + str(defeats_tot) + ' volte')


start_time = time()
main()
print ('Elapsed time: ' + str(time() - start_time) + ' seconds.')
