# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

import cgi, cgitb
import athletemodel
import yate

cgitb.enable()

#athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_name)

print(yate.start_response())
print(yate.include_header("NUAC's Timing Data"))
#print(yate.header("Athelete: " + athlete_name + ', DOB: ' + athletes[athlete_name].dob + "."))
print(yate.header("Athelete: " + athlete['Name'] + ', DOB: ' + athlete['DOB'] + "."))
print(yate.para('The top times for this athlete are:'))
#print(yate.u_list(athletes[athlete_name].top3()))
print(yate.u_list(athlete['top3']))
#print(yate.para("The entire set of timing data is: " + str(athletes[athlete_name].clean_data) + " (duplicates removed.)"))
print(yate.para("The entire set of timing data is: " + str(athlete['data']) + " (duplicates removed.)"))
print(yate.include_footer({"Home": "/index.html", "Select another athlete": "generate_list.py"}))