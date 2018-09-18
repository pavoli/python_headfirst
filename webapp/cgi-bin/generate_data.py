# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

import cgi, json, sys
import athletemodel, yate


#athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athletes_name = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athletes_name)
print(yate.start_response('application/json'))
#print(json.dumps(athletes[athletes_name].as_dict))
print(json.dumps(athlete['Name'].as_dict))