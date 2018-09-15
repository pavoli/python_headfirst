# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

import helper

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([helper.sanitize(t) for t in self.times]))[0:3])

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_time):
        self.times.extend(list_of_time)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return (Athlete(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return (None)

'''
sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
print(type(sarah))
print(sarah)
print(sarah.name)
print(sarah.dob)
print(sarah.times)
'''

james = get_coach_data('james.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))

vera = Athlete('Vera Vi')
vera.add_time('1.22')
vera.add_times(['2.22', '1-21', '1.58'])
print(vera.top3())