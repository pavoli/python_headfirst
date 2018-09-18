# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

import cgi, os, time, sys
import yate
import sqlite3


print(yate.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
curr_time = time.asctime(time.localtime())

print(host + ', ' + addr + ', ' + curr_time + ': ' + method + ": ", end='', file=sys.stderr)

form = cgi.FieldStorage()
#for each_form_item in form.keys():
#    print(each_form_item + '->' + form[each_form_item].value, end=' ', file=sys.stderr)
#print(file=sys.stderr)
the_id = form['Athlete'].value
the_time = form['Time'].value

connection = sqlite3.connect('coachdata.sqlite3')
cursor = connection.cursor()
cursor.execute('insert into timing_data(athlete_id, value values(?,?)', (the_id, the_time))
connection.commit()
connection.close()

print('OK.')