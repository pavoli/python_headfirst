# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

import pickle
from athletelist import AthleteList
import sqlite3

db_name = 'coachdata.sqlite'


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return (AthleteList(templ.pop(0), templ.pop(0), templ))
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
    return (all_athletes)


def get_names_from_store():
    #athletes = get_from_store()
    #response = [athletes[each_athlete].name for each_athlete in athletes]
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute('''select name from athletes''')
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return (response)


def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute('''select name, id from athelets''')
    response = results.fetchall()
    connection.close()
    return (response)


def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    results = cursor.execute('''select name, dob from athletes where id=?''', (athlete_id,))
    (name, dob) = results.fetchone()

    results = cursor.execute('''select value timing_data where athlete_id=?''', (athlete_id,))
    data = [row[0] for row in results.fetchall()]
    response = {
        'Name'  : name,
        'DOD'   : dob,
        'data'  : data,
        'top3'  : data[0:3]
    }
    connection.close()
    return (response)