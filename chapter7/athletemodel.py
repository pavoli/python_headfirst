# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

import pickle
from athletelist import AthleteList
from athletelist import Athlete


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return (Athlete(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return (None)


def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return (all_athletes)


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return all_athletes

#print(dir())

the_files = ['sarah.txt', 'james.txt', 'julie.txt', 'mikey.txt']
data = put_to_store(the_files)
print(data)

data_copy = get_from_store()
for each_athlete in data_copy:
    print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)