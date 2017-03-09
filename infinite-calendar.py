#!/usr/bin/python3

m = {1: (0, 6), 2: (3, 2), 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}

daysOfWeek = {
    0: 'sunday',
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday'
}

class date:

    def isBiss(self):
        return (anno % 4 == 0 and anno % 100 != 0) or anno % 400==0

    def m(self):
        ms = m[self.month]
        if type(ms) == 'tuple':
            return ms[1] if self.isBiss() else ms[0]
        else:
            return ms

    def g(self):
        return self.day % 7

    def a(self):
        return (self.year % 100) % 28 + int(((self.year % 100) % 28) / 4)

    def s(self):
        return 6 - (int(self.year / 100) % 4) * 2

    def dayOfWeek(self):
        return daysOfWeek[(self.g() + self.m() + self.a() + self.s()) % 7]

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

day, month, year =  map(int, input().split('/'))
print (date(day, month, year).dayOfWeek())