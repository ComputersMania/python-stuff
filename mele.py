pickRate = [0, 2, 3, 4, 5, 6, 7]
                                                                                # Lunedì, martedì, mercoledì, giovedì, venerdì, sabato, domenica

def picked(startDay, startPop, life):                                                     #StartDay: giorno della settimana del primo giorno di raccolta, life:durata in giorni della raccolta
    population = startPop
    picked = 0
    for day in range(0 + startDay, life + startDay):
        currentPickRate = pickRate[day % len(pickRate)]
        if population >= currentPickRate:
            picked += currentPickRate
            population -= currentPickRate
        population += 1
    return picked

print(picked(5, 1, 304))
