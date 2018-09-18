# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

import json
import athletemodel
import yate

#names = athletemodel.get_names_from_store()
names = athletemodel.get_namesID_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))